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

<HEAD>
    
</HEAD>
<template>
  
    <form @submit.prevent.stop="onSubmit">
    <div class="card-body">

    <div class="d-flex justify-content-center">
        <div class="row mb-3" style="width: 400px">
            <div class="card" style="width:18 rem">
            <img src="https://github.com/ladybag38/cont/blob/main/logo.PNG?raw=true" height="150">
            <div class="col-12">
               
            <label class="col-sm-2 col-form-label" ></label>
                <input type="text" v-model="username" class="form-control" placeholder="Логин">
            </div>
            <div class="col-12">
                <label class="form-label"></label>
                <input type="password" v-model="password" class="form-control" placeholder="Пароль">
                <label class="form-label"></label>
            </div>
            <div class="d-grid gap-2">
                <label class="form-label" ></label>
                <button type="submit" class="btn btn-primary">Войти</button>
                <label class="form-label" ></label>
            </div>
        </div>
    </div>
</div>
</div>
    </form>
</template>


<style scoped>
.btn-primary{

background-color: rgb(5, 33, 84);
height: 40px;
color: rgb(255, 255, 255);

}
.form-control{
    width: 370px;
}



</style>