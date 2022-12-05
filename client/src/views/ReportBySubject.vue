<script setup>
import { storeToRefs } from "pinia";
import { useTeacherStore } from "../stores/teacherStore";
import { computed, onBeforeMount, ref } from "vue";
import xlsx from "json-as-xlsx"
import { groupByStudent } from "../util/group";
const teacherStore = useTeacherStore();
const { subjects, lessons, subjectStudents, report } =
  storeToRefs(teacherStore);

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
</script>

<script>
import { useLessonsStore } from "../stores/lessons";
import ReportRow from "@/components/ReportRow.vue";
import _ from "lodash";
import { useTeacherStore } from "../stores/teacherStore";
import { formatDate } from "../util/formatDate";

function downloadxlsx(){
    var jsonData = "[ { \"sheet\": \"Etuds\", \n \"columns\": [\n{ \"label\": \"ФИО\", \"value\": \"user\" },";
    var header = new Array(); // { label: "User", value: "user" }, // Top level data
    header.push('user');
    var currstr = document.getElementById("jour").outerText + '\n';
    for (var i = 0; i < document.getElementById("head").childElementCount - 1; i++){
      var ind = currstr.indexOf('\n');
      header.push('d' + (i + 1).toString(10));
      
      jsonData = jsonData + '{ \"label\": \"'+ currstr.slice(0, ind) +'\", \"value\": \"' + header[i + 1] + '\"},'
      currstr = currstr.slice(ind + 1);
    }
    jsonData = jsonData.slice(0,jsonData.lastIndexOf(',')) + '],\n\"content\": ['
    for (var i = 1; i < document.getElementById("jour").childElementCount; i++){
      jsonData = jsonData + '{'
      for (var j = 0; j < header.length; j++){        
        var ind = currstr.indexOf('\n');
        jsonData = jsonData + ' \"' + header[j] + '\" : \"' + currstr.slice(0, ind) + '\"';
        if (j < header.length - 1) jsonData = jsonData + ',';
        currstr = currstr.slice(ind + 1);
        
      }
      jsonData = jsonData + '},'
    }
    jsonData = jsonData.slice(0,jsonData.lastIndexOf(',')) + ']}]';
    console.log(jsonData);
    
    let settings = {
      fileName: "Отчёт по предмету " + document.getElementById("selecsuj").options[document.getElementById("selecsuj").selectedIndex].text, // Name of the resulting spreadsheet
      extraLength: 3, // A bigger number means that columns will be wider
      writeMode: 'writeFile', // The available parameters are 'WriteFile' and 'write'. This setting is optional. Useful in such cases https://docs.sheetjs.com/docs/solutions/output#example-remote-file
      writeOptions: {}, // Style options from https://github.com/SheetJS/sheetjs#writing-options
      RTL: false, // Display the columns from right-to-left (the default value is false)
    }
    let data = JSON.parse(jsonData);
    xlsx(data, settings)
  }

export default {
  data() {
    return {
      selectedSubject: "",
    };
  },
  methods: {
    onSelectClick(id) {
      this.teacherStore.fetchReportBySubjectId(id);
      this.teacherStore.fetchStudentsBySubjectId(id);
      this.teacherStore.fetchSubjectLessons(id);
    },
    onClick() {
      
    },
  },
};
</script>

<template>
  <div class="report_wrapper">
    <h2>Отчёт по предметам</h2>
    <div class='cl'>
   <li> <select v-model="selectedSubject" id = "selecsuj">
      <option disabled value="" >Выберите один из вариантов</option>
      <option v-for="s in subjects" :value="s.id">
        {{ `${s.name} (${s.level})` }}
      </option>
    </select>
   </li>

   <li> <button class = "btn btn-info ms-2" @click="onSelectClick(selectedSubject)">Показать</button></li>
  <li><button class = "btn btn-info ms-2" @click="onClick(downloadxlsx())">Скачать отчёт</button></li>
  </div>
      <div id = "jour" v-if="!Boolean(lessons) || !Boolean(subjectStudents)"> Выберите предмет</div>

      <div id = "jour" v-else>
        <div id = "head" class="journal_header">
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
  gap: 10px;
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
  border-right: 1px solid rgb(0, 85, 16);
}


.btn-info{
  color:white;
  background-color: rgb(5, 33, 84 );
  height: 30px;
  width: 170px;
  font-size:50;
  
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
    margin: 20px;
    padding: 20px;
  }
  
  
  option{
    color: rgb(5, 33, 84 );
  
    background-color: rgb(129, 168, 240);
  }
select{
  width: 300px;
}

</style>
