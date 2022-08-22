<template lang="">
  <Teleport to="body">
    <!-- use the modal component, pass in the prop -->
    <modal
      :show="showModal"
      @submit="onSubmit({ topic, date, homework })"
      @close="onClose()"
    >
      <template #header>
        <h3>Добавить урок</h3>
      </template>
      <template #body>
        <div class="block">
          <span>Тема: </span>
          <input type="text" placeholder="Тема урока" v-model="topic" />
        </div>
        <div class="block">
          <span>Дата: </span>
          <input type="date" placeholder="Дата урока" v-model="date" />
        </div>

        <span>Домашнее задание: </span>
        <textarea
          placeholder="Текст домашнего задания"
          rows="4"
          v-model="homework"
        />
      </template>

      <template #footer> </template>
    </modal>
  </Teleport>
</template>
<script setup>
defineProps({
  showModal: Boolean,
  onClose: Function,
  onSubmit: Function,
});
</script>
<script>
import Modal from "../../../components/modal-window.vue";
export default {
  data() {
    return {
      topic: "",
      date: new Date(Date.now()).toISOString().split("T")[0],
      homework: "",
    };
  },
};
</script>
<style scoped>
.block {
  width: 100%;
  display: flex;
  gap: 10px;
  align-items: center;
}
</style>
