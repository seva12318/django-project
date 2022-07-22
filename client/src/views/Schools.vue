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