<script setup>
import { RouterLink, RouterView } from "vue-router";
import Popup from "./components/Popup/Popup.vue";
</script>

<script>
export default {
  data() {
    return {
      showPopup: false,
    };
  },
  methods: {
    openPopup() {
      this.showPopup = true;
    },
    closePopup() {
      this.showPopup = false;
    },
    changeVisiblePopup() {
      this.showPopup = !this.showPopup;
    },
  },
};
</script>

<template>
  <header>
    <nav class="nav">
      <RouterLink to="/">Домашняя</RouterLink>
      <RouterLink to="/teachers">Преподаватели</RouterLink>
      <RouterLink to="/subjects">Предметы</RouterLink>
      <RouterLink to="/students">Обучающиеся</RouterLink>
      <RouterLink to="/schools">Образовательные организации</RouterLink>
      <RouterLink to="/choices">Выбор студентов</RouterLink>
      <Popup :show="showPopup" :onClose="closePopup">
        <template #anchor>
          <span @mouseenter="openPopup()" class="popup_opener">Отчёты</span>
        </template>
        <template #body>
          <RouterLink to="/reports/schools" class="popup_item"
            >Отчёт по школам</RouterLink
          >
          <RouterLink to="/reports/teachers/1/subjects" class="popup_item"
            >Отчёты по предметам преподавателя</RouterLink
          >
          <RouterLink to="/reports/subjects" class="popup_item"
            >Отчёты по предметам (всем)</RouterLink
          >
        </template>
      </Popup>
      <RouterLink to="/about">О приложении</RouterLink>
      <RouterLink to="/about">Выход</RouterLink>
      <RouterLink to="/teacherHome">Дом препода</RouterLink>
    </nav>
  </header>

  <RouterView />
</template>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  font-family: Roboto;
}

#app {
  /* flex: 1;
  display: flex;
  flex-direction: column; */
  height: 100vh;
  padding: 0 50px;
}

header {
  padding-top: 20px;
  padding-left: 20px;
  padding-bottom: 20px;
}

.nav {
  flex: 1;
  display: flex;
  gap: 20px;
}

.wrapper {
  flex: 9;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

textarea {
  resize: none;
  width: 100%;
  padding: 5px 10px;
}

input {
  width: 100%;
  padding: 5px 10px;
}

.popup_opener {
  cursor: pointer;
  user-select: none;
}

.popup_item {
  padding: 10px 20px;
}

.popup_item:hover {
  opacity: 0.5;
  background: #fff;
}
</style>
