<script setup>
import { storeToRefs } from "pinia";
import { useLessonsStore } from "../stores/lessons";
import { computed, onBeforeMount, ref } from "vue";

const lessonsStore = useLessonsStore();
const { reports } = storeToRefs(lessonsStore);
const { schools } = storeToRefs(lessonsStore);

const reportsStored = computed(() => {
  return _(reports.value)
    .orderBy((x) => x[sortFiled.value])
    .value();
});

let sortFiled = ref("name");
// let students_name = ref("");
// let lessons_name = ref("");
// let date = ref("");
// let mark = ref("");

onBeforeMount(() => {
  lessonsStore.fetchReports("1");
  lessonsStore.fetchSchools();
});

function onSelectClick(id){
  console.log(id)
   lessonsStore.fetchReports(id)
}
</script>

<script>
import { useLessonsStore } from "../stores/lessons";
import ReportRow from "@/components/ReportRow.vue";
import _ from "lodash";
</script>

<template>



      <select v-model="selectedSchool">
        <option  v-for="s in schools" :value="s.id">
          {{s.title}}
        </option>
      </select>
      <button @click="onSelectClick(selectedSchool)">Показать</button>
    
    <!-- не выводит список -->
  <ReportRow
    v-for="r in reportsStored"
    :students_name="r.students_name"
    :lessons_name="r.lessons_name"
    :date="r.date"
    :mark="r.mark"
  />
  <hr />
  
</template>

<style></style>