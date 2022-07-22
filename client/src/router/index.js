import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import students from '../views/students.vue'
import teachers from '../views/teachers.vue'
import schools from '../views/schools.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/students',
      name: 'students',
      component: students
    },
    {
      path: '/teachers',
      name: 'teachers',
      component: teachers
    },
    {
      path: '/schools',
      name: 'schools',
      component: schools
    },
  ]
})

export default router
