import { createRouter, createWebHashHistory } from "vue-router";

import Login from './views/Login.vue';
import Result from './views/Result.vue';
import LoadingPage from '@/views/LoadingPage.vue';
//import Recovery from './views/Recovery.vue'
//import History from './views/History.vue'


const routes = [
    { path: '/', name: 'Login', component: Login },
    { path: '/home', name: 'Home', component: Home},/*
    { path: '/registr', name: 'Registr', component: Registr},
    { path: '/history', name: 'History', component: History},
    { path: '/result', name: 'Result', component: Result},
    { path: '/recovery', name: 'Recovery', component: Recovery}*/
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
