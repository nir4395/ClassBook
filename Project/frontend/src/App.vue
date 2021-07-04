<template>
  <div  id="app">
        <div style="height:150px;width:1000px;margin-left:40%;margin-top:3%">
             <div style="margin-left:2%;margin-top:2%;height:100%;float:left;font-family:monospace;font-size:44px">ClassBook</div>
            <img style="margin-left:3%;float:left" src="./assets/large_studentsmarts.png">

      </div>
      <hr>
    <div class="navDiv" id="nav">
   
      <div class="routeDiv"><router-link class="route"  to="/">Home</router-link> </div>
      
    <div class="routeDiv"> <router-link  class="route" to="/about">About</router-link> </div>
     <div class="routeDiv">    <router-link class="route"  to="/doc"> Document Preview</router-link> </div>
   <!--online Fictive now-->
      <div class="routeDiv">    <router-link class="route"  to="/selection"> Document Selection</router-link> </div>
    

   
    </div>
    <router-view/>
   
  </div>
</template>
<script>
export default {
  data(){
    return{
      Logo:'../assets/pdf.png'
    }
  }
}
</script>
<style>
#app {
  font-family: monospace;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
.route{
  font-size: 33px;
    color:rebeccapurple;
}
.routeDiv{
  float: left;
  height:100%;
  width:20%;
  margin-left: 5%;
}
.navDiv{
  height: 150px;
    width: 100%;
    margin-left: 4%;
}
</style>
