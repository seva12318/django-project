<script setup>
defineProps({
    number: Number,
    name: String,
    mark: Number | String,
    hwmark: Number | String,
    markId: Number | undefined,
    onSave: Function,
    hwavailable: Number
})

const emits = defineEmits(
    ['hwmark-clicked', 'mark-clicked']
)

const MARKS = [
    '2',
    '3',
    '4',
    '5',
    'Н',
]

async function onMarkClicked(m) {
    emits('mark-clicked', m);
}

async function onHwMarkClicked(m) {
    emits('hwmark-clicked', m);
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
                 :class="{'btn-success': mark===m, 'btn-outline-primary': m !== mark}"
                 @click="onMarkClicked(m)">{{m}}</div>
            </div>
        </td>
        <td v-if="hwavailable !== 0">
            <div class="btn-group">
            <div v-for="r in MARKS"
                 class="btn "
                 :class="{'btn-success': hwmark===r, 'btn-outline-primary': r !== hwmark}"
                 @click="onHwMarkClicked(r)">{{r}}</div>
            </div>
        </td>
    </tr>
</template>

<style scoped>
  .btn-success {
    background-color: rgb(5, 33, 84);
    border-color: rgb(47, 97, 245);
  }
</style>