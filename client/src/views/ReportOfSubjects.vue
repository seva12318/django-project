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

    <div>
      <div class="journal_header">
        <span @click="changeSubjectsSort()">Название предмета</span>
        <span>Тема урока</span>
        <span @click="changeLessonsSort()">Дата урока</span>
        <span>Домашнее задание</span>
      </div>

      <div
        v-if="
          !Boolean(sortedSubjects) ||
          !Boolean(sortedLessons) ||
          !Boolean(filteredLessons)
        "
      >
        <div>{{ JSON.stringify(sortedSubjects) }}|||||||||||||||||||||</div>
        <div>{{ JSON.stringify(filteredLessons) }}|||||||||||||||||||||</div>
        <div>{{ JSON.stringify(sortedLessons) }}</div>
        Ждёмс
      </div>

      <div class="journal_row" v-for="s in sortedSubjects" v-else>
        <div>
          <span>{{ `${s.name} (${s.level})` }}</span>
          <span></span>
          <span></span>
          <span></span>
        </div>
        <div v-if="!filteredLessons[s.id]">
          <span></span>
          <span>Уроки отсутствуют</span>
          <span>Уроки отсутствуют</span>
          <span>Уроки отсутствуют</span>
        </div>
        <div v-for="(lesson, index) in sortedLessons[s.id]" v-else>
          <span></span>
          <span>{{ lesson.topic }}</span>
          <span>{{ lesson.date }}</span>
          <span class="homework">{{ lesson.homework }}</span>
        </div>
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
  padding-bottom: 50px;
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
  width: 250px;
  text-align: center;
  font-weight: 500;
  user-select: none;
}
.journal_header > span:first-child {
  user-select: none;
  cursor: pointer;
}
.journal_header > span:nth-child(3) {
  user-select: none;
  cursor: pointer;
}
.journal_header > span:last-child {
  border-right: 1px solid black;
}

.journal_row {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.journal_row > div {
  display: flex;
}

.journal_row span {
  border: 1px solid black;
  border-top: none;
  border-right: none;
  padding: 5px;
  width: 250px;

  display: flex;
  justify-content: center;
}

.homework {
  word-wrap: break-word;
  word-break: break-all;
}

.journal_row span:last-child {
  display: flex;
}

.journal_row span:last-child {
  border-right: 1px solid black;
}
</style>
