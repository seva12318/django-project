<script>
export default {
  components: {
    Modal,
  },
  data() {
    return {
      showModal: false,
      newTeacher: {
        surname: "",
        name: "",
        patr: "",
      },
    };
  },
  methods: {
    onFormSumbit() {
      this.showModal = false;
      this.lessonsStore.addTeacher(
        this.newTeacher.surname,
        this.newTeacher.name,
        this.newTeacher.patr
      );
      this.newTeacher = {
        surname: "",
        name: "",
        patr: "",
      };
    },
  },
};
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
//     lessonsStore.addTeacher(surname.value, name.value, patr.value)
// }

function onUpdateClick(id, event){
    lessonsStore.updTeacher(id,  event.name, event.surname, event.patr )
}


onBeforeMount( () => {
    lessonsStore.fetchTeachers();
})


</script>

<template>
<h2>Преподаватели</h2>
<button id="show-modal" @click="showModal = true">Добавить</button>

  <Teleport to="body">
    <!-- use the modal component, pass in the prop -->
    <modal
      :show="showModal"
      @submit="onFormSumbit()"
      @close="showModal = false"
    >
      <template #header>
        <h3>Добавить преподавателя</h3>
      </template>
      <template #body>
        <input type="text" v-model="newTeacher.surname" placeholder="Фамилия" />
        <input type="text" v-model="newTeacher.name" placeholder="Имя" />
        <input type="text" v-model="newTeacher.patr" placeholder="Отчество" />
        
      </template>

      <template #footer> </template>
    </modal>
  </Teleport>

<hr />

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

 
</template>
<style>

</style>