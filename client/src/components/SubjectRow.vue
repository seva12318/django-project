<script setup>
defineProps({
    level: String,
    name: String,
    time: String,
    teacher_fio: String,
})

const emit = defineEmits([ "delete", "update"])

</script>

<template>
    <div>
        <span > Наименование: <input type="text" v-model="name"> </span>  
        <span > Уровень: <input type="text" v-model="level"> </span> 
        <span> Время: <input type="text" v-model="time"> </span>  
        <span> Преподаватель: <input type="text" v-model="teacher_fio"> </span>
        <span @click="$emit('delete')">delete</span>
        <span @click="$emit('update', {name, level, time, teacher_fio})">update</span>
    </div>
</template>

<style>

</style>