<template>
    <div class=itemDiv>
    
            <div id="box">
                <img style="padding:7%;height:100%;width:100%"  :src="require(`@/assets/${img}`)"/>
            </div>
            <div style="border:2px;black;height:20%;width:100%;background-color:white">
                <h2 style="text-align:left;font-weight:bold">{{name}}</h2>
                <div>
                    <div style="background-color:white;float:left;background-image:none"> <img style="height:30px;width:30px" 
                       src='../assets/user3.jpg'/></div>
                   
                     <h5 style="    margin-top: 2%;
    float: left;
    text-align: left;
    font-weight: bold;
    color: gray;
    margin-left: 5%;
}">{{author}} * {{date}} {{stars}} stars</h5>
                </div>
               
                </div>
       
            <!-- <img style="width:50px;height:50px;float:left" src='../assets/doc1.png'> -->
            
     
      
         
    </div>
    
</template>
<script>
export default {
    props:['name','img','author','date','stars'],
    methods:{
      
        
    }
}
</script>
<style scoped>
.itemDiv{
   width:400px;
   padding: 2%;
   height:500px;
   border-radius: 12%;
   float: left;
   
    
    
}

.itemDiv:hover{
   width:800px;
   padding: 2%;
   height:1000px;
   border-radius: 12%;
   float: left;
   
    
    
}
#box{
    height:80%;width:100%;background-color:#CAF0F8;border-radius:2%
}
</style>