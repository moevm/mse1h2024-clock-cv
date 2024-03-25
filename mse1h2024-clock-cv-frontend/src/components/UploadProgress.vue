<script>
import {ref} from "vue";

export default {
  data() {
    return {
      lastActiveElement: ref(HTMLElement),
      rootElementRef: ref(HTMLElement)
    }
  },
  props: {
    to: {
      type: String
    },
    fullScreen: {
      type: Boolean
    },
    shouldCatchFocus: {
      type: Boolean
    }
  },
  methods: {
    catchFocus() {
      this.rootElementRef.value?.focus()
    },
    restoreLastFocus() {
      this.lastActiveElement.value?.focus();
    },
    storeLastActiveElement(){
      this.lastActiveElement.value = document.activeElement
    }
  },
  mounted() {
    this.storeLastActiveElement();
    if (this.shouldCatchFocus) this.catchFocus()
  },
  unmounted() {
    this.restoreLastFocus()
  }
}
</script>
<template>
  <div ref="rootElementRef" class="app-spinner app-spinner--fullscreen" tabindex="0" @focusout="catchFocus">
    <div class="app-spinner__overlay" />
    <div class="app-spinner__icon" />
  </div>
</template>

<style>
.app-spinner {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 3;
  width: 100%;
  height: 100%;
}

.app-spinner:focus {
    outline: none;
}

.app-spinner__icon {
    position: absolute;
    top: 50%;
    left: 50%;
    z-index: 1;
    width: 40px;
    height: 40px;
    background-repeat: no-repeat;
    background-size: contain;
    animation: spinnerAnimation 0.6s infinite linear;
    background-image: url("../assets/spinner-icon.svg");
}

.app-spinner__overlay {
    width: 100%;
    height: 100%;
    background-color: rgba(111, 217, 205, 0.42);
}

.app-spinner--fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
}


@keyframes spinnerAnimation {
  0% {
    transform: translate(-50%, -50%) rotate(0);
  }

  100% {
    transform: translate(-50%, -50%) rotate(360deg);
  }
}
</style>
