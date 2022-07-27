<script setup>
defineProps({
    school_title: String
})

const emit = defineEmits(["nameClick", "delete", "update"])

</script>

<template>
    <div>
        <span> Наименование: <input type="text" v-model="school_title"> </span>  
        <span @click="$emit('delete')">delete</span>
        <span @click="$emit('update', {school_title})">update</span>
    </div>
</template>

<style>

</style>