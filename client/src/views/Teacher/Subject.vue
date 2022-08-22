<template lang="">
  <div class="wrapper">
    <Loader v-if="!Boolean(lessons) || !Boolean(subject) || isLoading" />
    <div class="subject_wrapper" v-else>
      <div class="subject_name">
        <span class="subject_title">{{
          `${subject.name} (${subject.level})`
        }}</span>
        <span>
          {{ `Время: ${subject.time}` }}
        </span>
      </div>
      <div class="lessons_wrapper" v-if="lessons.length === 0">
        <div class="subject_no_lessons">
          На данный момент у вас нет уроков по этому предмету
        </div>
        <div class="add_lesson" @click="onModalOpen()">+ Добавить урок</div>
      </div>
      <div class="lessons_wrapper" v-else>
        <div class="add_lesson" @click="onModalOpen()">+ Добавить урок</div>
        <div class="subject_lessons">
          <div class="subject_lesson" v-for="(lesson, index) in lessons">
            <span class="title">{{ `Урок №${index + 1}` }}</span>
            <hr />
            <div>
              <span class="title">Тема: </span>
              <span>{{ lesson.topic }}</span>
            </div>
            <div>
              <span class="title">Дата: </span>
              <span>{{ formatDate(lesson.date) }}</span>
            </div>
            <hr />
            <span class="title">Домашнее задание:</span>
            <span>{{ `${lesson.homework}` }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <ModalAddLesson
    :showModal="showModal"
    :onClose="onModalClose"
    :onSubmit="onAddLesson"
  />
</template>
<script setup>
import { storeToRefs } from "pinia";
import { useTeacherStore } from "../../stores/teacherStore";
import Loader from "../../components/Loader/Loader.vue";
import ModalAddLesson from "./ModalAddLesson/ModalAddLesson.vue";

const teacherStore = useTeacherStore();
// добавить уроки и удалить из data, когда появится ручка
const { subject, lessons, isLoading } = storeToRefs(teacherStore);
</script>
<script>
export default {
  data() {
    return {
      subjectId: this.$route.params.id,
      showModal: false,
    };
  },
  methods: {
    navigate(subjectId) {
      this.$router.push({ path: `/subjects/${subjectId}` });
    },
    onModalOpen() {
      this.showModal = true;
    },
    onModalClose() {
      this.showModal = false;
    },
    formatDate(date) {
      // format from yyyy-mm-dd to dd.mm.yyyy
      return date.split("-").reverse().join(".");
    },
    onAddLesson(lesson) {
      this.teacherStore.addLesson({
        ...lesson,
        subjectId: Number(this.subjectId),
        date: this.formatDate(lesson.date),
      });
      this.onModalClose();
    },
  },
  // запрос на уроки не работает
  beforeMount() {
    this.teacherStore.fetchSubjectLessons(this.subjectId);
    this.teacherStore.fetchSubjectById(this.subjectId);
  },
};
</script>
<style scoped>
.subject_wrapper {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  flex: 1;
  padding-top: 50px;
}
.subject_name {
  display: flex;
  flex-direction: column;
  font-size: 22px;
  font-weight: 600;
  text-align: center;
}
.lessons_wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
  gap: 20px;
}
.add_lesson {
  padding: 10px 20px;
  border-radius: 8px;
  background: #42b983;

  cursor: pointer;

  display: flex;
  flex-direction: column;
  gap: 10px;
}
.add_lesson:hover {
  opacity: 0.9;
  transform: scale(1.1);
}
.subject_lessons {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 10px;
  flex-grow: 1;
}
.subject_lesson {
  display: flex;
  flex-direction: column;
  padding: 20px 40px;
  border-radius: 6px;
  border: 1px solid gray;
  flex-grow: 1;
  max-width: 400px;
}
.subject_lesson hr {
  margin-top: 10px;
  margin-bottom: 10px;
}
.subject_lesson .title {
  font-size: 18px;
  font-weight: 500;
}
.subject_no_lessons {
  margin-top: 200px;
  text-align: center;
}
</style>
