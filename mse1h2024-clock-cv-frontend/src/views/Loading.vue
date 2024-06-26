<template>
    <div class="explanation">
        Необходимо нарисовать циферблат и
        расположить на нем цифры согласно
        общепринятой картине часов в 12-часовом
        формате. На циферблате
        необходимо указать определенное время - {{ store.state.randomHours }}:{{ store.state.randomMinutes }}.
        Цифры должны быть такими же, как на образце.
    </div>
    <div id="error" hidden="hidden">
        Изображение должно иметь расширение
        <q style="quotes: '\00ab' '\00bb'">png</q>
        и иметь такой же размер как изначальный макет!
    </div>
    <div class="container">
        <div class="clock">
            <TheClock :hours="store.state.randomHours" :minutes="store.state.randomMinutes"></TheClock>
            <br>
            <span class="clock-text">Образец полученного циферблата</span>
        </div>
        <div class="buttons">
            <input type="file" id="upload-input" ref="file"
                   hidden/>
            <button class="upload-button">
                <label for="upload-input" class="download-label">
                    Загрузить
                </label>
            </button>
            <br>
            <a href="/clock-sample.png" download="clock-sample.png">
                <button class="download-button">Скачать макет</button>
            </a>
        </div>
    </div>
    <br>
    <div class="flex-buttons">
        <button id="result-button" disabled v-on:click="submitFile()">Результат</button>
        <router-link to="/history" v-if="$store.state.userName.length > 0">
            <button>История</button>
        </router-link>
    </div>

    <UploadProgress v-if="isLoading"></UploadProgress>
    <ErrorModal :show="isErrorModalShown" :errorText="errorMessage" @close="closeErrorModal"/>
</template>

<script>
import axios from "axios"
import TheClock from "@/components/TheClock.vue";
import store from "@/js/store";
import router from "@/js/router";
import UploadProgress from "@/components/UploadProgress.vue";
import ErrorModal from "@/components/ErrorModal.vue";

export default {
    name: 'LoadingPage',
    computed: {
        store() {
            return store
        }
    },
    components: {ErrorModal, UploadProgress, TheClock},
    data() {
        return {
            isLoading: false,
            isErrorModalShown: false,
            errorMessage: 'Изображение должно иметь расширение png и иметь такой же размер как изначальный макет!'
        }
    },
    methods: {
        submitFile() {
            this.isLoading = true
            let formData = new FormData();
            let url ='/upload'
            formData.append('file', this.$refs.file.files[0])
            formData.append('hours', store.state.randomHours)
            formData.append('minutes', store.state.randomMinutes)
            if(store.state.userId){
                url += `?user_id=${store.state.userId}`
            }
            axios.post(url, formData,
                {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }
            ).then( res => {
                this.isLoading = false
                if(res.data.error) {
                    this.isErrorModalShown = true
                    this.isLoading = false
                    this.errorMessage = res.data.error
                    return
                }
                store.state.result = res.data.result
                store.state.description = res.data.description
                store.state.imageId = res.data.imageId
                router.push('/result')
            }).catch( error => {
                this.isErrorModalShown = true
                this.isLoading = false
                this.errorMessage = error
                console.log(error);
            });
        },

        closeErrorModal() {
            this.isErrorModalShown = false;
        }
    },
    beforeMount() {
      store.state.randomHours = Math.floor(Math.random() * (12)) + 1
      store.state.randomMinutes = Math.floor(Math.random() * (59 + 1))
    },
    mounted() {
        const fileInput = document.getElementById('upload-input');

        fileInput.addEventListener('change', () => {
            const file = fileInput.files[0];
            if (file) {
                if (!file.name.endsWith('.png')) {
                    this.isErrorModalShown = true
                    return
                }
                const fileReader = new FileReader();
                fileReader.onload = (e) => {
                    const img = new Image();
                    try {
                        img.src = e.target.result;
                    } catch (error) {
                        this.isErrorModalShown = true
                        console.log(error)
                    }

                    img.onload = () => {
                        let width = img.width;
                        let height = img.height;
                        if (width !== 1190 || height !== 699) {
                            this.isErrorModalShown = true
                            return
                        }
                        document.getElementById("result-button").removeAttribute("disabled")
                        document.getElementById("upload-input").setAttribute("disabled", "disabled")
                        document.getElementById('error').setAttribute('hidden', 'hidden')
                    };
                };
                fileReader.readAsDataURL(file);
            }
        });
    }
}
</script>

<style scoped>
.flex-buttons {
    display: flex;
    justify-content: center;
    width: 62vw;
    margin-left: 30vw;
    margin-top: 1vw;
}

.flex-buttons button {
    margin-left: 1vw;
}

.explanation {
    width: 65vw;
    margin-left: 28vw;
    margin-top: 4%;
    font-size: 2.2vw;
    text-align: justify;
}

#error {
    position: absolute;
    left: 3vw;
    top: 33vw;
    width: 20vw;
    font-size: 1.5vw;
    background-color: indianred;
    padding: 1vw;
    border-radius: 1vw;
    text-align: center;
}

.container {
    width: 62vw;
    height: 35vw;
    background-color: rgb(255, 253, 253, 0.42);
    margin-top: 2.5vw;
    margin-left: 30vw;
    border: 0.5vw solid #6FD9CD;
}

.clock {
    width: 22vw;
    height: 22vw;
    padding-left: 6.6vw;
    padding-top: 6.9vw;
    float: left;
    font-size: 1.65vw;
    text-align: center;
    position: relative;
}

.clock-text {
    left: 7vw;
    position: absolute;
    top: 30vw;
}

.buttons {
    float: left;
    padding-left: 3.9vw;
}

.upload-button {
    margin-top: 8.85vw;
}

.download-button {
    margin-top: 5.42vw;
}

button {
    width: 25.89vw;
    height: 7.13vw;
    background-color: #6FD9CD;
    border-radius: 1.32vw;
    border: 0.52vw solid #FFFDFD;
    font-size: 2.64vw;
    font-family: "Comfortaa", sans-serif;
}

button:hover {
    background-color: #0991A4;
    cursor: pointer;
}

.download-label:hover {
    cursor: pointer;
}

.download-label {
    display: block;
    height: 100%;
    width: 100%;
    padding-top: 6%;
    margin: auto;
}

</style>