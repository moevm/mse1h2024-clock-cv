<template>
  <img src="../assets/clock_face.png" alt="no clock" class="clock-face">
  <img src="../assets/clock_arrow.png" alt="no arrow" id="clock-arrow-minutes">
  <img src="../assets/clock_arrow.png" alt="no arrow" id="clock-arrow-hours">
</template>

<script>
export default {
  name: 'TheClock',
  props: {
    hours: {
      type: Number,
      required: true
    },
    minutes: {
      type: Number,
      required: true
    }
  },
  mounted() {
    const hoursArrow = document.getElementById('clock-arrow-hours')
    const minutesArrow = document.getElementById('clock-arrow-minutes')
    const hourAngle = (this.hours + this.minutes/60) * 30 - 90
    const minuteAngle = this.minutes * 6 - 90
    minutesArrow.style.transformOrigin = `0 50%`
    minutesArrow.style.transform += `translate(100%, -345%) rotate(${minuteAngle}deg)`
    hoursArrow.style.transformOrigin = `0 50%`
    hoursArrow.style.transform += `translate(0%, -345%) rotate(${hourAngle}deg)`
  }

}
</script>

<style scoped>
.clock-face {
  width: 100%;
}

#clock-arrow-minutes {
  width: 35%;
  position: relative;
}

#clock-arrow-hours {
  width: 35%;
}
</style>