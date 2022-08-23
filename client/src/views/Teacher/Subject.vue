<template lang="">
  <div class="wrapper">
    <Loader v-if="!Boolean(lessons) || !Boolean(subject) || isLoading" />
    <div class="subject_wrapper" v-else>
      <div class="subject_name">
        <span class="subject_title">{{
          `${subject.name} (${subject.level})`
        }}</span>
        <span>
          {{ `Время: ${subject.time}` }}
        </span>
      </div>
      <div class="lessons_wrapper" v-if="lessons.length === 0">
        <div class="subject_no_lessons">
          На данный момент у вас нет уроков по этому предмету
        </div>
        <div class="btn" @click="openAddLessonModal()">+ Добавить урок</div>
      </div>
      <div class="lessons_wrapper" v-else>
        <div class="btn" @click="openAddLessonModal()">+ Добавить урок</div>
        <div class="subject_lessons">
          <div class="subject_lesson" v-for="(lesson, index) in sortedLessons">
            <div>
              <span class="title">{{
                `Урок №${sortedLessons.length - index}`
              }}</span>
              <hr />
              <div>
                <span class="title">Тема: </span>
                <span>{{ lesson.topic }}</span>
              </div>
              <div>
                <span class="title">Дата: </span>
                <span>{{ formatDate(lesson.date) }}</span>
              </div>
              <hr />
              <span class="title">Домашнее задание:</span>
              <span>{{ `${lesson.homework}` }}</span>
              <hr />
            </div>
            <div class="btns">
              <div
                class="btn add_lesson"
                @click="
                  openEditLessonModal({
                    ...lesson,
                    number: sortedLessons.length - index,
                  })
                "
              >
                Редактировать
              </div>
              <div class="btn add_lesson" @click="navigateToLesson(lesson.id)">
                Открыть журнал
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <ModalLesson
    :showModal="showModal"
    :onClose="onModalClose"
    :onSubmit="isEdit ? onUpdateLesson : onAddLesson"
    :isEdit="isEdit"
    :lesson="currentLesson"
  />
</template>
<script setup>
import { computed } from "vue";
import { storeToRefs } from "pinia";
import { useTeacherStore } from "../../stores/teacherStore";
import Loader from "../../components/Loader/Loader.vue";
import ModalLesson from "./ModalAddLesson/ModalLesson.vue";

const teacherStore = useTeacherStore();
// добавить уроки и удалить из data, когда появится ручка
const { subject, lessons, isLoading } = storeToRefs(teacherStore);
const sortedLessons = computed(() => {
  return lessons !== null
    ? // descending sort
      lessons.value.sort((l1, l2) => (l1.date > l2.date ? -1 : 1))
    : null;
});
</script>
<script>
export default {
  data() {
    return {
      subjectId: this.$route.params.id,
      showModal: false,
      isEdit: false,
      currentLesson: {
        topic: "",
        homework: "",
        date: new Date(Date.now()).toISOString().split("T")[0],
      },
    };
  },
  methods: {
    navigateToLesson(lessonId) {
      // this.$router.push({ path: `/lessons/${lessonId}` });
      alert(`navigate to ${lessonId}`);
    },
    onModalOpen() {
      this.showModal = true;
    },
    onModalClose() {
      this.showModal = false;
    },
    formatDate(date) {
      // format from yyyy-mm-dd to dd.mm.yyyy
      return date.split("-").reverse().join(".");
    },
    onAddLesson(lesson) {
      this.teacherStore.addLesson({
        ...lesson,
        subjectId: Number(this.subjectId),
        date: lesson.date,
      });
      this.onModalClose();
      this.sortedLessons =
        this.lessons !== null
          ? // descending sort
            this.lessons.value.sort((l1, l2) => (l1.date > l2.date ? -1 : 1))
          : null;
    },
    onUpdateLesson(lesson) {
      this.teacherStore.updateLesson(lesson.id, {
        ...lesson,
        date: lesson.date,
      });
      this.onModalClose();
      this.sortedLessons =
        this.lessons !== null
          ? // descending sort
            this.lessons.value.sort((l1, l2) => (l1.date > l2.date ? -1 : 1))
          : null;
    },
    openAddLessonModal() {
      this.isEdit = false;
      this.currentLesson = {
        topic: "",
        homework: "",
        date: new Date(Date.now()).toISOString().split("T")[0],
      };
      this.onModalOpen();
    },
    openEditLessonModal(lesson) {
      this.isEdit = true;
      this.currentLesson = lesson;
      this.onModalOpen();
    },
  },
  beforeMount() {
    this.teacherStore.fetchSubjectLessons(this.subjectId);
    this.teacherStore.fetchSubjectById(this.subjectId);
  },
};
</script>
<style scoped>
.subject_wrapper {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  flex: 1;
  width: 90%;
  padding-top: 50px;
}
.subject_name {
  display: flex;
  flex-direction: column;
  font-size: 22px;
  font-weight: 600;
  text-align: center;
}
.lessons_wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
  gap: 20px;
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
.btn:hover {
  opacity: 0.9;
  transform: scale(1.1);
}
.subject_lessons {
  display: flex;
  flex-direction: row;
  justify-content: center;
  flex-wrap: wrap;
  gap: 10px;
  max-width: 100%;
  padding-bottom: 100px;
}
.subject_lesson {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 20px 40px;
  border-radius: 6px;
  border: 1px solid gray;
  min-width: 300px;
  max-width: calc(100% / 4);
}
.subject_lesson hr {
  margin-top: 10px;
  margin-bottom: 10px;
}
.subject_lesson .title {
  font-size: 18px;
  font-weight: 500;
}
.subject_lesson .btns {
  display: flex;
  flex-direction: column;
  gap: 10px;

  align-items: center;
}
.subject_no_lessons {
  margin-top: 200px;
  text-align: center;
}
</style>
