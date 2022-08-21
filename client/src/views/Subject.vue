<template lang="">
  <div class="wrapper">
    <div>
      <span class="subject_title">{{
        `${subject.name} (${subject.level})`
      }}</span>
      <span>
        {{ `Время: ${subject.time}` }}
      </span>
    </div>
  </div>
</template>
<script setup>
import { storeToRefs } from "pinia";
import { useTeacherStore } from "../stores/teacherStore";

const teacherStore = useTeacherStore();
// добавить уроки и удалить из data, когда появится ручка
const { subject } = storeToRefs(teacherStore);
</script>
<script>
export default {
  data() {
    return {
      subjectId: this.$route.params.id,
      lessons: [
        {
          id: 1,
          subjects: 2,
          subjects_name: "Информатика",
          topic: "Программирование на С#",
          homework: "пентаг",
          date: "2019-04-20",
        },
        {
          id: 2,
          subjects: 1,
          subjects_name: "Информатика",
          topic: "Программирование на С#",
          homework: "Взломать пентагон",
          date: "2025-05-20",
        },
        {
          id: 3,
          subjects: 5,
          subjects_name: "Экономика",
          topic: "Кря",
          homework: "вфывфы",
          date: "2025-03-20",
        },
        {
          id: 4,
          subjects: 5,
          subjects_name: "Экономика",
          topic: "asd",
          homework: "asd",
          date: "2022-02-20",
        },
      ],
    };
  },
  methods: {
    navigate(subjectId) {
      this.$router.push({ path: `/subjects/${subjectId}` });
    },
  },
  // запрос на уроки не работает
  beforeMount() {
    console.log(this.subjectId);
    this.teacherStore.fetchSubjectLessons(this.subjectId);
    this.teacherStore.fetchSubjectById(this.subjectId);
  },
};
</script>
<style scoped></style>
