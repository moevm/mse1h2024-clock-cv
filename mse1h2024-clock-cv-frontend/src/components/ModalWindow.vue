<script>
import axios from "axios";
import TheClock from "@/components/TheClock.vue";
import store from "@/store";

export default {
    name: 'ModalWindow',
    computed: {
        store() {
            return store
        }
    },
    components: {TheClock},
    methods: {
        close() {
            this.$emit('close');
        },
    },
    data() {
        return {
            imageUrl: ''
        }
    },
    mounted() {
        const url = '/images/?id=' + store.state.imageId
        axios.get(url, {responseType: 'arraybuffer'})
            .then(response => {
                const blob = new Blob([response.data], {type: 'image/png'});
                this.imageUrl = URL.createObjectURL(blob);
            })
            .catch(error => {
                console.error('Error fetching image from FastAPI', error);
            });
    }

};
</script>
<template>
    <transition name="modal-fade">
        <div class="modal-backdrop">
            <div class="modal"
                 role="dialog"
                 aria-labelledby="modalTitle"
                 aria-describedby="modalDescription"
            >
                <header
                    class="modal-header"
                    id="modalTitle"
                >
                    <slot name="header">
                        <p class="text4">Количество баллов:<br/><span class="number1">{{ store.state.result }}</span>
                        </p>
                        <button
                            type="button"
                            class="btn-close"
                            @click="close"
                            aria-label="Close modal"
                        >
                            <img src="../assets/close.png" class="closeknop">
                        </button>
                    </slot>
                </header>
                <section
                    class="modal-body"
                    id="modalDescription"
                >
                    <slot name="body">
                        <p class="text5">{{ store.state.description }}</p>
                        <div class="images">
                            <p class="text4">Образец:</p>
                            <div class="clock">
                                <TheClock :minutes=30 :hours=9></TheClock>
                            </div>
                            <p class="text4">Результат:</p>
                            <img :src="imageUrl" alt="Image from FastAPI" class="image-errors"/>
                        </div>
                    </slot>
                </section>
            </div>
        </div>
    </transition>
</template>
<style scoped>
.modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    z-index: 1;
}

.modal {
    width: 1097px;
    height: 863px;
    background: #FFFCFC;
    border-radius: 20px;
    border: 8px #6FD9CD solid;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
}


.modal-header {
    display: flex;
    flex-direction: row;
    color: #4AAE9B;
}

.modal-body {
    position: relative;
    padding: 20px 10px;
}

.btn-close {
    border: none;
    font-size: 20px;
    margin-left: auto;
    margin-right: 2%;
    cursor: pointer;
    font-weight: bold;
    color: #4AAE9B;
    background: transparent;
}

.image-errors {
    width: 100%;
    padding-left: 5vw;
}

.images {
    margin-top: 50px;
    width: 800px;
    text-align: center;
}

.clock {
    width: 17vw;
    height: 17vw;
    padding-left: 17vw;
    text-align: center;
    position: relative;
}

.closeknop {
    width: 88px;
    height: 90px;
}

.text4 {
    color: black;
    font-size: 50px;
    font-family: Comfortaa;
    font-weight: 400;
    word-wrap: break-word;
    margin-left: 20%;
}

.text5 {
    text-align: justify;
    color: black;
    font-size: 50px;
    font-family: Comfortaa;
    font-weight: 700;
    word-wrap: break-word;
    margin-left: 4%;
}

.number1 {
    color: black;
    font-size: 80px;
    font-family: Comfortaa;
    font-weight: 400;
    word-wrap: break-word;
}
</style>