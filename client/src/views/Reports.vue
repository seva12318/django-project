<script setup>
import { storeToRefs } from "pinia";
import { useLessonsStore } from "../stores/lessons";
import { computed, onBeforeMount, ref } from "vue";

import { groupByStudent } from "../util/group";

const lessonsStore = useLessonsStore();
const { reports } = storeToRefs(lessonsStore);
const { schools } = storeToRefs(lessonsStore);

const reportsStored = computed(() => {
  return _(reports.value)
    .orderBy((x) => x[sortFiled.value])
    .value();
});

const reportByStudent = computed(() => {
  return reports.value ? groupByStudent(reports.value["school-journal"]) : [];
});

let sortFiled = ref("name");

onBeforeMount(() => {
  // lessonsStore.fetchReports("1");
  lessonsStore.fetchSchools();
});
</script>

<script>
import { useLessonsStore } from "../stores/lessons";
import ReportRow from "@/components/ReportRow.vue";
import _ from "lodash";

export default {
  data() {
    return {
      selectedSchool: "",
    };
  },
  methods: {
    onSelectClick(id) {
      console.log(id);
      console.log(this.reportsStored);
      console.log(this.reportsStored[0]);
      console.log(this.reportByStudent);
      this.lessonsStore.fetchReports(id);
    },
  },
};
</script>

<template>
  <select v-model="selectedSchool">
    <option disabled value="">Выберите один из вариантов</option>
    <option v-for="s in schools" :value="s.id">
      {{ s.title }}
    </option>
  </select>
  <button @click="onSelectClick(selectedSchool)">Показать</button>

  <div class="journal_header">
    <span>ФИО</span>
    <span>Предмет</span>
    <!-- <span>Школа</span> -->
    <span>Оценки</span>
  </div>
  <ReportRow
    v-for="(r, index) in reportByStudent"
    :number="index"
    :students_name="r.students_name"
    :lessons_name="r.lessons_name"
    :date="r.date"
    :mark="r.marks.join(' ')"
  />
</template>

<style scoped>
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

.journal_header > span:last-child {
  border-right: 1px solid black;
}
</style>
