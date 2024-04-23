<template>
    <div class="modalchart"> 
        <span class="close" @click="closeModal"><img src="../assets/close.png" class="closeknop"></span>
            <div class="context">
            <Bar
                id="my-chart-id"
                :options="chartOptions"
                :data="chartData"
            />
        </div>
    </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
    name: 'BarChart',
    components: { Bar },
    props: {
        arr: {
            type: Array,
            required: true
        }
    },
    data() {
        return {
            chartData: {
                labels: [],
                datasets: []
            },
            chartOptions: {
                responsive: true
            }
        }
    },
    beforeMount() {
        this.chartData.labels = this.arr.map(elem => elem.date)
        this.chartData.datasets = [{ label: "Количество баллов",backgroundColor: '#6FD9CD', data: this.arr.map(elem => elem.points)}]
    },
    methods: {
        closeModal() {
            this.$emit('close');
        }
    }
}
</script>

<style scoped>
.modalchart{
    display: block;
    position: fixed;
    z-index: 1;
    left: 5%;
    top: 2%;
    width: 90%;
    height: 95%;
    overflow: auto;
    background-color: #fefefe;
    border: 6px solid #6FD9CD;
}

.context{
    width: 90%;
    height: 89%;
    margin: auto auto;
}

.closeknop {
    width: 60px;
    height: 60px;
    cursor: pointer;
}

</style>