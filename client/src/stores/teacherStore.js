import { defineStore } from "pinia";

export const useTeacherStore = defineStore({
  id: "teacher",
  state: () => ({
    teacher: {},
    subjects: [],
    subject: null,
    lessons: null,
    isLoading: false,
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
      const lessons = (await response.json())["sub-lessons"];
      this.lessons = lessons;
    },

    // 22.08.2022
    async addLesson({ topic, date, subjectId, homework }) {
      this.isLoading = true;

      await fetch("/api/lessons/", {
        method: "POST",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify({ topic, date, homework, subjects: subjectId }),
      });

      this.fetchSubjectLessons(subjectId).finally(
        () => (this.isLoading = false)
      );
    },

    // 23.08.2022
    async updateLesson(lessonId, updatedLesson) {
      this.isLoading = true;

      await fetch(`/api/lessons/${lessonId}/`, {
        method: "PATCH",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify(updatedLesson),
      });

      console.log(updatedLesson);

      this.fetchSubjectLessons(updatedLesson.subjects).finally(
        () => (this.isLoading = false)
      );
    },
  },
});
