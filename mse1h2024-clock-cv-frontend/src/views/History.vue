<template>
    <div class="block1">
        <div class="dropdown">
            <div class="Rectangle1">
                <input type="checkbox" id="menu">
                    <div class="-hover">
                        <label for="menu" class="-arrow"></label>
                    </div>
                <div class="-list">
                    <p>Пояснение</p>
                </div>
            </div>
        </div>
        <div class="block2">
            <button class="grafknop">График</button>
            <router-link to="/result"><button class="knopreturn">Вернуться назад</button></router-link>
        </div>
    </div>
    
</template>

<script>
export default {
    name: 'HistoryComp',
}
</script>

<style scoped>

.block1{
    display: flex;
    justify-content: right;
    flex-direction: column;
}

.block2{
    display:flex;
    flex-direction: row;
    position: absolute;
    bottom: 2%;
    right: 8%;
}

.knopreturn{
    margin-left: 10%;
    text-align: center;
    color: black; 
    font-size: 40px; 
    font-family: Comfortaa; 
    font-weight: 700; 
    word-wrap: break-word;
    width: 457px; 
    height: 108px; 
    background: #6FD9CD; 
    border-radius: 20px; 
    border: 6px #FFFDFD solid;
}

.grafknop{
    width: 457px; 
    height: 108px; 
    background: #6FD9CD; 
    border-radius: 20px; 
    border: 6px #FFFDFD solid;
    text-align: center;
    color: black; 
    font-size: 40px; 
    font-family: Comfortaa; 
    font-weight: 700; 
    word-wrap: break-word;
}

.grafknop:hover{
    cursor: pointer;
    background: #0991A4;
}

.knopreturn:hover{
    cursor: pointer;
    background: #0991A4;
}

.Rectangle1{
    width: 1047px; 
    height: 148px; 
    background: rgba(255, 252.88, 252.88, 0.42); 
    border: 6px #6FD9CD solid;
    
}

.dropdown {
  display: inline-block;
  position: relative;
  margin-left: auto;
    margin-right: 4%;
    margin-top: 2%;
}

.dropdown #menu {
  display: none;
}

.dropdown .-hover {
  color: #fdac7a;
}

.dropdown .-hover > span {
  text-decoration: underline dashed;
  font-style: italic;
}

.dropdown .-arrow::after {
  content: url("../assets/down.png");
  zoom: 15%;
  background-size: 100px !important;
  width: 116px !important;
  height: 114px !important;
  font-size: 50%;
  cursor: pointer;
}

.dropdown .-list {
  display: none;
  width: calc(100%);
  box-shadow: 0 2px 3px rgba(0,0,0,.35);
  padding: 5px;
  box-sizing: border-box;
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 10;
  background: rgba(255, 252.88, 252.88, 0.42); 
  border: 6px #6FD9CD solid;
}

.dropdown .-list p {
  display: block;
  color: inherit;
}

.dropdown .-list p:hover {
  color: #fdac7a;
}

.dropdown #menu:checked ~ .-list {
  display: block;
}

.dropdown #menu:checked ~ .-arrow::after {
    content: url("../assets/up.png");
}

</style>