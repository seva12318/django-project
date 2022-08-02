<script>
export default {
  components: {
    Modal,
  },
  data() {
    return {
      showModal: false,
      newSchool: {
        title: "",
      },
    };
  },
  methods: {
    onFormSumbit() {
      this.showModal = false;
      this.lessonsStore.addSchool(
        this.newSchool.title
      );
      this.newTeacher = {
        title: "",
      };
    },
  },
};
</script>
<script setup>
import { storeToRefs } from 'pinia';
import {computed, onBeforeMount, ref} from 'vue';
import {useLessonsStore} from '../stores/lessons';
import SchoolRow from '@/components/SchoolRow.vue';
import _ from 'lodash';
import Modal from '../components/modal-window.vue'

const lessonsStore = useLessonsStore(); 
const {schools} = storeToRefs(lessonsStore);
let sortFiled = ref("school_title");

const schoolStored = computed(() =>{
    return _(schools.value)
        .orderBy(x => x[sortFiled.value])
        .value();
});

function onDeleteClick(school){
    lessonsStore.deleteSchool(school.id)
}

function onUpdateClick(id, event){
   // console.log(id)
    console.log(event)
    lessonsStore.updSchool(id,  event.school_title)
}

onBeforeMount( () => {
    lessonsStore.fetchSchools();
})

</script>

<template>
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
        <input type="text" v-model="newSchool.title" placeholder="Образовательная организация" />
      </template>
      <template #footer> </template>
    </modal>
  </Teleport>

<hr />
    <SchoolRow 
        v-for="s in schoolStored" 
        :school_title = "s.title" 
        @name-click = "onNameClick(s)"
        @delete = "onDeleteClick(s)"
        @update = "onUpdateClick(s.id, $event)"
    />
  
</template>