<script setup>
import {computed, onBeforeMount} from "vue";
import {storeToRefs} from "pinia";
import {useTeacherStore} from "../../stores/teacherStore";
import {formatDate} from "../../util/formatDate";
import Loader from "../../components/Loader/Loader.vue";
import JournalRow from "./JournalRow/JournalRow.vue";
import {useRoute, useRouter} from "vue-router";

const teacherStore = useTeacherStore();
// добавить уроки и удалить из data, когда появится ручка
const {subjectStudents, lesson, marks, subject, isLoading} = storeToRefs(teacherStore);

const router = useRouter()
const route = useRoute()


const subjectId = computed(() => route.params.subjectId);
const lessonId = computed(() => route.params.lessonId);

const sortedStudents = computed(() => {
    return subjectStudents !== null
        ? // descending sort
        subjectStudents.value.sort((s1, s2) => {
            return s1.surname > s2.surname ? 1 : -1;
        })
        : null;
});

const studentsWithMarks = computed(() => {
    return sortedStudents !== null && marks !== null
        ? sortedStudents.value.map((s) => ({
            ...s,
            mark: marks.value[
                marks.value.findIndex((mark) => mark.students === s.id)
                ]?.mark,
            markId:
            marks.value[marks.value.findIndex((mark) => mark.students === s.id)]
                ?.id,
        }))
        : null;
});

async function onChangeMark(studentId, markId, mark) {
    if (markId) {
        await teacherStore.updateMark({markId, mark});
    } else {
        await teacherStore.addMark({
            studentId,
            lessonId: lessonId.value,
            mark,
        });
    }
    await teacherStore.fetchMarksByLessonId(lessonId.value);
}

function navigateToLessons() {
    router.push({
        path: `/subjects/${subjectId.value}`,
    });
}

onBeforeMount(() => {
    teacherStore.fetchStudentsBySubjectId(subjectId.value);
    teacherStore.fetchLessonById(lessonId.value);
    teacherStore.fetchMarksByLessonId(lessonId.value);
    teacherStore.fetchSubjectById(subjectId.value);
})


</script>

<template>
    <Loader
        v-if="
      !Boolean(subjectStudents) ||
      !Boolean(lesson) ||
      !Boolean(subject) ||
      isLoading
    "
    />
    <div class="journal_wrapper" v-else>
        <h2>
            {{
                `Урок от ${formatDate(lesson.date)} по предмету ${subject.name} (${
                    subject.level
                })`
            }}
        </h2>

        <table class="table">
            <thead>
            <tr>
                <th>№</th>
                <th>ФИО</th>
                <th>Оценка</th>
            </tr>
            </thead>
            <tbody>
            <JournalRow
                v-for="(student, index) in studentsWithMarks"
                :number="index + 1"
                :name="`${student.surname} ${student.name} ${student.patr}`"
                :mark="student.mark || null"
                :markId="student.markId"
                @mark-clicked="onChangeMark(student.id, student.markId, $event)"
            />
            </tbody>
        </table>

        <div class="btn save" @click="navigateToLessons()">&lt; Назад к предмету</div>
    </div>
</template>

<style scoped>
.journal_wrapper {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    flex: 1;
    width: 90%;
    padding: 50px 100px;
}

.journal_header {
    display: flex;
    justify-content: flex-start;
    margin-top: 20px;
}

.journal_header > span {
    width: calc(100% / 3);
    border: 1px solid black;
    border-right: none;
    padding: 5px;
}

.journal_header > span:first-child {
    width: 40px;
}

.journal_header > span:last-child {
    border-right: 1px solid black;
}

.btn {
    padding: 10px 20px;
    border-radius: 8px;
    background: #42b983;

    cursor: pointer;

    display: flex;
    flex-direction: column;
    gap: 10px;

    text-align: center;

    width: fit-content;
}

.btn.save {
    margin-top: 20px;
}

.btn:hover {
    opacity: 0.9;
    transform: scale(1.1);
}
</style>
