import {defineStore} from "pinia";
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
            try {
                const response = await axios.get(`/api/teachers/${id}/`);
                const teacher = response.data;
                this.teacher = teacher;
            } catch (error) {
                console.log(error)
            }
        },

        async fetchTeacherSubjects(teacherId) {
            const response = await axios.get(`/api/teachers/subjects/`);
            this.subjects = response.data.subjects;
        },

        async fetchSubjectById(subjectId) {
            const response = await axios.get(`/api/subjects/${subjectId}/`);
            this.subject = response.data;
        },

        async fetchSubjectLessons(subjectId) {
            const response = await axios.get(`/api/subjects/${subjectId}/lessons/`);
            this.lessons = response.data["sub-lessons"];
        },

        // 22.08.2022
        async addLesson({topic, date, subjectId, homework}) {
            this.isLoading = true;
            //работает не трогать
            let response = await axios.post("/api/lessons/", {
                topic: topic,
                date: date,
                homework: homework,
                subjects: subjectId,
            });

            this.fetchSubjectLessons(subjectId).finally(
                () => (this.isLoading = false)
            );
        },

        // 23.08.2022
        async updateLesson(lessonId, updatedLesson) {
            this.isLoading = true;

            let response = await axios.patch(`/api/lessons/${lessonId}/`, {
                topic: updatedLesson.topic,
                date: updatedLesson.date,
                homework: updatedLesson.homework,
                subjects: updatedLesson.subjectId,
            });

            await this.fetchSubjectLessons(updatedLesson.subjects)

            this.isLoading = false;
        },

        async removeLesson(lesson) {
            if (confirm("Подтвердите удаление урока")) {
                let response = await axios.delete(`/api/lessons/${lesson.id}/`);
                await this.fetchSubjectLessons(lesson.subjects);
            }
        },

        // 29.08.2022
        async fetchStudentsBySubjectId(subjectId) {
            this.isLoading = true;

            const response = await axios.get(`/api/subjects/${subjectId}/students/`);
            this.subjectStudents = response.data["sub-journal"];

            this.isLoading = false;
        },

        async fetchLessonById(lessonId) {
            this.isLoading = true;

            const response = await axios.get(`/api/lessons/${lessonId}/`);
            this.lesson = response.data;

            this.isLoading = false;
        },

        // 30.08.2022
        async fetchMarksByLessonId(lessonId) {
            const response = await axios.get(`/api/lessons/${lessonId}/journal/`);
            this.marks = response.data.journal;
        },

        async addMark({studentId, mark, lessonId}) {
            let response = await axios.post("/api/journals/", {
                students: studentId,
                lessons: lessonId,
                mark: String(mark),
            })
        },

        async updateMark({markId, mark}) {
            let response = await axios.patch(`/api/journals/${markId}/`, {
                mark: mark,
            });

        },

        // 02.09.2022
        async fetchReportBySubjectId(subjectId) {
            this.isLoading = true;

            const response = await axios.get(`/api/journals/${subjectId}/subject/`);
            this.report = response.data["sub-journal"];

            this.isLoading = false;
        },
        async fetchTeacherId() {
            this.isLoading = true;
            let r = await axios.get('/api/teachers/user/')
            //console.log(r.data.teacher[0].user);
            this.teacherId = r.data.teacher[0].id;
            //console.log(this.teacherId);
            this.isLoading = false;
            return this.teacherId;
        },
    },

});
