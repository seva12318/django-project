<script>
export default {
  props: {
    show: Boolean,
    onClose: Function,
  },
};
</script>

<template>
  <div class="anchor">
    <slot name="anchor"></slot>
    <div class="popup" v-show="show" @mouseleave="onClose()">
      <slot name="body"></slot>
    </div>
  </div>
</template>

<style scoped>
.anchor {
  position: relative;
  height: 50px;
}
.popup {
  position: absolute;
  z-index: 1;
  top: 25px;
  left: 0;
  display: flex;
  flex-direction: column;

  background: #42b983;
  width: 220px;
}
</style>
