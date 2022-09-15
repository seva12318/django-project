import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import students from "../views/students.vue";
import teachers from "../views/teachers.vue";
import schools from "../views/schools.vue";
import subjects from "../views/subjects.vue";
import ReportBySchool from "../views/ReportBySchool.vue";
import choices from "../views/Choices.vue";
// 21.08.2022
import TeacherHome from "../views/Teacher/TeacherHome.vue";
import Subject from "../views/Teacher/Subject.vue";
// 29.08.2022
import Journal from "../views/Teacher/Journal.vue";
// 01.09.2022
import ReportBySubject from "../views/ReportBySubject.vue";
import ReportOfSubjects from "../views/ReportOfSubjects.vue";

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
      path: "/reports/schools",
      name: "report by school",
      component: ReportBySchool,
    },
    {
      path: "/reports/teachers/:id/subjects",
      name: "report by teacher subject",
      component: ReportBySubject,
    },
    {
      path: "/reports/subjects",
      name: "report by subjects",
      component: ReportOfSubjects,
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
    {
      path: "/subjects/:subjectId/lessons/:lessonId/journal",
      name: "journal",
      component: Journal,
    },
  ],
});

export default router;
