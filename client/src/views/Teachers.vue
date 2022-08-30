<script>
import TeacherRow from "@/components/TeacherRow.vue";
import _ from "lodash";
import Modal from "../components/modal-window.vue";
export default {
  components: {
    Modal,
  },
  data() {
    return {
      showModal: false,
      newTeacher: {
        surname: "",
        name: "",
        patr: "",
      },
      isEdit: false,
    };
  },
  methods: {
    onFormSumbit() {
      this.showModal = false;
      this.lessonsStore.addTeacher(
        this.newTeacher.surname,
        this.newTeacher.name,
        this.newTeacher.patr
      );
      this.resetTeachers();
    },
    onModalClose() {
      this.showModal = false;
      this.resetTeachers();
    },
    resetTeachers() {
      this.newTeacher = {
        surname: "",
        name: "",
        patr: "",
      };
    },
  },
};
</script>
<script setup>
import { storeToRefs } from "pinia";
import { computed, onBeforeMount, ref } from "vue";
import { useLessonsStore } from "../stores/lessons";

const lessonsStore = useLessonsStore();
const { teachers } = storeToRefs(lessonsStore);
let sortFiled = ref("name");

const teacherStored = computed(() => {
  return _(teachers.value)
    .orderBy((x) => x[sortFiled.value])
    .value();
});

function toggleSort(fildeName) {
  sortFiled.value = fildeName;
}

function onDeleteClick(teacher) {
  let permission = window.confirm(
    `Вы действительно хотите удалить учителя ${teacher.surname} ${teacher.name} ${teacher.patr}?`
  );
  if (permission) {
    lessonsStore.deleteTeacher(teacher.id);
  }
}

function onUpdateClick(id, { name, surname, patr }) {
  lessonsStore.updTeacher(id, name, surname, patr);
}

onBeforeMount(() => {
  lessonsStore.fetchTeachers();
});
</script>

<template>
  <h2>Преподаватели</h2>
  <button id="show-modal" @click="showModal = true">Добавить</button>

  <Teleport to="body">
    <!-- use the modal component, pass in the prop -->
    <modal :show="showModal" @submit="onFormSumbit()" @close="onModalClose()">
      <template #header>
        <h3>Добавить преподавателя</h3>
      </template>
      <template #body>
        <input type="text" v-model="newTeacher.surname" placeholder="Фамилия" />
        <input type="text" v-model="newTeacher.name" placeholder="Имя" />
        <input type="text" v-model="newTeacher.patr" placeholder="Отчество" />
      </template>

      <template #footer> </template>
    </modal>
  </Teleport>

  <hr />

  <div class="container">
    <button @click="toggleSort('name')">По имени</button>
    <button @click="toggleSort('surname')">По фамилии</button>

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
  <TeacherRow
    v-for="s in teacherStored"
    :name="s.name"
    :surname="s.surname"
    :patr="s.patr"
    @surname-click="onSurnameClick(s)"
    @name-click="onNameClick(s)"
    @delete="onDeleteClick(s)"
    @update="onUpdateClick(s.id, $event)"
    :isEdit="isEdit"
  />
  <hr />
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
  background-color: #42b983;
  border-radius: 50%;

  transform: translateX(0);
  transition: all 0.3s cubic-bezier(0.2, 0.85, 0.32, 1.2);
}

.toggle-button:checked::after {
  transform: translateX(calc(100% + 3px));
  background-color: #fff;
}
.toggle-button:checked {
  background-color: #42b983;
}

/* button {
  width: 50px;
} */
</style>
