import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import students from "../views/students.vue";
import teachers from "../views/teachers.vue";
import schools from "../views/schools.vue";
import subjects from "../views/subjects.vue";
import reports from "../views/reports.vue";
import choices from "../views/Choices.vue";
// 21.08.2022
import TeacherHome from "../views/TeacherHome.vue";
import Subject from "../views/Subject.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/students",
      name: "students",
      component: students,
    },
    {
      path: "/teachers",
      name: "teachers",
      component: teachers,
    },
    {
      path: "/schools",
      name: "schools",
      component: schools,
    },
    {
      path: "/subjects",
      name: "subjects",
      component: subjects,
    },
    {
      path: "/reports",
      name: "reports",
      component: reports,
    },
    {
      path: "/choices",
      name: "choices",
      component: choices,
    },
    {
      path: "/teacherHome",
      name: "teacherHome",
      component: TeacherHome,
    },
    {
      path: "/subjects/:id",
      name: "subject",
      component: Subject,
    },
  ],
});

export default router;
