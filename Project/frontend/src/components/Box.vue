<template>
    <div class="shadow box">
         <div class="boxText">{{boxText}}</div>
    
        <img class="imageinBox" :src="require(`@/assets/${imgsrc}`)">
       
    </div>
</template>
<script>
export default {
    props:['boxText','imgsrc'],
   
 

}

</script>

<style>
    .imageinBox{
            margin-top:10%;
           width:100px;
            height: 100px;
    }
    .box{
        height: 200px;
        width:200px;
        background-color:#CAF0F8 !important;
        border-radius: 25%;
        
        
    }
    .boxText{
        font-size:24px;
        font-weight: bold;
        font-family: Verdana;
    }
</style>