<template>
  <div class="home">
    <p>Hey there</p>
    <p>I have been tapped {{ count }}</p>
    <button @click="increment">Tap Me</button>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data() {
    return {
      count: 0,
    }
  },
  methods: {
    increment() {
      this.count += 1;
    }
  }
}
</script>
