<script setup>
defineProps({
    number: Number,
    name: String,
    mark: Number | String,
    markId: Number | undefined,
    onSave: Function,
});

const emits = defineEmits(['mark-clicked']);

const MARKS = [
    '2',
    '3',
    '4',
    '5',
    'н',
]

function onMarkClicked(m) {
    emits('mark-clicked', m);
}
</script>

<template>
    <tr>
        <td>{{ number }}</td>
        <td>{{ name }}</td>
        <td>
            <div class="btn-group">
            <div v-for="m in MARKS"
                 class="btn "
                 :class="{'btn-primary': mark===m, 'btn-outline-primary': m !== mark}"
                 @click="onMarkClicked(m)">{{m}}</div>
            </div>
        </td>
    </tr>
</template>

