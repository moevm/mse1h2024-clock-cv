import { createRouter, createWebHashHistory } from "vue-router";

import Login from './views/Login.vue';
import Result from './views/Result.vue';
import Loading from "./views/Loading.vue";
import Registr from "./views/Registr.vue";
import Recovery from './views/Recovery.vue'
//import History from './views/History.vue'


const routes = [
    { path: '/', name: 'Login', component: Login },
    { path: '/loading', name: 'Loading', component: Loading},
    { path: '/result', name: 'Result', component: Result},
    { path: '/registr', name: 'Registr', component: Registr}/*,
    { path: '/history', name: 'History', component: History}*/,
    { path: '/recovery', name: 'Recovery', component: Recovery}
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
