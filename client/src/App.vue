<script setup>
import {RouterLink, RouterView, useRoute, useRouter} from "vue-router";
import {onBeforeMount, ref, watch} from "vue";
import {useAuthStore} from "@/stores/authStore";
import {storeToRefs} from "pinia";

const authStore = useAuthStore();
const {
    isAuthenticated,
} = storeToRefs(authStore)

const route = useRoute()
const router = useRouter()

const showPopup = ref();

function openPopup() {
    showPopup.value = true;
}

function closePopup() {
    showPopup.value = false;
}

function changeVisiblePopup() {
    showPopup.value = !this.showPopup;
}

function onLogout() {
    authStore.logout();
}

onBeforeMount(() => {
    authStore.check();
})

watch(isAuthenticated, () => {
    if (isAuthenticated.value) {

        router.push(route?.query?.redirect || "/");
    } else {
        router.push("/login");
    }
})

</script>

<template>
    <header>
        <nav class="nav">

            <div class="flex-grow-1"></div>
            <template v-if=isAuthenticated>
                 <RouterLink to="/">Список предметов</RouterLink>
            </template>
            <a href="#" @click="onLogout" v-if="isAuthenticated">Выход</a>
        </nav>
    </header>

    <RouterView/>
</template>

<style lang="scss">
@import "../node_modules/bootstrap/scss/bootstrap";

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    font-family: Roboto;
}

#app {
    /* flex: 1;
    display: flex;
    flex-direction: column; */
    height: 100vh;
    padding: 0 50px;
}

header {
    padding-top: 20px;
    padding-left: 20px;
    padding-bottom: 20px;
}

.nav {
    flex: 1;
    display: flex;
    gap: 20px;
}

.wrapper {
    flex: 9;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

textarea {
    resize: none;
    width: 100%;
    padding: 5px 10px;
}

input {
    width: 100%;
    padding: 5px 10px;
}

.popup_opener {
    cursor: pointer;
    user-select: none;
}

.popup_item {
    padding: 10px 20px;
}

.popup_item:hover {
    opacity: 0.5;
    background: #fff;
}
</style>
