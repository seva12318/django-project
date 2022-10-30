<template lang="">
  <div
    class="journal_record"
    :class="{ odd: number % 2 === 1, even: number % 2 === 0 }"
  >
    <span>{{ number }}</span>
    <span>{{ name }}</span>
    <select
      v-model="mark"
      @change="save(markId, mark)"
      placeholder="Оцена за урок"
    >
      <option value="2">2</option>
      <option value="3">3</option>
      <option value="4">4</option>
      <option value="5">5</option>
      <option value="x">x</option>
    </select>
    <!-- <input v-model="mark" @input="save(markId, mark)" /> -->
  </div>
</template>
<script setup>
import { debounce } from "../../../util/debounce";
defineProps({
  number: Number,
  name: String,
  mark: Number,
  markId: Number | undefined,
  onSave: Function,
});
</script>
<script>
export default {
  props: {
    onSave: {
      type: Function,
    },
  },
  data() {
    return { save: debounce(this.$props.onSave, 500) };
  },
};
</script>
<style scoped>
.journal_record {
  display: flex;
  justify-content: flex-start;
}

.journal_record > span,
input,
select {
  width: calc(100% / 3);
  border: 1px solid black;
  border-top: none;
  border-right: none;
  padding: 5px;
}

.journal_record > span:first-child {
  width: 40px;
}

.journal_record > input:last-child {
  border-right: 1px solid black;
}

.journal_record.odd * {
  background: rgb(187, 186, 186);
}
</style>
