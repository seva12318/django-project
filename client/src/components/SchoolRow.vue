<script setup>
defineProps({
    school_title: String,
    isEdit: Boolean,
})

const emit = defineEmits(["nameClick", "delete", "update"])

</script>

<template>
    <div>
        <table>
            <tbody>
                <tr>
                    <td><span> <input type="text" v-model="school_title" :disabled="!isEdit"> </span> </td>
                    <td v-show="isEdit">
                        <button
                        @click="$emit('update', {school_title})"
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

<style>

</style>