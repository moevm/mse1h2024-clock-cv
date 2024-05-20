<script>
import modal from '../components/ModalWindow.vue'
import store from "../js/store";

export default {
    name: 'ResultComp',
    computed: {
        store() {
            return store
        }
    },
    components: {
        modal,
    },
    data() {
        return {
            isModalVisible: false,
        };
    },
    methods: {
        showModal() {
            this.isModalVisible = true;
        },
        closeModal() {
            this.isModalVisible = false;
        }
    }
};
</script>

<template>
    <div>
        <modal
            v-show="isModalVisible"
            @close="closeModal"
        />
    </div>
    <div>
        <div class="block1">
            <div>
                <router-link to="/loading">
                    <button class="repetknop">Повторить тест</button>
                </router-link>
            </div>
            <div>
                <router-link to="/history">
                    <button class="historyknop" :disabled="store.state.userName.length===0">История тестирований</button>
                </router-link>
            </div>    
        </div>
        <div class="Rectangle1">
            <p class="text1">Имя пользователя:<br/>
                <span class="text2">
                    {{(store.state.userName.length > 0)?store.state.userName:'...'}}
                </span>
            </p>
            <p class="text1">Количество баллов:<br/><span class="number">{{ store.state.result }}</span></p>
        </div>
        <div class="block2">
            <button class="detailknop" @click="showModal">Подробнее</button>
            <div class="text3"><p>Предоставленная информация не явлеяется заменой профессиональной медицинской консультации.
                    Рекомендуется обратиться к специалисту для получения точного диагноза и рекомендаций.</p>
            </div>
        </div>
    </div>
</template>

<style scoped>
.block1 {
    display: flex;
    flex-direction: row;
    gap: 1.9vw;
    justify-content: right;
    margin-top: 2vh;
}

.block2{
    display: flex;
    flex-direction: column;
}

.repetknop {
    width: 24vw;
    height: 12vh;
    background: #6FD9CD;
    border-radius: 1.32vw;
    border: 0.53vw #FFFDFD solid;
    text-align: center;
    font-family: Comfortaa;
    color: black;
    font-size: 2vw;
    font-weight: 400;
    word-wrap: break-word;
}

.repetknop:hover {
    cursor: pointer;
    background: #0991A4;
}

.historyknop {
    width: 32vw;
    height: 12vh;
    background: #6FD9CD;
    border-radius: 1.32vw;
    border: 0.53vw #FFFDFD solid;
    text-align: center;
    color: black;
    font-size: 2vw;
    font-family: Comfortaa;
    font-weight: 400;
    word-wrap: break-word;
}

.historyknop:hover {
    cursor: pointer;
    background: #0991A4;
}

.Rectangle1 {
    width: 56.9vw;
    height: 36vh;
    background: #FFFCFC;
    border-radius: 1.32vw;
    border: 0.53vw #6FD9CD solid;
    margin-left: auto;
    margin-right: 0;
    margin-top: 2vh;
}

.text1 {
    text-align: center;
    color: black;
    font-size: 2vw;
    font-family: Comfortaa;
    font-weight: 400;
    word-wrap: break-word;
}

.text2 {
    text-align: center;
    color: black;
    font-size: 2.6vw;
    font-family: Comfortaa;
    font-weight: 400;
    word-wrap: break-word;
    margin-top: -2vh;
}

.number {
    color: black;
    font-size: 3vw;
    font-family: Comfortaa;
    font-weight: 400;
    word-wrap: break-word;
}

.detailknop {
    width: 25vw;
    height: 12vh;
    background: #6FD9CD;
    border-radius: 1.32vw;
    border: 0.53vw #FFFDFD solid;
    margin-top: 2vh;
    text-align: center;
    color: black;
    font-size: 2.64vw;
    font-family: Comfortaa;
    font-weight: 400;
    word-wrap: break-word;
    position: fixed;
    right: 15vw;
    z-index: -1;
}

.detailknop:hover {
    cursor: pointer;
    background: #0991A4;
}

.text3 {
    width: 50vw;
    height: 9vh;
    text-align: justify;
    color: black;
    font-size: 1.2vw;
    font-family: Comfortaa;
    font-weight: 400;
    word-wrap: break-word;
    position: fixed;
    right: 5vw;
    bottom: 7vh;
    z-index: -1;
}
</style>