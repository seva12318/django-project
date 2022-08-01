<script setup>
defineProps({
    // school_journal:String,
    students_name: String,
    date: String,
    lessons_name: String,
    mark:String
})

// const emit = defineEmits(["delete", "update"])
const emit = defineEmits(["nameClick", "surnameClick", "delete", "update"])
function onSurnameClick(){
    emit("surnameClick",{
        "studentName": props.students_name,
        "studentSurname": props.lessons_name,
    })
}

</script>

<template>
    <div>
        <span @click="onSurnameClick"> ФИО: <input type="text" v-model="students_name"> </span>  
        <span> Занятие: <input type="text" v-model="lessons_name"> </span> 
        <span> Дата: <input type="text" v-model="date"> </span>  
        <span> Оценка: <input type="text" v-model="mark"> </span> 
    </div>
</template>

<style></style>