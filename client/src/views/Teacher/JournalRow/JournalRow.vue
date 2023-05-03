<script setup>
defineProps({
    number: Number,
    name: String,
    mark: Number | String,
    hwmark: Number | String,
    markId: Number | undefined,
    onSave: Function,
})

const emits = defineEmits(
    ['hwmark-clicked', 'mark-clicked']
)

const MARKS = [
    '2',
    '3',
    '4',
    '5',
    'н',
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
            <div class="btn-group 1">
            <div v-for="m in MARKS"
                 class="btn "
                 :class="{'btn-primary': mark===m, 'btn-outline-primary': m !== mark}"
                 @click="onMarkClicked(m)">{{m}}</div>
            </div>
        </td>
        <td>
            <div class="btn-group 2">
            <div v-for="r in MARKS"
                 class="btn "
                 :class="{'btn-primary': hwmark===r, 'btn-outline-primary': r !== hwmark}"
                 @click="onHwMarkClicked(r)">{{r}}</div>
            </div>
        </td>
    </tr>
</template>

