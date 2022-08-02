<script>
export default {
  components: {
    Modal
  },
  data() {
    return {
      showModal: false
    }
  }
}
</script>
<script setup>
import { storeToRefs } from 'pinia';
import {computed, onBeforeMount, ref} from 'vue';
import {useLessonsStore} from '../stores/lessons';
import TeacherRow from '@/components/TeacherRow.vue';
import _ from 'lodash';
import Modal from '../components/modal-window.vue'

const lessonsStore = useLessonsStore(); 
const {teachers} = storeToRefs(lessonsStore);
let sortFiled = ref("name");

let surname = ref("");
let name = ref("");
let patr = ref("");

const teacherStored = computed(() =>{
    return _(teachers.value)
        .orderBy(x => x[sortFiled.value])
        .value();
});

function toggleSort(fildeName){
    sortFiled.value = fildeName
}

// function onSurnameClick(teacher){
//     console.log(teacher.surname)
// }

// function onNameClick(teacher){
//     console.log(teacher.name)
// }

function onDeleteClick(teacher){
    lessonsStore.deleteTeacher(teacher.id)
}

// function onFormSumbit(){
//     lessonsStore.addTeacher(surname.value, name.value, patr.value, school.value)
// }

function onUpdateClick(id, event){
    lessonsStore.updTeacher(id,  event.name, event.surname, event.patr )
}


onBeforeMount( () => {
    lessonsStore.fetchTeachers();
})


</script>

<template>
    <button @click="toggleSort('name')">По имени</button>
    <button @click="toggleSort('surname')">По фамилии</button>
    
            <TeacherRow 
              v-for="s in teacherStored" 
              :name = "s.name"
              :surname = "s.surname"
              :patr = "s.patr" 
              @surname-click = "onSurnameClick(s)"
              @name-click = "onNameClick(s)"
              @delete = "onDeleteClick(s)"
              @update = "onUpdateClick(s.id, $event)"
            />
    <hr> 

  <button id="show-modal" @click="showModal = true">Добавить</button>

  <Teleport to="body">
    <modal :show="showModal" @close="showModal = false">
      <template #header>
        <h3>Добавить учителя</h3>
      </template>
      <template #body>
       
        <h3>Данные учителя:</h3>
        
        <input type="text" v-model="surname" placeholder="Фамилия"/>
        <input type="text" v-model="name" placeholder="Имя"/>
        <input type="text" v-model="patr" placeholder="Отчество"/>
        
        </template>
       
        <template #footer> 
        </template>
    </modal>
  </Teleport>
</template>
<style>

</style>