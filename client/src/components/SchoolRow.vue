<script setup>
defineProps({
    school_title: String
})

const emit = defineEmits(["nameClick", "delete", "update"])

</script>

<template>
    
        <table>
      
        <tbody>
    <tr>
        <td><span> Наименование: <input type="text" v-model="school_title"> </span> </td>
        <td><button @click="$emit('delete')">удалить</button></td>
        <td><button @click="$emit('update', {school_title})">обновить</button></td>
        </tr>
        </tbody>
        </table>
</template>

<style>

</style>