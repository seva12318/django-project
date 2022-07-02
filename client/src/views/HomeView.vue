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

const studentsStored = computed(() =>{
    return _(students.value)
        .orderBy(x => x[sortFiled.value])
        .value();
});

function toggleSort(fildeName){
    sortFiled.value = fildeName
}

function onSurnameClick(student){
    console.log(students.surname)
}

function onNameClick(student){
    console.log(students.name)
}

function onDeleteClick(student){
    lessonsStore.deleteStudent(student.id)
}

onBeforeMount( () => {
    lessonsStore.fetchStudents();
})
</script>

<template>
<h1>Главная страница</h1>
    <input type="text" v-model ="inputText">
    <div>Вы ввели: {{inputText}}</div>
    <button @click="toggleSort('name')">По имени</button>
    <button @click="toggleSort('surname')">По фамилии</button>
    <StudentRow 
        v-for="s in studentsStored" 
        :name = "s.name" 
        :surname = "s.surname"
        @surname-click = "onSurnameClick(s)"
        @name-click = "onNameClick(s)"
        @delete = "onDeleteClick(s)"
    />
</template>


<style>

</style>