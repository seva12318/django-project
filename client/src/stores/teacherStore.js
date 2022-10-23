import { defineStore } from "pinia";

import {ref} from "vue";
import axios from "axios";

export const useTeacherStore = defineStore({
  id: "teacher",
  state: () => ({
    teacher: {},
    subjects: [],
    subject: null,
    lessons: null,
    subjectStudents: null,
    lesson: null,
    marks: null,
    isLoading: false,
    report: [],
    teacherId: null
  }),
  actions: {
    // 21.08.2022
    async fetchTeacherById(id) {
      try{
      const response = await fetch(`/api/teachers/${id}/`, {
        method: "GET",
        headers: {
          "content-type": "application/json",
        },
      });
      //console.log(response);
      const teacher = await response.json();
      this.teacher = teacher;
    }
    catch(error){
      console.log(error)
    }
    },

    async fetchTeacherSubjects(teacherId) {
      try{
      const response = await fetch(`/api/teachers/${teacherId}/subjects/`, {
        method: "GET",
        headers: {
          "content-type": "application/json",
          // "csrftoken": csrftoken,
        },
      });
      const subjects = (await response.json()).subjects;
      this.subjects = subjects;
      }
      catch(error){
        console.log(error)
      }
    },

    async fetchSubjectById(subjectId) {
      const response = await fetch(`/api/subjects/${subjectId}/`, {
        method: "GET",
        headers: {
          "content-type": "application/json",
        },
      });
      const subject = await response.json();
      this.subject = subject;
    },

    async fetchSubjectLessons(subjectId) {
      const response = await fetch(`/api/subjects/${subjectId}/lessons/`, {
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

      // await fetch("/api/lessons/", {
      //   method: "POST",
      //   headers: {
      //     "content-type": "application/json",
      //     
      //   },
      //   body: JSON.stringify({ topic, date, homework, subjects: subjectId}),
      // });
      
      //работает не трогать
      let response = await axios.post("/api/lessons/", {
        
        topic:topic,
        date:date,
        homework:homework,
        subjects: subjectId,
        
    });
    
      this.fetchSubjectLessons(subjectId).finally(
        () => (this.isLoading = false)
      );
    },

    // 23.08.2022
    async updateLesson(lessonId, updatedLesson) {
      this.isLoading = true;

      // await fetch(`/api/lessons/${lessonId}/`, {
      //   method: "PATCH",
      //   headers: {
      //     "content-type": "application/json",
      //   },
      //   body: JSON.stringify(updatedLesson),
      // });

      //а почему???????
      let response = await axios.patch(`/api/lessons/${lessonId}/`,{
        topic:updatedLesson.topic,
        date:updatedLesson.date,
        homework:updatedLesson.homework,
        subjects: updatedLesson.subjectId,
      });

      this.fetchSubjectLessons(updatedLesson.subjects).finally(
        () => (this.isLoading = false)
      );
    },

    // 29.08.2022
    async fetchStudentsBySubjectId(subjectId) {
      this.isLoading = true;

      const response = await fetch(`/api/subjects/${subjectId}/students/`, {
        method: "GET",
        headers: {
          "content-type": "application/json",
        },
      });
      this.subjectStudents = (await response.json())["sub-journal"];

      this.isLoading = false;
    },

    async fetchLessonById(lessonId) {
      this.isLoading = true;

      const response = await fetch(`/api/lessons/${lessonId}/`, {
        method: "GET",
        headers: {
          "content-type": "application/json",
        },
      });
      this.lesson = await response.json();

      this.isLoading = false;
    },

    // 30.08.2022
    async fetchMarksByLessonId(lessonId) {
      this.isLoading = true;

      const response = await fetch(`/api/lessons/${lessonId}/journal/`, {
        method: "GET",
        headers: {
          "content-type": "application/json",
        },
      });
      this.marks = (await response.json()).journal;

      this.isLoading = false;
    },

    async addMark({ studentId, mark, lessonId }) {
      //this.isLoading = true;
      let response = await axios.post("/api/journals/",{
        students: studentId,
          lessons: lessonId,
          mark: String(mark),
      })
      // await fetch("/api/journals/", {
      //   method: "POST",
      //   headers: {
      //     "content-type": "application/json",
      //   },
      //   body: JSON.stringify({
      //     students: studentId,
      //     lessons: lessonId,
      //     mark: String(mark),
      //   }),
      // });
      //this.isLoading = false;
    },

    async updateMark({ markId, mark }) {

      let response = await axios.patch(`/api/journals/${markId}/`,{
        mark: mark,
      });

      // this.fetchSubjectLessons(updatedLesson.subjects).finally(
      //   () => (this.isLoading = false)


      // await fetch(`/api/journals/${markId}/`, {
      //   method: "PATCH",
      //   headers: {
      //     "content-type": "application/json",
      //   },
      //   body: JSON.stringify({
      //     mark,
      //   }),
      // });
    },

    // 02.09.2022
    async fetchReportBySubjectId(subjectId) {
      this.isLoading = true;

      const response = await fetch(`/api/journals/${subjectId}/subject/`, {
        method: "GET",
        headers: {
          "content-type": "application/json",
        },
      });
      this.report = (await response.json())["sub-journal"];

      this.isLoading = false;
    },
    async fetchTeacherId() {
      this.isLoading = true;
      
      let r = await axios.get('/api/teachers/user/')
      //console.log(r.data.teacher[0].user);
      this.teacherId  = r.data.teacher[0].id;
     //console.log(this.teacherId);
      this.isLoading = false;
     return this.teacherId;
    },
  },
  
});
