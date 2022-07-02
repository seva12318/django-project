<script setup>
defineProps({
    name: String,
    surname: String,
})

// const joinedName =computed(() =>{
//     return name+surname;
// });

const emit = defineEmits(["nameClick", "surnameClick", "delete"])
function onSurnameClick(){
    emit("surnameClick",{
        "studentName": props.name,
        "studentSurname": props.surname,
    })
}

</script>

<template>
    <div>
        <span class="student-name" @click="$emit('nameClick')"> Имя: {{name}} </span>  
        <span class="student-surname" @click="OnSurnameClick"> Фамилия: {{surname}} </span> 
        <span @click="$emit('delete')">delete</span>
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