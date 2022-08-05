<script setup>
import { storeToRefs } from 'pinia';
import {computed, onBeforeMount, ref} from 'vue';
import {useLessonsStore} from '../stores/lessons';
import StudentRow from '@/components/StudentRow.vue';
import _ from 'lodash';

const lessonsStore = useLessonsStore(); 
const {students} = storeToRefs(lessonsStore);
let sortFiled = ref("name");
let inputText = ref("");

let surname = ref("");
let name = ref("");
let patr = ref("");
let school = ref("");

const studentsStored = computed(() =>{
    return _(students.value)
        .orderBy(x => x[sortFiled.value])
        .value();
});

function toggleSort(fildeName){
    sortFiled.value = fildeName
}

function onSurnameClick(student){
    console.log(student.surname)
}

function onNameClick(student){
    console.log(student.name)
}

function onDeleteClick(student){
    lessonsStore.deleteStudent(student.id)
}

function onFormSumbit(){
    lessonsStore.addStudent(surname.value, name.value, patr.value, school.value)
}

function onUpdateClick(id, event){
   // console.log(id)
   // console.log(event)
    lessonsStore.updStudent(id,  event.surname, event.name)
}


onBeforeMount( () => {
    lessonsStore.fetchStudents();
})
</script>

<template>
<h1>Главная страница</h1>
    <input type="text" v-model ="inputText">
    <div>Вы ввели: {{inputText}}</div>
    
</template>


<style>

</style>