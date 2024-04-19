<template>
    <div v-if="show" class="modal">
        <div class="modal-content">
            <span class="close" @click="closeModal">×</span>
            <p>{{ errorText }}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ErrorWindow',
    props: {
        show: {
            type: Boolean,
            required: true
        },
        errorText: {
            type: String,
            required: true
        }
    },
    methods: {
        closeModal() {
            this.$emit('close');
        }
    }
};
</script>

<style scoped>
/* Стили для модального окна */
.modal {
    display: block;
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgb(0, 0, 0);
    background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
    background-color: #fefefe;
    margin: 15% auto;
    padding: 20px;
    border: 1px solid #888;
    width: 80%;
}

.close {
    color: #aaaaaa;
    float: right;
    font-size: 50px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    color: #000;
    text-decoration: none;
    cursor: pointer;
}

p {
    font-size: 24px;
}
</style>