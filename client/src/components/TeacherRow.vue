<script setup>
defineProps({
    name: String,
    surname: String,
    patr: String,
    isEdit: Boolean,
})

const emit = defineEmits(["nameClick", "surnameClick", "delete", "update"])


</script>

<template>
<div>
    <table>
      
        <tbody>
    <tr>
        <td><span @click="$emit('nameClick')"><input type="text" v-model="name" :disabled="!isEdit"> </span>  </td>
        <td><span @click="OnSurnameClick"><input type="text" v-model="surname" :disabled="!isEdit"> </span> </td>
        <td><span> <input type="text" v-model="patr" :disabled="!isEdit"> </span>  </td>
        <td v-show="isEdit">
            <button
              @click="$emit('update', { name, surname, patr })"
            >
              Сохранить
            </button>
          </td>
          <td v-show="isEdit">
            <button @click="$emit('delete')">Удалить</button>
          </td>
    </tr>
    </tbody>
    </table>
    </div>
</template>

<style scoped lang="scss">

</style>
