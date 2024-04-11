<template>
    <div class="block1">
        <form class="forms" @submit.prevent="submitForm">
            <div class="Rectangle2">
                <div class="Rectangle4">
                    <p class="text3">Восстановление пароля</p>
                </div>
            </div>
            <div class="Rectangle3">
                <input id="emailInput" type="email" class="Input" placeholder="Введите адрес эл. почты">
            </div>
            <div class="block2">
                <button class="recoveryknop" type="submit"><p class="text1">Отправить новый пароль на почту</p></button>
            </div>
        </form>
    </div>

    <ErrorModal :show="isErrorModalShown" :errorText="errorMessage" @close="closeErrorModal"/>
</template>

<script>
import ErrorModal from "@/components/ErrorModal.vue";
import axios from "axios";
import router from "@/router";

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
                if (res.data.error) {
                    this.isErrorModalShown = true
                    this.errorMessage = res.data.error
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
    right: 10%;
}

.Rectangle2 {
    width: 992px;
    height: 117px;
    background: #FFFDFD;
    margin-left: auto;
    margin-right: 4%;
    margin-top: 3%;
}

.Rectangle3 {
    width: 992px;
    height: 117px;
    background: #FFFDFD;
    margin: 1.5% 4% 2% auto;
}

.Rectangle4 {
    width: 964px;
    height: 90px;
    background: rgba(217, 217, 217, 0);
    border: 5px #6FD9CD solid;
    transform: translate(1.2%, 7%);
}

.text1 {
    width: 740px;
    height: 79px;
    color: black;
    font-size: 40px;
    font-family: Comfortaa;
    font-weight: 700;
    word-wrap: break-word;
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

.Input {
    color: rgba(0, 0, 0, 0.35);
    font-size: 60px;
    font-weight: 400;
    word-wrap: break-word;
    width: 992px;
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

.recoveryknop {
    width: 780px;
    height: 140px;
    background: #6FD9CD;
    border-radius: 20px;
    border: 6px #FFFDFD solid;
    text-align: center;
    line-height: 35px;
    box-sizing: border-box;
}

.recoveryknop:hover {
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