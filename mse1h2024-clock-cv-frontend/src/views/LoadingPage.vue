<template>
  <div class="explanation">
    Необходимо нарисовать циферблат и
    расположить на нем цифры согласно
    общепринятой картине часов в 12-часовом
    формате. На изображенном циферблате
    необходимо указать определенное время.
  </div>
  <div class="container">
    <div class="clock">
      <TheClock :hours="2" :minutes="45"></TheClock>
      <br>
      <span class="clock-text">Образец полученного циферблата</span>
    </div>
    <div class="buttons">
      <input type="file" id="upload-input" ref="file"
               v-on:change="handleFileUpload()" hidden/>
      <button class="upload-button">
        <label for="upload-input" class="download-label">
           Загрузить
        </label>
      </button>
      <br>
      <a href="../assets/fon1.jpg" download="sample">
        <button class="download-button">Скачать макет</button>
      </a>
    </div>
  </div>
  <br>
  <button id="result-button" disabled v-on:click="submitFile()">Результат</button>
  <UploadProgress v-if="isLoading"></UploadProgress>
</template>

<script>
import axios from "axios"
import TheClock from "@/components/TheClock.vue";
import store from "@/store";
import router from "@/router";
import UploadProgress from "@/components/UploadProgress.vue";

export default {
  name: 'LoadingPage',
  components: {UploadProgress, TheClock},
  data(){
    return {
      file: '',
      isLoading: false
    }
  },
  methods: {
    handleFileUpload(){
      this.file = this.$refs.file.files[0]
      document.getElementById("result-button").removeAttribute("disabled")
    },
    submitFile(){
      this.isLoading = true
      let formData = new FormData();
      formData.append('file', this.file);
      axios.post( '/upload', formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
      ).then(function(res){
        store.state.result = res.data.result
        store.state.description = res.data.description
        router.push('/result')
      }).catch(function(error){
          console.log(error);
      });
    }
  }
}
</script>

<style scoped>
.explanation {
  width: 65vw;
  margin-left: 28vw;
  margin-top: 4%;
  font-size: 2.5vw;
  text-align: justify;
}

.container {
  width: 62vw;
  height: 35vw;
  background-color: rgb(255,253,253, 0.42);
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

.upload-button{
  margin-top: 8.85vw;
}

.download-button{
  margin-top: 5.42vw;
}

#result-button{
  margin-top: 0.22vw;
  margin-left: 45.44vw;
  font-weight: 700;
}

button{
  width: 25.89vw;
  height: 7.13vw;
  background-color: #6FD9CD;
  border-radius: 1.32vw;
  border: 0.52vw solid #FFFDFD;
  font-size: 2.64vw;
  font-family: "Comfortaa", sans-serif;
}

button:hover{
  background-color: #0991A4;
  cursor: pointer;
}

.download-label:hover{
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