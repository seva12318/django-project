<script setup>
defineProps({
  number: Number,
  students_name: String,
  date: String,
  lessons_name: String,
  mark: String,
});

// const emit = defineEmits(["delete", "update"])
const emit = defineEmits(["nameClick", "surnameClick", "delete", "update"]);
function onSurnameClick() {
  emit("surnameClick", {
    studentName: props.students_name,
    studentSurname: props.lessons_name,
  });
}
</script>

<template>
  <div :id = number
    class="journal_record"
    :class="{ odd: number % 2 === 1, even: number % 2 === 0 }"
  >
    <span>{{ students_name }}</span>
    <span>{{ lessons_name }}</span>
    <span>{{ mark }}</span>
  </div>
</template>

<style scoped>
.journal_record {
  display: flex;
  justify-content: flex-start;
}

.journal_record > span,
input {
  width: calc(100% / 3);
  border: 1px solid black;
  border-top: none;
  border-right: none;
  padding: 5px;
}

.journal_record > span:last-child {
  border-right: 1px solid black;
}

.journal_record.odd * {
  background: rgb(187, 186, 186);
}
</style>
