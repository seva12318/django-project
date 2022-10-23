import {defineStore} from "pinia";
import {ref} from "vue";
import axios from "axios";

export const useAuthStore = defineStore("AuthStore", () => {
    const isAuthenticated = ref(false);
    const userName = ref();
    const csrf = ref();
    const isSuperuser = ref();

    async function check() {
        let r = await axios.get("/api/accounts/check-login/");

        axios.defaults.headers.common['X-CSRFToken'] = r.data.csrf;

        isAuthenticated.value = r.data.authenticated;
        isSuperuser.value = r.data.is_superuser;
        csrf.value = r.data.csrf;
        userName.value = r.data.username;
    }

    async function login(username, password) {
        await logout();
        let r = await axios.post("/api/accounts/login/", {
            username: username,
            password: password,
        });
        await check();
    }

    async function logout() {
        let r = await axios.post("/api/accounts/logout/");
        await check();
    }

    // async function addLesson(topic,homework, date, subjectId ){
    //     let r = await axios.post("/api/lessons/", {
    //         topic:topic,
    //         date:date,
    //         homework:homework,
    //         subjects: subjectId,
    //     });
    // }
    
    return {
        isAuthenticated,
        userName,
        csrf,
        isSuperuser,

        check,
        login,
        logout
    }


})