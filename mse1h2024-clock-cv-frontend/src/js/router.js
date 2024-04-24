import { createRouter, createWebHashHistory } from "vue-router";

import Login from '../views/Login.vue';
import Result from '../views/Result.vue';
import Loading from "../views/Loading.vue";
import Registr from "../views/Registr.vue";
import Recovery from '../views/Recovery.vue'
import History from '../views/History.vue'
import store from "@/js/store";


const routes = [
    { path: '/', name: 'Login', component: Login },
    { path: '/loading', name: 'Loading', component: Loading},
    { path: '/result', name: 'Result', component: Result},
    { path: '/registr', name: 'Registr', component: Registr},
    { path: '/history', name: 'History', component: History},
    { path: '/recovery', name: 'Recovery', component: Recovery},
]

const paths = ['/', '/loading', '/result', '/registr', '/history', '/recovery']
const allowedRoutes = ['/', '/registr', '/recovery']; // список разрешенных маршрутов

const router = createRouter({
    history: createWebHashHistory(),
    routes
})



router.beforeEach((to, from, next) => {
    if(!paths.includes(to.path))
        return
    if (allowedRoutes.includes(to.path) || store.state.entry) {
        next(); // разрешаем переход на заданный маршрут
    } else {
        next('/'); // если маршрут не разрешен, перенаправляем на главную страницу
    }
});
export default router
