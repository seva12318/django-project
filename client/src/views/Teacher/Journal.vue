<template lang="">
  <Loader
    v-if="
      !Boolean(subjectStudents) ||
      !Boolean(lesson) ||
      !Boolean(subject) ||
      isLoading
    "
  />
  <div class="journal_wrapper" v-else>
    <h2>
      {{
        `Урок от ${formatDate(lesson.date)} по предмету ${subject.name} (${
          subject.level
        })`
      }}
    </h2>
    <div class="journal_header">
      <span>№</span>
      <span>ФИО</span>
      <!-- <span>Школа</span> -->
      <span>Оценка</span>
    </div>
    <div class="journal_body" v-show="studentsWithMarks !== null">
      <JournalRow
        v-for="(student, index) in studentsWithMarks"
        :number="index + 1"
        :name="`${student.surname} ${student.name} ${student.patr}`"
        :mark="student.mark || null"
        :markId="student.markId"
        :onSave="onChangeMark.bind(null, student.id)"
      >
        <span>{{ index + 1 }}</span>
        <span>{{ `${student.surname} ${student.name} ${student.patr}` }}</span>
        <!-- <span>{{ student.school_title }}</span> -->
        <input type="number" :value="student.mark || 'Не проставлена'" />
      </JournalRow>
    </div>
    <div class="btn save" @click="navigateToLessons()">Сохранить</div>
  </div>
</template>
<script setup>
import { computed } from "vue";
import { storeToRefs } from "pinia";
import { useTeacherStore } from "../../stores/teacherStore";
import { formatDate } from "../../util/formatDate";
import Loader from "../../components/Loader/Loader.vue";
import JournalRow from "./JournalRow/JournalRow.vue";

const teacherStore = useTeacherStore();
// добавить уроки и удалить из data, когда появится ручка
const { subjectStudents, lesson, marks, subject, isLoading } =
  storeToRefs(teacherStore);

const sortedStudents = computed(() => {
  return subjectStudents !== null
    ? // descending sort
      subjectStudents.value.sort((s1, s2) => {
        return s1.surname > s2.surname ? 1 : -1;
      })
    : null;
});

const studentsWithMarks = computed(() => {
  return sortedStudents !== null && marks !== null
    ? sortedStudents.value.map((s) => ({
        ...s,
        mark: +marks.value[
          marks.value.findIndex((mark) => mark.students === s.id)
        ]?.mark,
        markId:
          marks.value[marks.value.findIndex((mark) => mark.students === s.id)]
            ?.id,
      }))
    : null;
});
</script>
<script>
export default {
  data() {
    return {
      subjectId: +this.$route.params.subjectId,
      lessonId: +this.$route.params.lessonId,
    };
  },
  methods: {
    onChangeMark(studentId, markId, mark) {
      console.log("STUDENT ID: ", studentId);
      console.log("MARK ID: ", markId);
      console.log("MARK: ", mark);
      console.log("LESSON ID: ", this.lessonId);
      if (markId) {
        this.teacherStore.updateMark({ markId, mark });
      } else {
        this.teacherStore.addMark({
          studentId,
          lessonId: this.lessonId,
          mark,
        });
      }
    },
    navigateToLessons() {
      this.$router.push({
        path: `/subjects/${this.subjectId}`,
      });
    },
  },
  beforeMount() {
    this.teacherStore.fetchStudentsBySubjectId(this.subjectId);
    this.teacherStore.fetchLessonById(this.lessonId);
    this.teacherStore.fetchMarksByLessonId(this.lessonId);
    this.teacherStore.fetchSubjectById(this.subjectId);
  },
};
</script>
<style scoped>
.journal_wrapper {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  flex: 1;
  width: 90%;
  padding: 50px 100px;
}

.journal_header {
  display: flex;
  justify-content: flex-start;
  margin-top: 20px;
}

.journal_header > span {
  width: calc(100% / 3);
  border: 1px solid black;
  border-right: none;
  padding: 5px;
}
.journal_header > span:first-child {
  width: 40px;
}

.journal_header > span:last-child {
  border-right: 1px solid black;
}

.btn {
  padding: 10px 20px;
  border-radius: 8px;
  background: #42b983;

  cursor: pointer;

  display: flex;
  flex-direction: column;
  gap: 10px;

  text-align: center;

  width: fit-content;
}
.btn.save {
  margin-top: 20px;
}
.btn:hover {
  opacity: 0.9;
  transform: scale(1.1);
}
</style>
