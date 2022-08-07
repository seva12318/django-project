<script setup>
import { storeToRefs } from "pinia";
import { computed, onBeforeMount, ref } from "vue";
import { useLessonsStore } from "../stores/lessons";

const lessonsStore = useLessonsStore();
const { choices, students, subjects } = storeToRefs(lessonsStore);

let sortFiled = ref("name");

const choicesSorted = computed(() => {
  return _(choices.value)
    .orderBy((x) => x[sortFiled.value])
    .value();
});

const firstSubjects = computed(() => {
  const res = subjects.value.filter((subj) => subj.time === "10:00");
  return res;
});
const secondSubjects = computed(() => {
  const res = subjects.value.filter((subj) => subj.time === "11:45");
  return res;
});

function toggleSort(fildeName) {
  sortFiled.value = fildeName;
}

function onDeleteClick(choice) {
  let permission = window.confirm(
    `Вы действительно хотите удалить выбранные предметы студента ${choice.students_name}?`
  );
  if (permission) {
    lessonsStore.deleteChoice(choice.id); // изменить
  }
}

onBeforeMount(() => {
  lessonsStore.fetchChoices();
  lessonsStore.fetchStudents();
  lessonsStore.fetchSubjects();
});
</script>

<script>
import ChoicesRow from "@/components/ChoicesRow.vue";
import _ from "lodash";
import Modal from "../components/modal-window.vue";
export default {
  components: {
    Modal,
  },
  data() {
    return {
      showModal: false,
      newChoice: {
        studentId: 1,
        year: new Date().getFullYear(),
        semester: 1,
        firstSubjectId: 1,
        secondSubjectId: 2,
        classTitle: "",
      },
      isEdit: false,
    };
  },
  methods: {
    onFormSumbit() {
      this.showModal = false;
      // изменить
      this.lessonsStore.addChoice(
        this.newChoice.studentId,
        this.newChoice.year,
        this.newChoice.semester,
        this.newChoice.firstSubjectId,
        this.newChoice.secondSubjectId,
        this.newChoice.classTitle
      );
      this.resetChoice();
    },
    onUpdateClick(
      id,
      {
        studentName,
        year,
        semester,
        firstSubjectId,
        secondSubjectId,
        classTitle,
      }
    ) {
      this.lessonsStore.updateChoice(
        id,
        studentName,
        year,
        semester,
        firstSubjectId,
        secondSubjectId,
        classTitle
      );
    },
    onModalOpen() {
      this.newChoice.studentId = this.students[0].id;
      this.newChoice.firstSubjectId = this.firstSubjects[0].id;
      this.newChoice.secondSubjectId = this.secondSubjects[0].id;
      this.showModal = true;
    },
    onModalClose() {
      console.log(this.firstSubjects.filter((el) => el.id === 1));
      console.log(this.secondSubjects.filter((el) => el.id === 1));
      this.showModal = false;
      this.resetChoice();
    },
    resetChoice() {
      this.newChoice = {
        studentId: this.students[0].id,
        year: new Date().getFullYear(),
        semester: 1,
        firstSubId: this.firstSubjects[0].id,
        secondSubId: this.secondSubjects[0].id,
        classTitle: "",
      };
    },
  },
};
</script>

<template>
  <h2>Выборы</h2>
  <button id="show-modal" @click="onModalOpen()">Добавить</button>

  <Teleport to="body">
    <!-- use the modal component, pass in the prop -->
    <modal :show="showModal" @submit="onFormSumbit()" @close="onModalClose()">
      <template #header>
        <h3>Добавить выбор</h3>
      </template>
      <template #body>
        <div>
          <span>Студент: </span>
          <select v-model="newChoice.studentId" placeholder="Студент">
            <option v-for="s in students" :value="s.id">
              {{ `${s.surname} ${s.name} ${s.patr} ${s.school_title}` }}
            </option>
          </select>
        </div>
        <label>Год: <input type="number" v-model="newChoice.year" /></label>
        <label
          >Семестр: <input type="number" v-model="newChoice.semester"
        /></label>
        <label
          >Класс: <input type="text" v-model="newChoice.classTitle"
        /></label>
        <div>
          <span>Предмет 1: </span>
          <select v-model="newChoice.firstSubjectId" placeholder="Предмет 1">
            <option v-for="s in firstSubjects" :value="s.id">
              {{ `${s.name} ${s.level}` }}
            </option>
          </select>
        </div>
        <div>
          <span>Предмет 2: </span>
          <select v-model="newChoice.secondSubjectId" placeholder="Предмет 2">
            <option v-for="s in secondSubjects" :value="s.id">
              {{ `${s.name} ${s.level}` }}
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
  <ChoicesRow
    v-for="choice in choicesSorted"
    :studentName="choice.students_name"
    :year="choice.year"
    :semester="choice.semester"
    :firstSubject="{
      id: choice.sub_first,
      name: `${choice.sub_first_name} ${choice.sub_first}`,
    }"
    :firstSubjects="firstSubjects"
    :secondSubject="{
      id: choice.sub_second,
      name: `${choice.sub_second_name} ${choice.sub_second}`,
    }"
    :secondSubjects="secondSubjects"
    :classTitle="choice.num_class"
    @delete="onDeleteClick(choice)"
    @update="onUpdateClick(choice.id, $event)"
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
</style>
