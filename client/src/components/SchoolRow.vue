<script setup>
defineProps({
    name: String
})

const emit = defineEmits(["nameClick", "delete", "update"])

</script>

<template>
    <div>
        <span class="school-name" @click="$emit('nameClick')"> Имя: <input type="text" v-model="name"> </span>  
        <span @click="$emit('delete')">delete</span>
        <span @click="$emit('update', {name})">update</span>
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