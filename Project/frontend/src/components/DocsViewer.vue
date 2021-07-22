<template>
    <div class="docsDiv">
    <div style="border:2px solid black;height:10%;width:98%;background-color:#e9ecef"> My Recent docuemnts</div>
       <RecDocument thumbNailsrc="doc2.png"></RecDocument>
          <RecDocument thumbNailsrc="doc3.png"></RecDocument>
             <RecDocument thumbNailsrc="doc4.png"></RecDocument>
                <RecDocument thumbNailsrc="doc1.png"></RecDocument>
                 <RecDocument thumbNailsrc="doc1.png"></RecDocument>
                    <RecDocument thumbNailsrc="doc1.png"></RecDocument>
                       <RecDocument thumbNailsrc="doc1.png"></RecDocument>
                          <!-- <RecDocument thumbNailsrc="doc1.png"></RecDocument> -->
                
       

    </div>
</template>
<script>
import RecDocument from '../components/RecDocument.vue'
export default {
    components:{
        RecDocument
    }
}
</script>
<style >
.docsDiv{
       margin-top: 5%;
    margin-left: 3%;
    height: 240px;
    width: 100%
}
</style>