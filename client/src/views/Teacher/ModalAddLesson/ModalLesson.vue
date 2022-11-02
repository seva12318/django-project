<template>
  <Teleport to="body">
    <!-- use the modal component, pass in the prop -->
    <modal :show="showModal" @submit="submit()" @close="closeModal()">
      <template #header>
        <h3>
          {{
            isEdit ? `Редактирование урока №${lesson.number}` : "Добавить урок"
          }}
        </h3>
      </template>
      <template #body>
        <div class="block">
          <span>Тема: </span>
          <input type="text" placeholder="Тема урока" v-model="lesson.topic" />
        </div>
        <div class="block">
          <span>Дата: </span>
          <input type="date" placeholder="Дата урока" v-model="lesson.date" />
        </div>
        <span>Домашнее задание: </span>
        <textarea
          placeholder="Текст домашнего задания"
          rows="4"
          v-model="lesson.homework"
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
  isEdit: Boolean,
  lesson: Object,
});
</script>
<script>
import Modal from "../../../components/modal-window.vue";
export default {
  methods: {
    submit() {
      this.onSubmit(this.lesson);
    },
    closeModal() {
      this.onClose();
    },
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
