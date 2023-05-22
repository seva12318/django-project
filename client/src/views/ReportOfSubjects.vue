<script setup>
import { storeToRefs } from "pinia";
import { useLessonsStore } from "../stores/lessons";
import { computed, onBeforeMount, ref } from "vue";

import { groupByStudent } from "../util/group";

import { unformatDate, formatDate } from "../util/formatDate";

const lessonsStore = useLessonsStore();
const { subjects, lessons } = storeToRefs(lessonsStore);

let isSubjectsSortDescending = ref(false);
let isLessonsSortDescending = ref(false);

onBeforeMount(() => {
  lessonsStore.fetchSubjects();
  lessonsStore.fetchLessons();
});

const filteredLessons = computed(() =>
  lessons
    ? lessons.value.reduce((acc, val) => {
        const key = val["subjects"];
        if (acc[key]) {
          acc[key].push(val);
        } else {
          acc[key] = [val];
        }
        return acc;
      }, {})
    : null
);

const sortedSubjects = computed(() => {
  console.log("sort subjects");
  if (isSubjectsSortDescending) {
    return subjects
      ? subjects.value.sort((a, b) =>
          `${a.name} (${a.level})` > `${b.name} (${b.level})` ? -1 : 1
        )
      : null;
  } else {
    return subjects
      ? subjects.value.sort((a, b) =>
          `${a.name} (${a.level})` > `${b.name} (${b.level})` ? 1 : -1
        )
      : null;
  }
});

const sortedLessons = computed(() => {
  console.log(filteredLessons);

  return filteredLessons
    ? Object.keys(filteredLessons.value).reduce((acc, key) => {
        return {
          ...acc,
          [key]: filteredLessons.value[key].sort((a, b) =>
            isLessonsSortDescending
              ? a.date > b.date
                ? -1
                : 1
              : a.date > b.date
              ? 1
              : -1
          ),
        };
      }, {})
    : null;
});

function changeSubjectsSort() {
  isSubjectsSortDescending = !isSubjectsSortDescending;
}

function changeLessonsSort() {
  isLessonsSortDescending = !isLessonsSortDescending;
}
</script>

<template>
  <div class="report_wrapper">
    <h2>Отчёт по предметам и их урокам</h2>

  <table>
    <tr>
      <td @click="changeSubjectsSort()">Название предмета</td>
      <tr class="header">
        <td @click="changeLessonsSort()">Дата урока</td>
        <td>Тема урока</td>
        <td>Домашнее задание</td>
      </tr>
    </tr>
    <template v-for="s in sortedSubjects">
    <tr>
      <td style="justify-content: left;">{{ `${s.name} (${s.level})` }}</td>
      <td v-if="!filteredLessons[s.id]">
        <td>Уроки отсутствуют</td>
      </td>
      <template v-for="(lesson, index) in sortedLessons[s.id]" v-else >
        <tr class="data">
          <td >{{ lesson.date }}</td>
          <td >{{ lesson.topic }}</td>
          <td >{{ lesson.homework }}</td>
        </tr>
      </template>
    </tr>
  </template>
</table>
  </div>
</template>

<style scoped>
.report_wrapper {
  display: flex;
  flex-direction: column;
  gap: 20px;
  align-items: flex-start;
  padding-bottom: 50px;
}

table {
   border: 1px solid black;
   display: table;
   width:1100px;
   border-bottom: none;
}
td{
  border: 1px solid black;
  padding: 5px;
  width:500px;
  display: table-cell;
  justify-content: center;
  border-top: none;
  border-right: none;
  word-wrap: break-word;
  word-break: break-all;
}
tr{
  width: 600px;
  display: table-row-group;
}

.header td{
  width:1/3;
  display: table-cell;
  justify-content: center;
  word-wrap: break-word;
  word-break: break-all;
}
.data td{

  width:1/3;
  display: table-cell;
  justify-content: center;
  word-wrap: break-word;
  word-break: break-all;
}
</style>
