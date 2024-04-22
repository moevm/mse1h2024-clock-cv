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
                <router-link to="/loading" class="link"> гостевой вход<br/></router-link>
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
import store from "@/store";
import router from "@/router";
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
            this.isErrorModalShown = false;
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
    height: 111px;
    background: linear-gradient(90deg, rgba(217, 242, 239, 0.15) 8%, #EDFDFB 42%, rgba(245.52, 251.43, 251.81, 0.67) 66%, #F6FBFC 95%);
}

.Rectangle2 {
    width: 697px;
    height: 117px;
    background: #FFFDFD;
    margin-left: auto;
    margin-right: 4%;
    margin-top: 7%;
}

.Rectangle3 {
    width: 697px;
    height: 117px;
    background: #FFFDFD;
    margin-left: auto;
    margin-right: 4%;
    margin-top: 1.5%;
}

.Rectangle4 {
    width: 671px;
    height: 90px;
    background: rgba(217, 217, 217, 0);
    border: 5px #6FD9CD solid;
    transform: translate(1.2%, 7%);
}

.text1 {
    text-align: right;
    color: black;
    font-size: 40px;
    font-weight: 400;
    word-wrap: break-word;
    margin: 2% 4% -2%;
}

.text2 {
    text-align: right;
    color: black;
    font-size: 40px;
    font-weight: 400;
    word-wrap: break-word;
    margin-right: 4%;
}

.text3 {
    color: black;
    font-size: 60px;
    font-weight: 700;
    word-wrap: break-word;
    text-align: left;
    margin-top: 1%;
    margin-left: 2%;
}

.text4 {
    color: black;
    font-size: 25px;
    font-weight: 400;
    word-wrap: break-word;
    margin-bottom: -1%;
    position: relative;
    left: 28%;
}


.Input {
    color: rgba(0, 0, 0, 0.35);
    font-size: 60px;
    font-weight: 400;
    word-wrap: break-word;
    width: 690px;
    height: 110px;
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
    width: 697px;
    height: 108px;
    background: #6FD9CD;
    border-radius: 20px;
    border: 6px #FFFDFD solid;
    margin-top: 1%;
    float: right;
    margin-right: 4%;
    text-align: center;
    color: black;
    font-size: 60px;
    font-weight: 400;
    word-wrap: break-word;
    font-family: Comfortaa;
}

.loginknop:hover {
    cursor: pointer;
    background: #0991A4;
}

.loginknop1 {
    width: 697px;
    height: 108px;
    background: #6FD9CD;
    border-radius: 20px;
    border: 6px #FFFDFD solid;
    margin-top: 1%;
    float: right;
    margin-right: 4%;
    text-align: center;
    color: black;
    font-size: 50px;
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
    font-size: 25px;
    font-family: Comfortaa;
    font-weight: 600;
    word-wrap: break-word;
}

</style>