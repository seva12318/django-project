<script setup>
import { storeToRefs } from "pinia";
import { useLessonsStore } from "../stores/lessons";
import { computed, onBeforeMount, ref } from "vue";

const lessonsStore = useLessonsStore();
const { students, schools } = storeToRefs(lessonsStore);

const studentsStored = computed(() => {
  return _(students.value)
    .orderBy((x) => x[sortFiled.value])
    .value();
});

let sortFiled = ref("name");
let inputText = ref("");

function toggleSort(fildeName) {
  sortFiled.value = fildeName;
}

function onSurnameClick(student) {
  console.log(student.surname);
}

function onNameClick(student) {
  console.log(student.name);
}

function onDeleteClick(student) {
  let permission = window.confirm(
    `Вы действительно хотите удалить студента ${student.surname} ${student.name} ${student.patr}?`
  );
  if (permission) {
    lessonsStore.deleteStudent(student.id);
  }
}

function onUpdateClick(id, { name, surname, patr, schoolId }) {
  // console.log(id)
  // console.log(event)
  lessonsStore.updStudent(id, surname, name, patr, schoolId);
}

onBeforeMount(() => {
  lessonsStore.fetchStudents();
  lessonsStore.fetchSchools();
});
</script>

<script>
import { useLessonsStore } from "../stores/lessons";
import StudentRow from "@/components/StudentRow.vue";
import _ from "lodash";
import Modal from "../components/modal-window.vue";

export default {
  components: {
    Modal,
  },
  data() {
    return {
      showModal: false,
      newStudent: {
        surname: "",
        name: "",
        patr: "",
        school: 1,
      },
      isEdit: false,
    };
  },
  methods: {
    onFormSumbit() {
      this.showModal = false;
      this.lessonsStore.addStudent(
        this.newStudent.surname,
        this.newStudent.name,
        this.newStudent.patr,
        this.newStudent.school
      );
      this.resetStudent();
    },
    onModalOpen() {
      this.newStudent.school = this.schools[0].id;
      this.showModal = true;
    },
    onModalClose() {
      this.showModal = false;
      this.resetStudent();
      console.log(this.schools);
    },
    resetStudent() {
      this.newStudent = {
        surname: "",
        name: "",
        patr: "",
        school: 1,
      };
    },
  },
};
</script>

<template>
  <h2>Обучающиеся</h2>
  <button id="show-modal" @click="onModalOpen()">Добавить</button>

  <Teleport to="body">
    <!-- use the modal component, pass in the prop -->
    <modal :show="showModal" @submit="onFormSumbit()" @close="onModalClose()">
      <template #header>
        <h3>Добавить обучающегося</h3>
      </template>
      <template #body>
        <input type="text" v-model="newStudent.surname" placeholder="Фамилия" />
        <input type="text" v-model="newStudent.name" placeholder="Имя" />
        <input type="text" v-model="newStudent.patr" placeholder="Отчество" />
        <div>
          <span>Школа: </span>
          <select v-model="newStudent.school" placeholder="Школа">
            <option v-for="s in schools" :value="s.id">
              {{ s.title }}
            </option>
          </select>
        </div>
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

  <StudentRow
    v-for="s in studentsStored"
    :name="s.name"
    :surname="s.surname"
    :patr="s.patr"
    :school="{ title: s.school_title, id: s.school }"
    :schools="schools"
    @surname-click="onSurnameClick(s)"
    @name-click="onNameClick(s)"
    @delete="onDeleteClick(s)"
    @update="onUpdateClick(s.id, $event)"
    :isEdit="isEdit"
  />

  <!-- <form action="" @submit.prevent.stop="onFormSumbit">
        <input type="text" v-model="surname" placeholder="Фамилия"/>
        <input type="text" v-model="name" placeholder="Имя"/>
        <input type="text" v-model="patr" placeholder="Отчество"/>
        <input type="text" v-model="school" placeholder="Школа"/>
        <button>Добавить</button>
    </form> -->
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
</style>
