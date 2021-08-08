<template>
    <div style="height:200px;width:400px;background-color:white;border-radius:4%;margin-top:5%">
        <div style="padding:2%;height:30%;width:100%">

            <div style="width:30%;float:left;height:100%">
                <!-- <img src="../assets/user2.png" style="float: left;
    height: 40px;
    width: 40px;
    background: white;
    border-radius: 54%;"/> -->
       <span style="height:100%;width: 40%;float: left" >Ben Cohen</span> 
       <span style="width:40%;float:left">{{ Publishdate}}</span>    
             <span style="width:40%;float:left">{{ currentviews}}</span> 
            </div>
             
             <span style="height:100;width: 50%;float: left">{{title}}</span>
  
    
        </div>
        <hr>
    <div style="padding:2%;height:20%;width:100%">
        {{content}}</div>     
      
        <!--
        <div style="float:left;height:100%;width:10%">
            <div>{{issueNumber}}</div>
             <div>{{status}}</div>
        </div>
         <div style="float:left;height:100%;width:90%">
               <div style="width:100%;height:25%">
                   <h2>{{title}}</h2>
                   <p> {{Publishdate}} {{currentviews}} views </p>
                   
               </div>
                <hr>
                  <div style="margin-top:13%;width:100%;height:75%">
                  {{content}}
                     
                  </div>
                  <div><input type="text"></div>
                
         </div>

             <div style="height:10%:width:100%;background-color:#e9ecef">
                 <hr>
             <input style="height:100%;width:100%" type="text">
         </div>    
         -->
    
        <div style="padding:2%;height:10%;width:100%"><button class="button">Reply</button></div>
    </div>
    
</template>
<script>
export default {
     props:['title','content','Publishdate','currentviews','issueNumber','status'],
   
   
    }





</script>
<style >
    .issueMainBox{
        padding:3%;
        margin-top:12%;
        overflow: auto;
        width:400px;
        background-color: #e9ecef;
        webkit-box-shadow: 10px;
        box-shadow: 10px 10px 16px #000000;
        height:150px
    }
</style>