<template>
    <div style="width;1000px;height:200px;background-color:white">



        
             <div style="width:80%;border-radius:7%;border:5px gray dotted;padding:4%;background:lightblue">
        <button @click="fill" class="button">Fill</button>
       <div id='myDivId'>
    <div  class="progress"></div>
    <div class="content">
        DIV
    </div>
</div>
    </div>
    </div>
   
</template>
<script>
export default {
  
    methods:{
        fill(){
            document.getElementsByClassName("progress")[0].animate({ width: '100%' }, 10000);
        },
            Load(){
                console.log("clicked")
                var loadingBox=document.getElementById("loadingBox")
                var width = parseInt(loadingBox.style.width,10); // always use a radix
              
                setInterval(() => {
                      if(width<100){
                      width=width+5
                      
                      loadingBox.style.width=width.toString()+"%";      
                      }
                      else{
                          clearInterval()
                      }
                }, 100);
            }
    },
  
}
</script>
<style>
.content{
    z-index:9;
    position:relative;
}
#myDivId{ color:white; padding:10px; overflow:hidden; position:relative;}
.progress{
    z-index:1;
    width:0px;
    height:100%;
    position:absolute;
    background:blue;
    left:0px;
    top:0px;
}
.loadDiv{
      margin-left: 6%;
    height: 70%;
    width: 88%;
    position: absolute;
    border: 5px dotted lightgray;
    border-radius: 12%;
    padding: 5%;
    margin-top: 4%;
}
    .filling{
        height: 100%;
        background-color:turquoise;
 
    }
</style>