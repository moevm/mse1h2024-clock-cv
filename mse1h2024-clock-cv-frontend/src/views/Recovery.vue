<template>
    <div class="block1">
        <form class="forms" @submit.prevent="submitForm">
            <div class="Rectangle2">
                <div class="Rectangle4">
                    <p class="text3">Восстановление пароля</p>
                </div>
            </div>
            <div class="Rectangle3">
                <input id="emailInput" type="email" class="Input" placeholder="Введите адрес эл. почты" v-model="email">
            </div>
            <div class="block2">
                <button class="recoveryknop" type="submit">Отправить новый пароль на почту</button>
            </div>
            
        </form>
        <div class="block3">
            <router-link to="/"><button class="returnknop">Вернуться назад</button></router-link>    
        </div>
    </div>

    <ErrorModal :show="isErrorModalShown" :errorText="errorMessage" @close="closeErrorModal"/>
</template>

<script>
import ErrorModal from "@/components/ErrorModal.vue";
import axios from "axios";
import router from "@/js/router";

export default {
    name: 'RecoveryComp',
    components: {ErrorModal},
    data() {
        return {
            email: '',
            isErrorModalShown: false,
            errorMessage: ''
        }
    },
    methods: {
        submitForm() {
            if (this.email.length === 0){
                this.errorMessage = 'Заполните поле'
                this.isErrorModalShown = true
                return
            }
            const formData = {
                email: this.email,
            }

            axios.post('/recover-password', formData,
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
                this.isErrorModalShown = true
                this.errorMessage = "Пароль отправлен на почту"
            }).catch( error => {
                this.isErrorModalShown = true
                this.errorMessage = error
                console.log(error)
            });
        },

        closeErrorModal() {
            this.isErrorModalShown = false;
            router.push('/')
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

.block2 {
    position: absolute;
    right: 4.5vw;
}

.block3 {
    position: absolute;
    right: 4.5vw;
    bottom: 0;
}

.Rectangle2 {
    width: 51vw;;
    height: 12.5vh;
    background: #FFFDFD;
    margin-left: auto;
    margin-right: 4vw;
    margin-top: 3vh;
}

.Rectangle3 {
    width: 51vw;
    height: 12.5vh;
    background: #FFFDFD;
    margin: 1.5% 4% 2% auto;
}

.Rectangle4 {
    width: 49.4vw;
    height: 10vh;
    background: rgba(217, 217, 217, 0);
    border: 0.3vw #6FD9CD solid;
    transform: translate(1.2%, 7%);
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

.Input {
    color: rgba(0, 0, 0, 0.35);
    font-size: 3vw;
    font-weight: 400;
    word-wrap: break-word;
    width: 51vw;
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

.recoveryknop {
    width: 51vw;
    height: 14vh;
    background: #6FD9CD;
    border-radius: 1.32vw;
    border: 0.53vw #FFFDFD solid;
    text-align: center;
    line-height: 3.4vh;
    box-sizing: border-box;
    text-align: center;
    color: black;
    font-size: 2.64vw;
    font-weight: 400;
    word-wrap: break-word;
    font-family: Comfortaa;
}

.recoveryknop:hover {
    cursor: pointer;
    background: #0991A4;
}

.returnknop {
    width: 51vw;
    height: 14vh;
    background: #6FD9CD;
    border-radius: 1.32vw;
    border: 0.53vw #FFFDFD solid;
    text-align: center;
    text-align: center;
    color: black;
    font-size: 2.64vw;
    font-weight: 400;
    word-wrap: break-word;
    font-family: Comfortaa;
}

.returnknop:hover {
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