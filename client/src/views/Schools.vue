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
import SchoolRow from '@/components/SchoolRow.vue';
import _ from 'lodash';
import Modal from '../components/modal-window.vue'

const lessonsStore = useLessonsStore(); 
const {schools} = storeToRefs(lessonsStore);
let sortFiled = ref("title");

let title = ref("");

const schoolStored = computed(() =>{
    return _(schools.value)
        .orderBy(x => x[sortFiled.value])
        .value();
});

function toggleSort(fildeName){
    sortFiled.value = fildeName
}

onBeforeMount( () => {
    lessonsStore.fetchSchools();
})

</script>

<template>

    <SchoolRow 
        v-for="s in schoolStored" 
        :title = "s.title" 
        @name-click = "onNameClick(s)"
        @delete = "onDeleteClick(s)"
        @update = "onUpdateClick(s.id, $event)"
    />
    <hr> 

  <button id="show-modal" @click="showModal = true">Добавить</button>

  <Teleport to="body">
    <!-- use the modal component, pass in the prop -->
    <modal :show="showModal" @close="showModal = false">
      <template #header>
        <h3>Добавить образовательную организацию</h3>
      </template>
      <template #body>
       
        <h3>Данные образовательной организации:</h3>
        
        <input type="text" v-model="title" placeholder="Наименование"/>
        
        </template>
       
        <template #footer> 
        </template>
    </modal>
  </Teleport>
</template>