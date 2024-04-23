<template>
    <span class="close" @click="closeModal">×</span>
    <Bar
        id="my-chart-id"
        :options="chartOptions"
        :data="chartData"
    />
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
        this.chartData.datasets = [{ data: this.arr.map(elem => elem.points)}]
    },
    methods: {
        closeModal() {
            this.$emit('close');
        }
    }
}
</script>