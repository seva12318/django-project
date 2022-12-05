import { defineStore } from "pinia";

export const useLessonsStore = defineStore({
  id: "lessons",
  state: () => ({
    students: [],
    teachers: [],
    schools: [],
    subjects: [],
    lessons: null,
    reports: [],
    choices: [],
  }),
  actions: {
    async fetchStudents() {
      let r = await fetch("/api/students/");
      this.students = await r.json();
    },
    async deleteStudent(studentId) {
      let r = await fetch(`/api/students/${studentId}/`, {
        method: "DELETE",
      });
      await this.fetchStudents();
    },
    async addStudent(surname, name, patr, school) {
      let r = await fetch(`/api/students/`, {
        method: "POST",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify({
          surname,
          name,
          patr,
          school,
        }),
      });
      await this.fetchStudents();
    },
    async updStudent(studentId, surname, name, patr, schoolId) {
      let r = await fetch(`/api/students/${studentId}/`, {
        method: "PATCH",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify({
          surname,
          name,
          patr,
          school: schoolId,
        }),
      });
      await this.fetchStudents();
    },
    async fetchTeachers() {
      let r = await fetch("/api/teachers/");
      this.teachers = await r.json();
    },
    async addTeacher(surname, name, patr) {
      let r = await fetch(`/api/teachers/`, {
        method: "POST",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify({
          surname,
          name,
          patr,
        }),
      });
      await this.fetchTeachers();
    },
    async deleteTeacher(teacherId) {
      let r = await fetch(`/api/teachers/${teacherId}/`, {
        method: "DELETE",
      });
      await this.fetchTeachers();
    },
    async updTeacher(teacherId, name, surname, patr) {
      let r = await fetch(`/api/teachers/${teacherId}/`, {
        method: "PATCH",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify({
          name,
          surname,
          patr,
        }),
      });
      await this.fetchTeachers();
    },
    async fetchSchools() {
      let r = await fetch("/api/schools/");
      this.schools = await r.json();
    },
    async addSchool(title) {
      let r = await fetch(`/api/schools/`, {
        method: "POST",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify({
          title,
        }),
      });
      await this.fetchSchools();
    },
    async deleteSchool(schoolId) {
      let r = await fetch(`/api/schools/${schoolId}/`, {
        method: "DELETE",
       
      });
      await this.fetchSchools();
    },
    async updSchool(schoolId, title) {
      let r = await fetch(`/api/schools/${schoolId}/`, {
        method: "PATCH",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify({
          title,
        }),
      });
      await this.fetchSchools();
    },
    async fetchSubjects() {
      let r = await fetch("/api/subjects/");
      this.subjects = await r.json();
    },
    async fetchLessons() {
      let r = await fetch("/api/lessons/");
      this.lessons = await r.json();
    },
    async addSubject(level, name, time, teacher) {
      let r = await fetch(`/api/subjects/`, {
        method: "POST",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify({
          level,
          name,
          time,
          teacher,
        }),
      });
      await this.fetchSubjects();
    },
    async deleteSubject(subjectId) {
      let r = await fetch(`/api/subjects/${subjectId}/`, {
        method: "DELETE",
      });
      await this.fetchSubjects();
    },
    async updSubject(subjectId, name, level, time, teacher_fio) {
      let r = await fetch(`/api/subjects/${subjectId}/`, {
        method: "PATCH",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify({
          name,
          level,
          time,
          teacher_fio,
        }),
      });
      await this.fetchSubjects();
    },
    async fetchReports(subjectId) {
      let r = await fetch(`/api/journals/${subjectId}/school/`);
      this.reports = await r.json();
    },
    async fetchChoices() {
      let r = await fetch("/api/choices/");
      this.choices = await r.json();
    },
    async addChoice(
      students,
      year,
      semester,
      sub_first,
      sub_second,
      num_class
    ) {
      let r = await fetch(`/api/choices/`, {
        method: "POST",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify({
          students,
          year: "" + year,
          semester: "" + semester,
          sub_first,
          sub_second,
          num_class,
        }),
      });
      await this.fetchChoices();
    },
    // AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    async updateChoice(
      choiceId,
      students_name,
      year,
      semester,
      sub_first,
      sub_second,
      num_class
    ) {
      let r = await fetch(`/api/choices/${choiceId}/`, {
        method: "PATCH",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify({
          students_name,
          year,
          semester,
          sub_first,
          sub_second,
          num_class,
        }),
      });
      await this.fetchChoices();
    },
    async deleteChoice(choiceId) {
      let r = await fetch(`/api/choices/${choiceId}/`, {
        method: "DELETE",
      });
      await this.fetchChoices();
    },
  },
});
