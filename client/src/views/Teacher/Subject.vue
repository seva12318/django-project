<template>
    <div class="wrapper">
        <Loader v-if="!Boolean(lessons) || !Boolean(subject) || isLoading"/>
        <div class="subject_wrapper" v-else>
            <div class="subject_name">
        <span class="subject_title">{{
                `${subject.name} (${subject.level})`
            }}</span>
                <span>
          {{ `Время: ${subject.time}` }}
        </span>
            </div>
            <div class="lessons_wrapper" v-if="lessons.length === 0">
                <div class="subject_no_lessons">
                    На данный момент у вас нет уроков по этому предмету
                </div>
                <div class="btn btn-green" @click="openAddLessonModal()">+ Добавить урок</div>
            </div>
            <div class="lessons_wrapper" v-else>
                <div class="btn btn-green" @click="openAddLessonModal()">+ Добавить урок</div>
                <div class="subject_lessons">
                    <div class="subject_lesson" v-for="(lesson, index) in sortedLessons">
                        <div>
                            <div class="d-flex justify-content-between">
              <span class="title">{{
                      `Урок №${sortedLessons.length - index}`
                  }}</span>
                                <div @click="onRemoveClicked(lesson)" class="btn btn-sm btn-danger">x</div>
                            </div>
                            <hr/>
                            <div>
                                <span class="title">Тема: </span>
                                <span>{{ lesson.topic }}</span>
                            </div>
                            <div>
                                <span class="title">Дата: </span>
                                <span>{{ formatDate(lesson.date) }}</span>
                            </div>
                            <hr/>
                            <span class="title">Домашнее задание:</span>
                            <span class="homework">{{ `${lesson.homework}` }}</span>
                            <hr/>
                        </div>
                        <div class="btns">
                            <div
                                class="btn btn-green "
                                @click="
                  openEditLessonModal({
                    ...lesson,
                    number: sortedLessons.length - index,
                  })
                "
                            >
                                Редактировать
                            </div>
                            <div class="btn btn-green " @click="navigateToLesson(lesson.id)">
                                Открыть журнал
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <ModalLesson
        :showModal="showModal"
        :onClose="onModalClose"
        :onSubmit="isEdit ? onUpdateLesson : onAddLesson"
        :isEdit="isEdit"
        :lesson="currentLesson"
    />
</template>
<script setup>
import {computed, onBeforeMount, ref} from "vue";
import {storeToRefs} from "pinia";
import {useTeacherStore} from "@/stores/teacherStore";
import {formatDate} from "@/util/formatDate";
import Loader from "../../components/Loader/Loader.vue";
import ModalLesson from "./ModalAddLesson/ModalLesson.vue";
import {useAuthStore} from "@/stores/authStore";
import {useRoute, useRouter} from "vue-router";

const authStore = useAuthStore();
const route = useRoute();
const router = useRouter()
const teacherStore = useTeacherStore();

// добавить уроки и удалить из data, когда появится ручка
const {subject, lessons, isLoading} = storeToRefs(teacherStore);
const sortedLessons = computed(() => {
    return lessons !== null
        ? // descending sort
        lessons.value.sort((l1, l2) => (l1.date > l2.date ? -1 : 1))
        : null;
});

const subjectId = ref(route.params.id);
const showModal = ref(false);
const isEdit = ref(false);
const currentLesson = ref({
    topic: "",
    homework: "",
    date: new Date(Date.now()).toISOString().split("T")[0],
});

function onRemoveClicked(lesson) {
    teacherStore.removeLesson(lesson);
}

onBeforeMount(() => {
    teacherStore.fetchSubjectLessons(route.params.id);
    teacherStore.fetchSubjectById(route.params.id);
});

function navigateToLesson(lessonId) {
  router.push({
    path: `/subjects/${subjectId.value}/lessons/${lessonId}/journal`,
  });
}

function onModalOpen() {
  showModal.value = true;
}

function onModalClose() {
  showModal.value = false;
}

function onAddLesson(lesson) {
  teacherStore.addLesson({
    ...lesson,
    subjectId: Number(subjectId.value),
    date: lesson.date,

  });
  onModalClose();
}

function onUpdateLesson(lesson) {
  teacherStore.updateLesson(lesson.id, {
    ...lesson,
    date: lesson.date,
  });
  onModalClose();
}

function openAddLessonModal() {
  isEdit.value = false;
  currentLesson.value = {
    topic: "",
    homework: "",
    date: new Date(Date.now()).toISOString().split("T")[0],
    //csrf: this.csrf
  };
  onModalOpen();
}

function openEditLessonModal(lesson) {
  isEdit.value = true;
  currentLesson.value = lesson;
  onModalOpen();
}
</script>

<style scoped>
.subject_wrapper {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    flex: 1;
    width: 90%;
    padding-top: 50px;
}

.subject_name {
    display: flex;
    flex-direction: column;
    font-size: 22px;
    font-weight: 600;
    text-align: center;
}

.lessons_wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
    gap: 20px;
}

.btn-green {
    padding: 10px 20px;
    border-radius: 8px;
    background: #42b983;

    cursor: pointer;

    display: flex;
    flex-direction: column;
    gap: 10px;

    text-align: center;

    width: fit-content;
    transition: all .3s;
}

.btn-green:hover {
    /*opacity: 0.9;*/
    background: #42b983;
    transform: scale(1.1);
}

.subject_lessons {
    display: flex;
    flex-direction: row;
    justify-content: center;
    flex-wrap: wrap;
    gap: 10px;
    max-width: 100%;
    padding-bottom: 100px;
}

.subject_lesson {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 20px 40px;
    border-radius: 6px;
    border: 1px solid gray;
    min-width: 300px;
    max-width: calc(100% / 4);
}

.subject_lesson hr {
    margin-top: 10px;
    margin-bottom: 10px;
}

.subject_lesson .title {
    font-size: 18px;
    font-weight: 500;
}

.subject_lesson .btns {
    display: flex;
    flex-direction: column;
    gap: 10px;

    align-items: center;
}

.subject_no_lessons {
    margin-top: 200px;
    text-align: center;
}

.homework {
    width: 100px;
    word-wrap: break-word;
}
</style>
