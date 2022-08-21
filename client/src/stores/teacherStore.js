import { defineStore } from "pinia";

export const useTeacherStore = defineStore({
  id: "teacher",
  state: () => ({
    teacher: {},
    subjects: [],
    subject: {},
    lessons: [],
  }),
  actions: {
    // 21.08.2022
    async fetchTeacherById(id) {
      const response = await fetch(`/api/teachers/${id}`, {
        method: "GET",
        headers: {
          "content-type": "application/json",
        },
      });
      const teacher = await response.json();
      this.teacher = teacher;
    },

    async fetchTeacherSubjects(teacherId) {
      const response = await fetch(`/api/teachers/${teacherId}/subjects`, {
        method: "GET",
        headers: {
          "content-type": "application/json",
        },
      });
      const subjects = (await response.json()).subjects;
      this.subjects = subjects;
    },

    async fetchSubjectById(subjectId) {
      const response = await fetch(`/api/subjects/${subjectId}`, {
        method: "GET",
        headers: {
          "content-type": "application/json",
        },
      });
      const subject = await response.json();
      this.subject = subject;
    },

    async fetchSubjectLessons(subjectId) {
      const response = await fetch(`/api/subjects/${subjectId}/lessons`, {
        method: "GET",
        headers: {
          "content-type": "application/json",
        },
      });
      const lessons = (await response.json()).lessons;
      this.lessons = lessons;
    },
  },
});
