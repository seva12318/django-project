<script setup>
import { storeToRefs } from "pinia";
import { computed, onBeforeMount, ref } from "vue";
import _ from "lodash";

import { useTeacherStore } from "../stores/teacherStore";
import { groupByStudent } from "../util/group";
import { formatDate } from "../util/formatDate";

const teacherStore = useTeacherStore();
const { subjects, lessons, subjectStudents, report } =
  storeToRefs(teacherStore);

const selectedSubject = ref("");

const sortedStudents = computed(() => {
  return subjectStudents !== null
    ? // ascending sort
      subjectStudents.value.sort((s1, s2) => (s1.surname > s2.surname ? 1 : -1))
    : null;
});

const sortedLessons = computed(() => {
  return lessons !== null
    ? // ascending sort
      lessons.value.sort((l1, l2) => (l1.date > l2.date ? 1 : -1))
    : null;
});

onBeforeMount(() => {
  teacherStore.fetchTeacherSubjects(1);
});

function onSelectClick(id) {
  teacherStore.fetchReportBySubjectId(id);
  teacherStore.fetchStudentsBySubjectId(id);
  teacherStore.fetchSubjectLessons(id);
}
</script>

<template>
  <div class="report_wrapper">
    <h2>Отчёт по предметам</h2>
    <select v-model="selectedSubject">
      <option disabled value="">Выберите один из вариантов</option>
      <option v-for="s in subjects" :value="s.id">
        {{ `${s.name} (${s.level})` }}
      </option>
    </select>
    <button @click="onSelectClick(selectedSubject)">Показать</button>

    <div v-if="!Boolean(lessons) || !Boolean(subjectStudents)">
      Выберите предмет
    </div>

    <div v-else>
      <div class="journal_header">
        <span></span>
        <span v-for="lesson in sortedLessons">{{
          formatDate(lesson.date)
        }}</span>
      </div>

      <div class="journal_row" v-for="s in sortedStudents">
        <span>{{ `${s.surname} ${s.name} ${s.patr}` }}</span>
        <span v-for="lesson in sortedLessons">{{
          report[
            report.findIndex(
              (record) =>
                record.lessons === lesson.id &&
                record.students_name === `${s.surname} ${s.name} ${s.patr}`
            )
          ]?.mark || ""
        }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.report_wrapper {
  display: flex;
  flex-direction: column;
  gap: 20px;
  align-items: flex-start;
}
.journal_header {
  display: flex;
  justify-content: flex-start;
  margin-top: 20px;
}

.journal_header > span {
  border: 1px solid black;
  border-right: none;
  padding: 5px;
  width: 100px;
}
.journal_header > span:first-child {
  width: 300px;
}
.journal_header > span:last-child {
  border-right: 1px solid black;
}

.journal_row {
  display: flex;
  justify-content: flex-start;
}

.journal_row > span {
  border: 1px solid black;
  border-top: none;
  border-right: none;
  padding: 5px;
  width: 100px;

  display: flex;
  justify-content: center;
}

.journal_row > span:first-child {
  width: 300px;
  display: flex;
  justify-content: flex-start;
}

.journal_row > span:last-child {
  border-right: 1px solid black;
}
</style>
