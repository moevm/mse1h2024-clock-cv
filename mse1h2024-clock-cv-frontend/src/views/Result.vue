<script>
import modal from '../components/ModalWindow.vue'
export default {
    name: 'ResultComp',
    components: {
      modal,
    },
    data () {
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
    <div class="block1">
        <router-link to="/loading"><button class="repetknop">Повторить тест</button></router-link>
        <button class="historyknop">История тестирований</button>
    </div>
    <div class="Rectangle1">
        <p class="text1">Имя пользователя:<br/><span class="text1">...</span></p>
        <p class="text2">Количество баллов:<br/><span class="number">{{ $store.state.result }}</span></p>
    </div>
    <div>
        <button class="detailknop" @click="showModal">Подробнее</button>
        <div class="text3">Предоставленная информация не явлеяется заменой профессиональной медицинской консультации. Рекомендуется обратиться к специалисту для получения точного диагноза и рекомендаций.</div>
    </div>
</template>

<style scoped>
.block1{
    display: flex;
    flex-direction: row;
    gap: 2%;
    justify-content: right;
}

.repetknop{
    width: 457px; 
    height: 108px; 
    background: #6FD9CD; 
    border-radius: 20px; 
    border: 6px #FFFDFD solid;
    text-align: center; 
    font-family: Comfortaa;
    color: black; 
    font-size: 40px;  
    font-weight: 400; 
    word-wrap: break-word;
    margin-top: 12%;
}

.repetknop:hover{
    cursor: pointer;
    background: #0991A4;
}

.historyknop{
    width: 605px; 
    height: 108px; 
    background: #6FD9CD; 
    border-radius: 20px; 
    border: 6px #FFFDFD solid;
    text-align: center; 
    color: black; 
    font-size: 40px; 
    font-family: Comfortaa; 
    font-weight: 400; 
    word-wrap: break-word;
    margin-top: 2.85%;
}

.historyknop:hover{
    cursor: pointer;
    background: #0991A4;
}

.Rectangle1{
    width: 1097px; 
    height: 294px; 
    background: #FFFCFC; 
    border-radius: 20px; 
    border: 8px #6FD9CD solid;
    margin-left: auto;
    margin-right: 0;
    margin-top: 2%;
}

.text1{
    text-align: center; 
    color: black; 
    font-size: 40px; 
    font-family: Comfortaa; 
    font-weight: 400; 
    word-wrap: break-word;
}

.text2{
   text-align: center;
   color: black; 
   font-size: 50px; 
   font-family: Comfortaa; 
   font-weight: 400; 
   word-wrap: break-word;
   margin-top: -2%;
}

.number{
    color: black; 
    font-size: 80px; 
    font-family: Comfortaa; 
    font-weight: 400; 
    word-wrap: break-word;
}

.detailknop{
    width: 457px; 
    height: 108px; 
    background: #6FD9CD; 
    border-radius: 20px; 
    border: 6px #FFFDFD solid;
    margin-top: 2%;
    text-align: center; 
    color: black; 
    font-size: 50px; 
    font-family: Comfortaa;
    font-weight: 400; 
    word-wrap: break-word;
    position:relative;
    right: -60%;
}

.detailknop:hover{
    cursor: pointer;
    background: #0991A4;
}

.text3{
    width: 963px; 
    height: 76px; 
    text-align: justify; 
    color: black; 
    font-size: 25px; 
    font-family: Comfortaa; 
    font-weight: 400; 
    word-wrap: break-word;
    position:fixed;
    right: 5%;
    bottom: 5%;
    z-index: -1;
}
</style>