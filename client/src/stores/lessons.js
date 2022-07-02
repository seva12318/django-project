import { defineStore } from 'pinia'

export const useLessonsStore = defineStore({
    "id": "lessons",
    state: ()=>({
        students:[]
    }),
    actions: {
        async fetchStudents() {
            let r = await fetch("/api/students/");
            this.students = await r.json();
           
        },
        async deleteStudent(studentId) {
            let r = await fetch(`/api/students/${studentId}/`,{
                method: "DELETE"
            });
            await this.fetchStudents();
        }
    }
}) 