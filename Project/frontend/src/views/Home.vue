<template>
  <div class="home">
    <h1>Welcome to Classbook</h1>
    <div style="height:100px;width:100%;margin-left:40%;margin-top:2%">
        <div style="float:left" class="routeDiv button"> <router-link style="font-size:16px;"  class="route" to="/login">Login</router-link> </div>
            <div  style="float:left" class="routeDiv button"> <router-link   style="font-size:16px;" class="route" to="/signup">Sign Up</router-link> </div>


    </div>
   
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
}
</script>
<style scoped>


</style>
