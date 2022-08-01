<script setup>
defineProps({
    name: String,
    surname: String,
    patr: String,
    school_title: String
})

const emit = defineEmits(["nameClick", "surnameClick", "delete", "update"])
function onSurnameClick(){
    emit("surnameClick",{
        "studentName": props.name,
        "studentSurname": props.surname,
    })
}

</script>

<template>
    <div>
        <span class="student-name" @click="$emit('nameClick')"> Имя: <input type="text" v-model="name"> </span>  
        <span class="student-surname" @click="OnSurnameClick"> Фамилия: <input type="text" v-model="surname"> </span> 
        <span> Отчество: <input type="text" v-model="patr"> </span>  
        <span> Школа: <input type="text" v-model="school_title"> </span> 
        <!-- добавить обновление школы -->
        <span @click="$emit('delete')">delete</span>
        <span @click="$emit('update', {name, surname, patr, school_title})">update</span>
    </div>
</template>

<style>
.student-name{
    background-color: aquamarine;
}
.student-surname{
    background-color: beige;
}
</style>