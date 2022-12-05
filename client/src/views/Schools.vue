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
      isEdit: false,
    };
  },
  methods: {
    onFormSumbit() {
      this.showModal = false;
      this.lessonsStore.addSchool(
        this.newSchool.title
      );
      this.resetSchool();
    },
    onModalClose() {
      this.showModal = false;
      this.resetSchool();
    },
    resetSchool() {
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
<h2>Образовательные организации</h2>
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
<div class="container">
   
    <div class="toggle">
      <input
        type="checkbox"
        id="toggle-button"
        class="toggle-button"
        v-model="isEdit"
      />
      <label for="toggle-button" class="text">Режим редактирования</label>
    </div>
  </div>

    <SchoolRow 
        v-for="s in schoolStored" 
        :school_title = "s.title" 
        @name-click = "onNameClick(s)"
        @delete = "onDeleteClick(s)"
        @update = "onUpdateClick(s.id, $event)"
        :isEdit="isEdit"
    />
  
</template>

<style scoped>
.container {
  display: flex;
  gap: 16px;
  padding: 8px 0;
}
.toggle {
  display: flex;
  align-items: center;
  gap: 8px;
}
.toggle-button {
  position: relative;
  display: inline-block;
  width: 50px;
  height: 25px;
  margin: 0;
  vertical-align: top;
  background: #ffffff;
  border: 1px solid #bbc1e1;
  border-radius: 30px;
  outline: none;
  cursor: pointer;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  transition: all 0.3s cubic-bezier(0.2, 0.85, 0.32, 1.2);
}

.toggle-button::after {
  content: "";

  display: inline-block;
  position: absolute;
  left: 3px;
  top: 1.5px;

  width: 20px;
  height: 20px;
  background-color: rgb(5, 33, 84);
  border-radius: 50%;

  transform: translateX(0);
  transition: all 0.3s cubic-bezier(0.2, 0.85, 0.32, 1.2);
}

.toggle-button:checked::after {
  transform: translateX(calc(100% + 3px));
  background-color: #fff;
}
.toggle-button:checked {
  background-color: #4242b9;
}
</style>
