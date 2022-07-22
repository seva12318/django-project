<script>
import Modal from '../components/modal-window.vue'

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

<template>
  <button id="show-modal" @click="showModal = true">Добавить</button>

  <Teleport to="body">
    <!-- use the modal component, pass in the prop -->
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