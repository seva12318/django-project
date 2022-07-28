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
import SubjectRow from '@/components/SubjectRow.vue';
import _ from 'lodash';
import Modal from '../components/modal-window.vue'

const lessonsStore = useLessonsStore(); 
const {subjects} = storeToRefs(lessonsStore);
let sortFiled = ref("name");

let name = ref("");
let level = ref("");
let time = ref("");
let teacher_fio = ref("");

const subjectStored = computed(() =>{
    return _(subjects.value)
        .orderBy(x => x[sortFiled.value])
        .value();
});

function toggleSort(fildeName){
    sortFiled.value = fildeName
}

function onDeleteClick(subject){
    lessonsStore.deleteSubject(subject.id)
}


function onUpdateClick(id, event){
   // console.log(id)
   // console.log(event)
    lessonsStore.updSubject(id,  event.name, event.level, event.time, event.teacher_fio)
}

onBeforeMount( () => {
    lessonsStore.fetchSubjects();
})


</script>

<template>

    <SubjectRow 
        v-for="s in subjectStored" 
        :name = "s.name" 
        :level = "s.level"
        :time = "s.time"
        :teacher_fio = "s.teacher_fio"
        @delete = "onDeleteClick(s)"
        @update = "onUpdateClick(s.id, $event)"
    />
    <hr> 

  <button id="show-modal" @click="showModal = true">Добавить</button>

  <Teleport to="body">
    <modal :show="showModal" @close="showModal = false">
      <template #header>
        <h3>Добавить предмет</h3>
      </template>
      <template #body>
       
        <h3>Данные по предмету:</h3>
        
        <input type="text" v-model="name" placeholder="Имя"/>
        <input type="text" v-model="level" placeholder="Уровень"/>
        <input type="text" v-model="time" placeholder="Время"/>
        <input type="text" v-model="teacher_fio" placeholder="Преподаватель"/>
        </template>
       
        <template #footer> 
        </template>
    </modal>
  </Teleport>
</template>
<style>

</style>