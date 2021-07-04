<template>
<div class="openMenu" id="main">

    <div style="width:50%;height:100%;float:left">
        <img  style="borse;" src="src\assets\exams.jpg" alt="Avatar"/></div>
    <span style="width:50%;float:left;font-size:30px;cursor:pointer;font-family:Verdana;height:100%" @click="openNav()"> menu</span>

  <div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" @click="closeNav()">&times;</a>
  <a href="#">Home</a>
  <a href="#">My Courses</a>
  <a href="#">Contact Us</a>
  <a href="#">Upload A document</a>
    <a href="#">Settings</a>
</div>
</div>
  

</template>
<script>

 


export default {
    methods:{
    openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
},
 closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
}
}
}

</script>
<style>
   .sidenav {
  height: 100%;
  width: 0;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: #111;
  overflow-x: hidden;
  transition: 0.5s;
  padding-top: 60px;
}

.sidenav a {
  padding: 8px 8px 8px 32px;
  text-decoration: none;
  font-size: 25px;
  color: white;;
  display: block;
  transition: 0.3s;
}

.sidenav a:hover {
  color: #f1f1f1;
}

.sidenav .closebtn {
  position: absolute;
  top: 0;
  right: 25px;
  font-size: 36px;
  margin-left: 50px;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
.openMenu{
   transition: margin-left .5s;
  padding: 16px;
        background-color: rgb(155, 155, 147);
        height: 100px;
    margin-top: -36%;
    margin-left: -69%;
    color: white;
}
</style>