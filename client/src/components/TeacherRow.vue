<script setup>
defineProps({
    name: String,
    surname: String,
    patr: String
})

const emit = defineEmits(["nameClick", "surnameClick", "delete", "update"])


</script>

<template>
    <table>
      
        <tbody>
    <tr>
        <td><span @click="$emit('nameClick')"><input type="text" v-model="name"> </span>  </td>
        <td><span @click="OnSurnameClick"><input type="text" v-model="surname"> </span> </td>
        <td><span> <input type="text" v-model="patr"> </span>  </td>
        <td><span @click="$emit('delete')">delete</span></td>
        <td><span @click="$emit('update', {name, surname, patr})">update</span></td>
    
    </tr>
    </tbody>
    </table>
</template>

<style scoped lang="scss">

</style>
