<template>
    <div class="block">
        <div class="Rectangle1">
            <p class="text1">Тест “Рисование часов” на определение </p>
            <p class="text2">нарушений памяти</p>
        </div>
    </div>
    <div class="block1">
        <form class="forms" @submit.prevent="submitForm">
            <div class="Rectangle2">
                <div class="Rectangle4">
                    <p class="text3">Вход в систему</p>
                </div>
            </div>
            <div class="Rectangle3">
                <input id="emailInput" class="Input" type="email" placeholder="Почта" v-model="email">
            </div>
            <div class="Rectangle3">
                <input id="passwordInput" type="password" class="Input" placeholder="Пароль" v-model="password">
            </div>
            <button class="loginknop" type="submit">Войти</button>
        </form>
        <div class="blockinf" style="text-align:center">
            <p class="text4">Впервые на сайте?
                <router-link to="/registr" class="link">Зарегистрироваться<br/></router-link>
            </p>
            <p class="text4">Или используете
                <router-link to="/loading" class="link" @click="setEntry"> гостевой вход<br/></router-link>
            </p>
            <p class="text4">Забыли пароль?
                <router-link to="/recovery" class="link"> Восстановить пароль</router-link>
            </p>
        </div>
    </div>

    <ErrorModal :show="isErrorModalShown" :errorText="errorMessage" @close="closeErrorModal"/>
</template>

<script>
import ErrorModal from "@/components/ErrorModal.vue";
import axios from "axios";
import store from "@/js/store";
import router from "@/js/router";

export default {
    name: 'LoginComp',
    components: {ErrorModal},
    data() {
        return {
            email: '',
            password: '',
            isErrorModalShown: false,
            errorMessage: ''
        }
    },
    methods: {
        submitForm() {
            if(this.email.length === 0 || this.password.length === 0){
                this.errorMessage = 'Заполните все поля!'
                this.isErrorModalShown = true
                return
            }
            const formData = {
                email: this.email,
                password: this.password
            }

            axios.post('/entry-user', formData,
                {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                }
            ).then( res => {
                if (res.data.status !== 'ok') {
                    this.isErrorModalShown = true
                    this.errorMessage = res.data.status
                    return
                }
                store.state.entry = true
                store.state.userId = res.data.userId
                store.state.userName = res.data.userName
                router.push('/loading')
            }).catch( error => {
                this.isErrorModalShown = true
                this.errorMessage = error
                console.log(error)
            });
        },

        closeErrorModal() {
            this.isErrorModalShown = false;
        },

        setEntry() {
            store.state.entry = true
        }
    }
}
</script>

<style scoped>

.block1 {
    display: flex;
    justify-content: right;
    flex-direction: column;
}

.Rectangle1 {
    width: 80%;
    margin-left: auto;
    margin-right: 0;
    height: 15vh;
    background: linear-gradient(90deg, rgba(217, 242, 239, 0.15) 8%, #EDFDFB 42%, rgba(245.52, 251.43, 251.81, 0.67) 66%, #F6FBFC 95%);
}

.Rectangle2 {
    width: 36vw;
    height: 12.5vh;
    background: #FFFDFD;
    margin-left: auto;
    margin-right: 4vw;
    margin-top: 7vh;
}

.Rectangle3 {
    width: 36vw;
    height: 12.5vh;
    background: #FFFDFD;
    margin-left: auto;
    margin-right: 4vw;
    margin-top: 1.5vh;
}

.Rectangle4 {
    width: 34.6vw;
    height: 10vh;
    background: rgba(217, 217, 217, 0);
    border: 0.3vw #6FD9CD solid;
    transform: translate(1.2%, 7%);
}

.text1 {
    text-align: right;
    color: black;
    font-size: 2.2vw;
    font-weight: 400;
    word-wrap: break-word;
    margin: 2% 4% -2%;
}

.text2 {
    text-align: right;
    color: black;
    font-size: 2.2vw;
    font-weight: 400;
    word-wrap: break-word;
    margin-right: 4vw;
}

.text3 {
    color: black;
    font-size: 3vw;
    font-weight: 700;
    word-wrap: break-word;
    text-align: left;
    margin-top: 1vh;
    margin-left: 2vw;
}

.text4 {
    color: black;
    font-size: 1.2vw;
    font-weight: 400;
    word-wrap: break-word;
    margin-bottom: -1vh;
    position: relative;
    left: 28vw;
}


.Input {
    color: rgba(0, 0, 0, 0.35);
    font-size: 3vw;
    font-weight: 400;
    word-wrap: break-word;
    width: 36vw;
    height: 12.5vh;
    border: none;
}

.Input::-webkit-input-placeholder {
    font-family: "Comfortaa", sans-serif;
}

.Input:-ms-input-placeholder {
    font-family: "Comfortaa", sans-serif;
}

.Input:-moz-placeholder {
    font-family: "Comfortaa", sans-serif;
}

.Input::-moz-placeholder {
    font-family: "Comfortaa", sans-serif;
}

.loginknop {
    width: 36vw;
    height: 12vh;
    background: #6FD9CD;
    border-radius: 1.32vw;
    border: 0.52vw #FFFDFD solid;
    margin-top: 1vh;
    float: right;
    margin-right: 4vw;
    text-align: center;
    color: black;
    font-size: 2.64vw;
    font-weight: 400;
    word-wrap: break-word;
    font-family: Comfortaa;
}

.loginknop:hover {
    cursor: pointer;
    background: #0991A4;
}

.link {
    color: black;
    font-size: 1.2vw;
    font-family: Comfortaa;
    font-weight: 600;
    word-wrap: break-word;
}

</style>