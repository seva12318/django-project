<script>
import { storeToRefs } from 'pinia';
import {computed, onBeforeMount, ref} from 'vue';
import Modal from '../components/modal-window.vue'
// import {useLessonsStore} from '../stores/lessons';
// const lessonsStore = useLessonsStore(); 
// const {students} = storeToRefs(lessonsStore);


// let surname = ref("");
// let name = ref("");
// let patr = ref("");
// let school = ref("");


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

function onFormSumbit(){
    lessonsStore.addStudent(surname.value, name.value, patr.value, school.value)
}
</script>

<template>
  <button id="show-modal" @click="showModal = true">Добавить</button>

  <Teleport to="body">
    <!-- use the modal component, pass in the prop -->
    <modal :show="showModal" @close="showModal = false">
      <template #header>
        <h3>Добавить ученика</h3>
      </template>
      <template #body>
        <form action="" @submit.prevent.stop="onFormSumbit">
        <h3>Данные ученика:</h3>
        
        <input type="text" v-model="surname" placeholder="Фамилия"/>
        <input type="text" v-model="name" placeholder="Имя"/>
        <input type="text" v-model="patr" placeholder="Отчество"/>
        <input type="text" v-model="school" placeholder="Школа"/>
        <button>Добавить</button>
    </form> 
      </template>
        <template #footer>
        ~
       
      </template>
    </modal>
  </Teleport>
</template>