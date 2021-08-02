<template>
    <div class="singleDivDoc">
        <div style="float:left">
            <img  :src="require(`@/assets/${img}`)" class="docImage"/>
        </div>
          <div class="titleDiv">
             <h1> {{name}}</h1>
        </div>
         <div class="titleDiv">
             <h1> 20KB</h1>
        </div>
          <div style="height:100%;width:25%;float:left">
              <div style="height:100%;width:30%;float:left"><img  style="width:50px;height:50px" src='../assets/user7.png'/></div>
               <div style="height:100%;width:70%;float:left">
                     <h2> {{author}}  </h2>
                        <h6 style="font-size:12px;color:gray">{{date}}  </h6>
               </div>
          
        </div>
          <div style="height:100%;width:15%;float:left">
               <div class="ratingDiv">{{stars}} Stars</div>
        </div>
        <div class="titleDiv">
            <button class="button dnlwdBtn">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-download" viewBox="0 0 16 16">
                <path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z"/>
                <path d="M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3z"/></svg>
      
            </button>
                
  </div>
    <hr>
      
    </div>
</template>
<script>
export default {
      props:['name','img','author','date','stars'],
    
}
</script>
<style scoped>
.singleDivDoc{
    margin-top:3%;
    border-radius:2%;
    width:100%;
    height:10%;
    background-color: white;
}
.titleDiv{
    width:15%;float:left;
    height: 100%;
}
.docImage{
        margin-left: 14%;
    width: 150px;
    height: 150px;
    padding: 4%;
    margin-top: 2%;
    border: 2px gray solid;
}
.docImage:hover{
        margin-left: 14%;
    width: 500px;
    height: 500px;
    padding: 4%;
    margin-top: 2%;
    border: 2px gray solid;
}
.ratingDiv{
    font-weight: bold;
    text-align: center;
    float: left;
    background-color: lightblue;
    margin-top: 8%;
    border-radius: 46%;
    width: 100px;
    height: 35px;
    padding: 1%;
}
h1,h2{
    padding: 14%;
    height: 100%;
    margin-top: -9%;
}
.dnlwdBtn{
        margin-top: 13%;
    width: 60px;
}

</style>