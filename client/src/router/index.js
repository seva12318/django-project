import {createRouter, createWebHistory} from "vue-router";
import students from "../views/Students.vue";
import teachers from "../views/Teachers.vue";
import schools from "../views/Schools.vue";
import subjects from "../views/Subjects.vue";
import ReportBySchool from "../views/ReportBySchool.vue";
import choices from "../views/Choices.vue";
import TeacherHome from "../views/Teacher/TeacherHome.vue";
import Subject from "../views/Teacher/Subject.vue";
import Journal from "../views/Teacher/Journal.vue";
import LoginView from "../views/LoginView.vue";
import ReportBySubject from "../views/ReportBySubject.vue";
import ReportOfSubjects from "../views/ReportOfSubjects.vue";
import {useAuthStore} from "@/stores/authStore";
import {storeToRefs} from "pinia";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "home",
            component: TeacherHome,
            meta: {requiresAuth: true}
        },
        {
            path: "/subjects/:id",
            name: "subject",
            component: Subject,
            meta: {requiresAuth: true}
        },
        {
            path: "/subjects/:subjectId/lessons/:lessonId/journal",
            name: "journal",
            component: Journal,
            meta: {requiresAuth: true}
        },
        {
            path: "/login",
            name: "login",
            component: LoginView,
            meta: {requiresAuth: false}
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

    ],
});

router.beforeEach((to, from) => {
    // instead of having to check every route record with
    // to.matched.some(record => record.meta.requiresAuth)
    const store = useAuthStore();
    const {
        isAuthenticated
    } = storeToRefs(store)

    if (to.meta.requiresAuth && !isAuthenticated.value) {
        // this route requires auth, check if logged in
        // if not, redirect to login page.
        return {
            path: '/login',
            // save the location we were at to come back later
            query: {redirect: to.fullPath},
        };
    }
})

export default router;
