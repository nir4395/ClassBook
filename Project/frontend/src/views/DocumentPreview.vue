
<template>
  <div class="mainDocumentDiv">
       
      <PDFJSViewer :path="`${path}`" :fileName="`${name}`"/>
      <CommentsSection></CommentsSection>
  </div>

  
</template>
<script>


import CommentsSection from '../components/Comments/CommentsSection.vue'
import PDFJSViewer from '../components/PDFJSViewer.vue'




export default {
 components:{
  //  DocsViewer,
   CommentsSection,

    // Issue,
    // RankModal,
    // Modal
    PDFJSViewer

 },
 

 data(){
   return{
        urlImg:'book.jpg',
        issues:[],
         VIEWS_FILTER:10,
        lastIssueNumber:1,
       isModalVisible: false,
       isRateDocVisable:false,
        name: 'compressed.tracemonkey-pldi-09.pdf', //change which pdf file loads
      path: '../public/lib/pdfjs-2.9.359-dist/web/viewer.html' //path of the PDF.js viewer.html
   }

 },
 
 }
</script>
<style>
 

.previewImg{
  margin-left: -15%;
    height: 100px;
    float: left;
    width: 100px;
    margin-top: 2%;
    position: absolute;
   
}
  .mainDocumentDiv{
    display: flex;
   flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 70%;
  /* height: 79vh; */
  min-width: 250px;
  }
  .documentArea{
  
    
    padding: 3%;
    height: 100%;
    width: 75%;
    float:left;
    
  
  }
  .reviewsBox{
    width:100%;
    height:11%;
    background-color: lightgrey;
  }
  .checked {
  color: orange;
}
.embedZone{
 margin-top: 14%;
    height: 75%;
    width: 100%;
}
.commentsArea{
  padding: 3%;
    height: 100%;
    width: 25%;
    float: left;
    background-color: #e9ecef;
    margin-top: 3%;

}
.addcommentDiv{
  height:10%;
  background-color: lightgrey;
  width:100%;
  
}
body{
  font-family:Helvetica
}
.issuesArea{
  height: 75%;
    width: 100%;
    overflow: auto;

}



</style>