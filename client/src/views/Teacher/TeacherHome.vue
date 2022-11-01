<template>
  <div class="teacher_wrapper">
    <div class="info">
      <div class="greeting">
        {{ `Здравствуйте, ${teacher.name} ${teacher.surname}!` }}
      </div>
      <div class="description">
        Ваши предметы отображены ниже. Чтобы взаимодействовать с ними, кликните
        на соответствующую карточку.
      </div>
    </div>
    <div class="subjects">
      <div
        class="subject"
        v-for="subject in subjects"
        @click="navigateToSubject(subject.id)"
      >
        <span class="subject_title">{{
          `${subject.name} (${subject.level})`
        }}</span>
        <span>
          {{ `Время: ${subject.time}` }}
        </span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { storeToRefs } from "pinia";
import { onBeforeMount } from "vue";
import { useTeacherStore } from "../../stores/teacherStore";

const teacherStore = useTeacherStore();
const { teacher, subjects } = storeToRefs(teacherStore);

// mock

onBeforeMount(() => {
  //авторизация
  teacherStore.fetchTeacherId().then(
    function (result, reject) {
      console.log(result);
      // что-то делаем с результатом операции

      teacherStore.fetchTeacherById(result);
      teacherStore.fetchTeacherSubjects(result);
    },
    function (err) {
      // обрабатываем ошибку
      console.error(err.message);
    }
  );
});
</script>
<script>
export default {
  data() {
    return {};
  },
  methods: {
    navigateToSubject(subjectId) {
      this.$router.push({ path: `/subjects/${subjectId}` });
    },
  },
};
</script>
<style scoped>
.teacher_wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 90%;
  gap: 50px;
}
.info {
  text-align: center;

  display: flex;
  flex-direction: column;
  gap: 10px;
}
.greeting {
  font-size: 24px;
}
.description {
  max-width: 40vw;
  font-size: 16px;
}
.subjects {
  display: flex;
  justify-content: space-between;
  width: 60%;
  gap: 36px;
}

@media screen and (max-width: 1440px) {
  .subjects {
    display: flex;
    flex-direction: column;
    gap: 36px;
  }
}

.subject {
  padding: 40px 60px;
  border-radius: 8px;
  background: #42b983;

  cursor: pointer;

  display: flex;
  flex-direction: column;
  gap: 10px;
}

.subject:hover {
  opacity: 0.9;
  transform: scale(1.1);
}

.subject_title {
  font-size: 18px;
  font-weight: 500;
}
</style>
