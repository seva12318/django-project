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
      <table>
      
        <tbody>
    <tr>
        <td><span><input type="text" v-model="name"> </span>  </td>
        <td><span><input type="text" v-model="level"> </span> </td>
        <td><span><input type="text" v-model="time"> </span>  </td>
        <td><span><input type="text" v-model="teacher_fio"> </span></td>
        <td><button @click="$emit('delete')">удалить</button></td>
        <td><button @click="$emit('update', {name, level, time, teacher_fio})">обновить</button></td>
    </tr>
    </tbody>
    </table>
</template>

<style>

</style>