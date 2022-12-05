<script setup>
import { storeToRefs } from "pinia";
import { useLessonsStore } from "../stores/lessons";
import { computed, onBeforeMount, ref } from "vue";
import xlsx from "json-as-xlsx"
import { groupByStudent } from "../util/group";

import ReportRow from "@/components/ReportRow.vue";
import _ from "lodash";
import axios from 'axios';

const lessonsStore = useLessonsStore();
const { reports } = storeToRefs(lessonsStore);
const { schools } = storeToRefs(lessonsStore);
let selectedSchool = ref("");

function padStr(i) {
    return (i < 10) ? "0" + i : "" + i;
}
function resMark(etud_id, lessons_name, date){
    return groupedStudents.value[etud_id].lessons[lessons_name][date] || ""

}
const reportsStored = computed(() => {
  return _(reports.value)
    .orderBy((x) => x[sortFiled.value])
    .value();
});

const reportByStudent = computed(() => {
  return reports.value
    ? groupByStudent(reports.value["school-journal"] || [])
    : [];
});

let sortFiled = ref("name");

onBeforeMount(() => {
  // lessonsStore.fetchReports("1");
  lessonsStore.fetchSchools();
});

const journal = computed(() => {
  return reports.value["school-journal"] || [];
})

const lesDates = computed(() => {
  let r = _(journal.value)
    .map(x => x.date)
    .uniq()
    .map(x => new Date(x))
    .orderBy()
    .map(x => padStr(x.getFullYear()) + '-' +
              padStr(1 + x.getMonth()) +'-' +
              padStr(x.getDate()))
    .value();

    return r;
})

const groupedStudents = computed(() => {
  let data = {};
  for(let x of journal.value) {
      console.log(x.lessons_name);
      if (!data[x.students]) {
        data[x.students] = {
          lessons: {},
          students_name: x.students_name,
        }
      }

      if (!data[x.students].lessons[x.lessons_name]) {
        data[x.students].lessons[x.lessons_name] = {}
      }

      data[x.students].lessons[x.lessons_name][x.date] = x.mark;
  };
  console.log(data)
  return data;
})

async function fetchReports(subjectId) {

  let response = await axios.get(`/api/journals/${subjectId}/school/`);
  let res = response.data;
  let data1 = response['school-journal'];
  journal.value = data1;
  let header = new Array(); // { label: "User", value: "user" },
  let headeralias = new Array();
  header.push('ФИО'); headeralias.push('user');
  header.push('Предмет'); headeralias.push('suj');
  for (var i = 0; i < lesDates.value.length; i++) {
    header.push(lesDates.value[i]);
    headeralias.push('d' + i.toString());
  }
  console.log(header,headeralias)
  //forming a header
  let data = {sheet: "Etuds", columns: [],content: []};
  for (var i = 0; i < header.length; i++) {
    data.columns.push(
      {'label': header[i], value: headeralias[i]}
    )
  }
  //forming content
  for (let key0 in groupedStudents.value) {
    for (let key1 in groupedStudents.value[key0].lessons) {
      let currlist = { [headeralias[0]]: groupedStudents.value[key0].students_name, [headeralias[1]]: key1}
      for (let i = 2; i < header.length; i++){
        currlist[headeralias[i]] = resMark(key0,key1,header[i]) //etud_id, lessons_name, date
      }
      data.content.push(currlist)
    }
  }
  data = [data]
  let ectitle = document.getElementById("selececol").options[document.getElementById("selececol").selectedIndex].text;
  let settings = {
    fileName: "Отчёт для " + ectitle, // Name of the resulting spreadsheet
    extraLength: 3, // A bigger number means that columns will be wider
    writeMode: 'writeFile', // The available parameters are 'WriteFile' and 'write'. This setting is optional. Useful in such cases https://docs.sheetjs.com/docs/solutions/output#example-remote-file
    writeOptions: {}, // Style options from https://github.com/SheetJS/sheetjs#writing-options
    RTL: false, // Display the columns from right-to-left (the default value is false)
  }
  xlsx(data, settings)
}

function downloadXLSX() {
  let ec = document.getElementById("selececol")
    .options[document.getElementById("selececol").selectedIndex]
    .value.toString(10);
  fetchReports(ec);
}

function onSelectClick(id) {
  console.log(id);
  console.log(this.reportsStored);
  console.log(this.reportsStored[0]);
  console.log(this.reportByStudent);
  this.lessonsStore.fetchReports(id);

  
}

</script>

<template>
  <h2>Отчёт по школам</h2>

 <div class='cl'>
 <li> <select v-model="selectedSchool" id='selececol'>
    <option disabled value="" >Выберите один из вариантов</option>
    <option v-for="s in schools" :value="s.id">
      {{ s.title }}
    </option>
  </select></li>
<li><button class="btn btn-info ms-2" @click="onSelectClick(selectedSchool)">Показать</button></li>
<li> <button class="btn btn-info ms-2" @click="downloadXLSX">Скачать отчёт</button></li>
</div>
<div class='cl'>
  <hr style="border-color:  rgb(255, 255, 255); border-width: 0.5px;  " >
  <hr style="border-color:  rgb(255, 255, 255); border-width: 0.5px;  " >
</div>
  <table class="table table-bordered" >
    <thead>
      <th>ФИО</th>
      <th>Предмет</th>
      <th v-for="d in lesDates">{{d}}</th>
    </thead>
    <tbody>
      <template v-for="(student, sID) in groupedStudents">
        <tr v-for="(dates, lessonName) in student.lessons">
          <td>{{student.students_name}}</td>
          <td>{{lessonName}}</td>
          <th v-for="d in lesDates">
            {{ dates[d] }}
          </th>
        </tr>
      </template>
    </tbody>
  </table>

</template>

<style scoped>
.journal_header {
  display: flex;
  justify-content: flex-start;
  margin-top: 20px;
  
 
}

.journal_header>span {
  width: calc(100% / 3);
  border: 1px solid black;
  border-right: none;
  padding: 5px;
  
  
}

.journal_header>span:last-child {
  border-right: 1px solid black;
 
}
.disabledvalue{
  color: red;
  background-color: red;
}

.btn-info{
color:white;
background-color: rgb(5, 33, 84 );
height: 30px;
width: 170px;

}
.btn-info:hover{
  background-color: rgb(129, 168, 240);
}
.ul{
    
  margin: 700px;
  height: 50;
  padding: 200px 3000px;
  list-style: none ;
  font-size: 0px;
  text-align: center;
  background-color: #fff;

}
li{
 
  height: 50px;
  width: 20px;
  font-size: 20px;
  position: relative;
  margin: 1px;
  padding: 40px;
}

option{
  color: rgb(5, 33, 84 );

  background-color: rgb(129, 168, 240);
}

</style>
