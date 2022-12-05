<script setup>
defineProps({
  name: String,
  surname: String,
  patr: String,
  //   school_title: String,
  school: Object,
  schools: Array,
  isEdit: Boolean,
});

const emit = defineEmits(["nameClick", "surnameClick", "delete", "update"]);
function onSurnameClick() {
  emit("surnameClick", {
    studentName: props.name,
    studentSurname: props.surname,
  });
}
</script>

<script>
export default {
  data() {
    return {
      schoolId: this.school.id,
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
            <span @click="$emit('nameClick')"
              ><input type="text" v-model="name" :disabled="!isEdit" />
            </span>
          </td>
          <td>
            <span @click="OnSurnameClick"
              ><input type="text" v-model="surname" :disabled="!isEdit" />
            </span>
          </td>
          <td>
            <span
              ><input type="text" v-model="patr" :disabled="!isEdit" />
            </span>
          </td>
          <td>
            <span>
              <input
                v-if="!isEdit"
                disabled
                type="text"
                :value="school.title"
              />
              <select v-else v-model="schoolId" placeholder="Школа">
                <option v-for="s in schools" :value="s.id">
                  {{ s.title }}
                </option>
              </select>
            </span>
          </td>
          <td v-show="isEdit">
            <button @click="$emit('update', { name, surname, patr, schoolId })">
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

<style></style>
