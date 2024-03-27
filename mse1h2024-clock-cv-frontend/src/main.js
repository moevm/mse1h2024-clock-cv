import { createApp } from 'vue'
import router from './router'
import App from './App.vue'
import axios from "axios";
import store from "./store"

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000/';
const app = createApp(App)

app.use(store)
app.use(router)
app.mount('#app')
