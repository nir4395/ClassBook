<template>
<div>
  <h1>We're Sorry!</h1>
  <h2 class="mx-auto">we couldn't find this page 😢</h2>
  <p>we are still learning how to solve this issue (we learn with ClassBook so we will probably fix this problem soon), want to study with ClassBook too?</p>
  <v-btn
    color="primary"
    elevation="5"
    @click="goToHome()"
  >Go To Homepage</v-btn>
</div>
</template>

<script>
export default {
methods:{
  goToHome(){
    this.$router.push('/')
  }
}
}
</script>

<style scoped>
h1{
  font-size: 10vw;
  line-height: 1em;
  margin-bottom: 5vh;
  position: relative;
  color:cornflowerblue;
}
h2{
  font-size: 1.5em;
  margin-bottom: 20px;
  text-transform: uppercase;
  color: #000;
  font-size: 2em;
  max-width: 600px;
  position: centered;
}
p{
  font-size: 1.2em;
  color: #0d0d0d;
}
</style>