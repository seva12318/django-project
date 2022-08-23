<script setup>
defineProps({
  studentName: String,
  year: Number,
  semester: Number,
  firstSubject: Object,
  firstSubjects: Array,
  secondSubject: Object,
  secondSubjects: Array,
  classTitle: String,
  isEdit: Boolean,
});

const emit = defineEmits(["delete", "update"]);
</script>
<script>
export default {
  data() {
    return {
      firstSubjectId: this.firstSubject.id,
      secondSubjectId: this.secondSubject.id,
    };
  },
};
</script>
<template>
  <div>
    <table>
      <tbody>
        <tr>
          <td>
            <input type="text" disabled v-model="studentName" class="name" />
          </td>
          <td>
            <input
              type="number"
              v-model="year"
              :disabled="!isEdit"
              class="year"
            />
          </td>
          <td>
            <input
              type="number"
              v-model="semester"
              :disabled="!isEdit"
              class="semester"
            />
          </td>
          <td>
            <input
              type="text"
              v-model="classTitle"
              :disabled="!isEdit"
              class="classTitle"
            />
          </td>
          <td>
            <input
              v-if="!isEdit"
              disabled
              type="text"
              :value="firstSubject.name"
            />
            <select
              v-else
              v-model="firstSubjectId"
              placeholder="Первый предмет"
            >
              <option v-for="s in firstSubjects" :value="s.id">
                {{ `${s.name} ${s.level}` }}
              </option>
            </select>
          </td>
          <td>
            <input
              v-if="!isEdit"
              disabled
              type="text"
              :value="secondSubject.name"
            />
            <select
              v-else
              v-model="secondSubjectId"
              placeholder="Второй предмет"
            >
              <option v-for="s in secondSubjects" :value="s.id">
                {{ `${s.name} ${s.level}` }}
              </option>
            </select>
          </td>
          <td v-show="isEdit">
            <button
              @click="
                $emit('update', {
                  studentName,
                  year,
                  semester,
                  firstSubjectId,
                  secondSubjectId,
                  classTitle,
                })
              "
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

<style scoped>
.name {
  width: 250px;
}
.year {
  max-width: 100px;
}
.semester {
  max-width: 100px;
}
.classTitle {
  max-width: 100px;
}
</style>
