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
    <header >
        <nav class="nav">

        
        
           <template v-if=isAuthenticated> 
            
            <ul>
                <hr style="border-color:  rgb(255, 255, 255); border-width: 0.5px;  " >
                <img src="https://github.com/ladybag38/cont/blob/main/only_logo.png?raw=true" height="100" width="120" padding-right="10px" padding-top="50px"> 
                <li><button type="submit" class="btn btn-primary"><RouterLink to="/" class="rout" active-class="router-link">Список предметов</RouterLink></button></li>
                 <li><button type="submit" class="btn btn-primary"><RouterLink to="/reports/schools"  class="rout" active-class="router-link">Оценки по школам</RouterLink></button></li>
                 <li><button type="submit" class="btn btn-primary"><RouterLink to="/reports/teachers/1/subjects" class="rout" active-class="router-link">Оценки по классам</RouterLink></button></li>
                 <li><button type="submit" class="btn btn-primary"><RouterLink to="/reports/subjects"       class="rout" active-class="router-link">Домашние задания</RouterLink></button></li>
                 <li><button type="submit" class="btn btn-primary" ><RouterLink to="/" @click="onLogout" v-if="isAuthenticated" class="rout" active-class="router-link">Выйти</RouterLink></button></li>

               
                </ul>
               
           </template>
            
    
       
        </nav>
        
    </header>

    <RouterView/>
   
</template>



<style lang="scss">
@import "../node_modules/bootstrap/scss/bootstrap";

* {
    box-sizing: content-box;
    margin: 0;
    padding: 0;
}

a{
    color: rgb(255, 255, 255);
text-decoration: none;}

body {
    background-color: rgb(255, 255, 255);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    font-family: Roboto;
}


.cent{
    list-style: none;
}


#app {
  flex: 1;
    display: flex;
    flex-direction: column;
    height: 100vh;
    padding: 130px 120px;
    background-color: rgb(255, 255, 255);
}

header {
    padding-top: 10px;
    padding-left: 10px;
    padding-bottom: 10px;
    margin-left: 2px;
    border-left: 5px;
    padding-right: 0px;
    
}
.rout:hover{
    color: rgb(255, 255, 255);   
}
.rout{
    color: rgb(255, 255, 255); 
    text-decoration: none;
    padding: 10px;
    font-size: 20px;
   font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}

.router-link:hover{
color: rgb(255, 255, 255);
}

ul{
    position: fixed;
    top: 0;
    margin: 0px;
    height: 50;
    padding: 0px;
    list-style: none ;
    font-size: 0px;
    text-align: center;
    background-color: #fff;

}

li{
    display: inline;
    height: 60px;
    width: 20px;
    font-size: 20px;
    position: relative;
    margin: 0px;
    padding: 5px;
}

.router-link{
font-size: 20px;
padding: 0px;
color: rgb(255, 255, 255);
text-decoration: none;
font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;


}

.nav {
    list-style-type: none;
    margin: 0;
    padding: 0;
    display: block;
    gap: 25px;

    height: 10;
}

.btn-primary{
background-color: rgb(5, 33, 84);
font-weight: 10;
font-size: 15;
padding: 15px 5px;

}

.wrapper {
    flex: 9;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: rgb(255, 255, 255);
    color:rgb(255, 255, 255);
}

textarea {
    resize: none;
    width: 100%;
    padding: 5px 10px;
    background-color: rgb(255, 255, 255);
    color:rgb(163, 163, 163);
}

input {
    width: 100%;
    padding: 5px 10px;
    background-color: rgb(255, 255, 255);
    color:rgb(163, 163, 163);
}

.popup_opener {
    cursor: pointer;
    user-select: none;
    background-color: rgb(255, 255, 255);
    color:rgb(5, 33, 84);
}

.popup_item {
    padding: 10px 20px;
}

.popup_item:hover {
    opacity: 0.5;
    background: #fff;
}



</style>
