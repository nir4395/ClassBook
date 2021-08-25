<template>
    <div class="mx-auto notfound">
        <div class="notfoundText">
           
            <h1 class="headerText">Sorry!</h1>
            <h2 style="padding:300px;" class="subHeaderText">Could not load this page</h2>
              
        </div>
         <a class="goback">RETURN TO HOMEPAGE</a>
         
    </div>
    
</template>
<style scoped>
.notfound{
     position: relative;
    height: 100vh;
}
.notfoundText{
        max-width: 520px;
    width: 100%;
    line-height: 1.4;
    text-align: center;

}
.subHeaderText{
    
        font-size: 28px;
    font-weight: 400;
    text-transform: uppercase;
    color: #211b19;
 
    padding: 10px 5px;
    margin: auto;
    display: inline-block;
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
}
.headerText{
    /* font-family: montserrat,sans-serif; */
    font-size: 136px;
    font-weight: 200;
    margin: 0;
    color: #211b19;
    text-transform: uppercase;
    position: absolute;
    left: 50%;
    top: 50%;
    -webkit-transform: translate(-50%,-50%);
    -ms-transform: translate(-50%,-50%);
    transform: translate(-50%,-50%);
}
.goback{
    font-family: montserrat,sans-serif;
    display: inline-block;
    font-weight: 700;
    text-decoration: none;
    color: #fff;
    text-transform: uppercase;
    padding: 13px 23px;
    background: #1985A1;
    font-size: 18px;
    -webkit-transition: .2s all;
    transition: .2s all;
}
</style>