<script>
export default {
  components: {
    Modal,
  },
  data() {
    return {
      showModal: false,
      newSubject: {
        level: "Начальный",
        name: "",
        time: "10:00",
        teacher: 1
      },
      lessonTime:[
        {name:'10:00', id:1},
        {name:'11:45', id:2}
      ],
      lessonLevel:[
        {name:'Начальный', id:1},
        {name:'Продвинутый', id:2}
      ],
    };
  },
  methods: {
    onFormSumbit() {
      this.showModal = false;
      this.lessonsStore.addSubject(
        this.newSubject.level,
        this.newSubject.name,
        this.newSubject.time,
        this.newSubject.teacher
      );
      this.newSubject = {
        level: "Начальный",
        name: "",
        time: "10:00",
        teacher: 1
      };
    },
  },
};
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
const {teachers} = storeToRefs(lessonsStore);
let sortFiled = ref("name");

const subjectStored = computed(() =>{
    return _(subjects.value)
        .orderBy(x => x[sortFiled.value])
        .value();
});


function onDeleteClick(subject){
    lessonsStore.deleteSubject(subject.id)
}


function onUpdateClick(id, event){
    lessonsStore.updSubject(id,  event.name, event.level, event.time, event.teacher)
}

onBeforeMount( () => {
    lessonsStore.fetchSubjects();
    lessonsStore.fetchTeachers();
})

</script>

<template>
<h2>Предметы</h2>

<button id="show-modal" @click="showModal = true">Добавить</button>

  <Teleport to="body">
    <!-- use the modal component, pass in the prop -->
    <modal
      :show="showModal"
      @submit="onFormSumbit()"
      @close="showModal = false"
    >
      <template #header>
        <h3>Добавить образовательную организацию</h3>
      </template>
      <template #body>
        <input type="text" v-model="newSubject.name" placeholder="Наименование" />
        <div>
          <span>Время: </span>
          <select v-model="newSubject.time" placeholder="Время">
            <option v-for="s in lessonTime" :value="s.name">
              {{ s.name }}
            </option>
          </select>
          </div>
          <div>
          <span>Уровень: </span>
          <select v-model="newSubject.level" placeholder="Уровень">
            <option v-for="s in lessonLevel" :value="s.name">
              {{ s.name }}
            </option>
          </select>
        </div>
        <div>
          <span>Преподаватель: </span>
          <select v-model="newSubject.teacher" placeholder="Преподаватель">
            <option v-for="s in teachers" :value="s.id">
              {{ s.surname }} {{ s.name }} {{ s.patr }}
              
            </option>
          </select>
        </div>
      </template>
      <template #footer> </template>
    </modal>
  </Teleport>
  <hr> 
    <SubjectRow 
        v-for="s in subjectStored" 
        :name = "s.name" 
        :level = "s.level"
        :time = "s.time"
        :teacher_fio = "s.teacher_fio"
        @delete = "onDeleteClick(s)"
        @update = "onUpdateClick(s.id, $event)"
    />
    

  
</template>
<style>

</style>