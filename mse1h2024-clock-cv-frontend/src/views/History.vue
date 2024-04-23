<template>
    <div class="container">
        <div class="history" v-for="(item, index) in items" :key="index">
            <div class="rectangle" >
                <div class="data">
                    <p>Дата теста</p>
                    <p>{{ item.date }}</p>
                </div>
                <div class="data">
                    <p>Количество баллов</p>
                    <p>{{ item.points }}</p>
                </div>

                <img src="../assets/up.png" alt='открыть описание' @click="showDescription(index)" v-if="!item.show" style="rotate: 180deg"/>
                <img src="../assets/up.png" alt='закрыть описание' @click="showDescription(index)" v-if="item.show"/>
            </div>

            <div class="description" v-if="item.show">
                <p>{{ item.description }}</p>
            </div>
        </div>

        <div class="buttons">
            <button @click="showBarChart">График</button>
            <router-link to="/result">
                <button>Вернуться назад</button>
            </router-link>
        </div>
    </div>

    <div v-if="isBarChartShown">
        <BarChart :arr="items" @close="closeBarChart"></BarChart>
    </div>
    <ErrorModal :show="isErrorModalShown" :errorText="errorMessage" @close="closeErrorModal"/>
</template>

<script>
import axios from "axios";
import store from "@/js/store";
import ErrorModal from "@/components/ErrorModal.vue";
import BarChart from "@/components/BarChart.vue";

export default {
    name: 'HistoryComp',
    components: {BarChart, ErrorModal},
    data() {
        return {
            items: [],
            isErrorModalShown: false,
            errorMessage: '',
            isBarChartShown: false
        };
    },
    methods: {
        showDescription(index) {
            this.items[index].show = !this.items[index].show
        },
        closeErrorModal() {
            this.isErrorModalShown = false
        },
        showBarChart() {
            if(this.items.length > 0)
                this.isBarChartShown = true
        },
        closeBarChart() {
            this.isBarChartShown = false
        }
    },
    beforeMount() {
        const url = '/history/?id=' + store.state.userId
        axios.get(url, {responseType: 'json'})
            .then(res => {
                if(res.data.status === 'ok') {
                    this.items = res.data.data
                    this.items.forEach(elem => {
                        elem.show = false
                    })
                }
                else {
                    this.errorMessage = res.data.status
                    this.isErrorModalShown = true
                }

            })
            .catch(error => {
                this.errorMessage = error
                this.isErrorModalShown = true
                console.error(error);
            });
    }
};
</script>

<style scoped>
.container {
    margin-top: 60px;
    margin-left: 45vw;
}

.history {
    margin-top: 20px;
    box-sizing: border-box;
    max-width: 1047px;
    display: flex;
    flex-direction: column;
}

.rectangle {
    width: 100%;
    height: 148px;
    background-color: rgba(255, 253, 253, 0.42);
    border: 6px solid #6FD9CD;
    display: flex;
    align-items: center;
    justify-content: space-around;
}

.description,
.data {
    font-weight: bold;
    font-size: 40px;
    text-align: center;
}

.data p{
    margin: 0;
}

img {
    width: 116px;
    height: 114px;
}

.description {
    width: 100%;
    height: 192px;
    background-color: rgba(255, 253, 253, 0.42);
    border-right: 6px solid #6FD9CD;
    border-left: 6px solid #6FD9CD;
    border-bottom: 6px solid #6FD9CD;
    display: flex;
    align-items: center;
    justify-content: space-around;
}

button {
    margin-left: 45px;
    cursor: pointer;
    width: 457px;
    height: 108px;
    background: #6FD9CD;
    border-radius: 20px;
    border: 6px #FFFDFD solid;
    text-align: center;
    color: black;
    font-size: 40px;
    font-weight: bold;
    font-family: Comfortaa;
}

.buttons {
    margin-top: 15%;
}
</style>


