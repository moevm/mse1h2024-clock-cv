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
                    <p class="text3">Регистрация</p>
                </div>
            </div>
            <div class="Rectangle3">
                <input id="nameInput" class="Input" type="text" placeholder="ФИО" v-model="name">
            </div>
            <div class="Rectangle3">
                <input id="emailInput" type="email" class="Input" placeholder="Почта" v-model="email">
            </div>
            <div class="Rectangle3">
                <input id="passwordInput" type="password" class="Input" placeholder="Пароль" v-model="password">
            </div>
            <div class="Rectangle3">
                <input id="passwordInputrepit" type="password" class="Input" placeholder="Повторите пароль"
                       v-model="passwordConfirmation">
            </div>
            <button class="loginknop1" type="submit">Зарегистрироваться</button>
        </form>
        <div class="blockinf" style="text-align:center">
            <p class="text4">Уже есть учетная запись?
                <router-link to="/" class="link">Войти<br/></router-link>
            </p>
            <p class="text4">Или используете
                <router-link to="/loading" class="link" @click="setEntry"> гостевой вход<br/></router-link>
            </p>
            <p class="text4">Забыли пароль?
                <router-link to="/recovery" class="link"> Восстановить пароль</router-link>
            </p>
        </div>

        <ErrorModal :show="isErrorModalShown" :errorText="errorMessage" @close="closeErrorModal"/>
    </div>
</template>

<script>
import axios from "axios";
import store from "@/js/store";
import router from "@/js/router";
import ErrorModal from '../components/ErrorModal.vue';

export default {
    name: 'RegistrComp',
    components: {
        ErrorModal
    },
    data() {
        return {
            name: '',
            email: '',
            password: '',
            passwordConfirmation: '',
            isErrorModalShown: false,
            errorMessage: ''
        }
    },
    methods: {
        submitForm() {
            if (this.name.length === 0 || this.email.length === 0 || this.password.length === 0 || this.passwordConfirmation.length === 0) {
                this.errorMessage = 'Заполните все поля!'
                this.isErrorModalShown = true
                return
            }
            if (this.password !== this.passwordConfirmation) {
                this.errorMessage = 'пароли не совпадают'
                this.isErrorModalShown = true
                return
            }

            const formData = {
                name: this.name,
                email: this.email,
                password: this.password
            }

            axios.post('/create-user', formData,
                {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                }
            ).then( res => {
                if (res.data.status !== 'ok') {
                    this.errorMessage = res.data.status
                    this.isErrorModalShown = true
                    return
                }
                store.state.entry = true
                store.state.userId = res.data.userId
                store.state.userName = res.data.userName
                router.push('/loading')
            }).catch( error => {
                console.log(error)
                this.isErrorModalShown = true
                this.errorMessage = error
            });
        },

        closeErrorModal() {
            this.isErrorModalShown = false
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

.loginknop1 {
    width: 36vw;
    height: 12vh;
    background: #6FD9CD;
    border-radius: 1.32vw;
    border: 0.53vw #FFFDFD solid;
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

.loginknop1:hover {
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