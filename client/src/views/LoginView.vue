<script setup>
import {useAuthStore} from "@/stores/authStore";
import {useRoute, useRouter} from "vue-router";
import {ref} from "vue";

const authStore = useAuthStore();


const username = ref()
const password = ref()

function onSubmit() {
    authStore.login(username.value, password.value);
}
</script>


<template>
    <form @submit.prevent.stop="onSubmit">
    <div class="d-flex justify-content-center">
        <div class="row g-3" style="width: 300px">
            <div class="col-12">
                <label class="form-label">Логин</label>
                <input type="text" v-model="username" class="form-control">
            </div>
            <div class="col-12">
                <label class="form-label">Пароль</label>
                <input type="password" v-model="password" class="form-control">
            </div>
            <div class="col-12">
                <button type="submit" class="btn btn-primary">Войти</button>
            </div>
        </div>
    </div>
    </form>
</template>


<style scoped>

</style>