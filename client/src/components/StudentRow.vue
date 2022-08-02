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
        <table> 
        <tbody>
    <tr>
        <td><span @click="$emit('nameClick')"><input type="text" v-model="name"> </span>  </td>
        <td><span @click="OnSurnameClick"><input type="text" v-model="surname"> </span> </td>
        <td><span><input type="text" v-model="patr"> </span>  </td>
        <td><span><input type="text" v-model="school_title"> </span> </td>
        <td><button @click="$emit('delete')">удалить</button></td>
        <td><button @click="$emit('update', {name, surname, patr, school_title})">обновить</button></td>
        </tr>
        </tbody>
        </table>
    </div>
</template>

<style>

</style>