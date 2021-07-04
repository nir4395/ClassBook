
<template>
  <div class="mainDocumentDiv">
       <img class="previewImg" src="../assets/doc.png" >
        <div style="font-size:55px" class="jumbotron jumbotron-fluid">Document Preview
               

        </div>
       <div style="height:70%;width:100%;">
         <div class="documentArea">
        <div class="reviewsBox">
          
            <div class="jumbotron jumbotron-fluid">
  <div class="container">
    <h1>Virtual Memory</h1>
    <div style="margin-left:2%;width:400px;height:50px;float:left">
      <div style="float:left">Rating: 4/5</div> 
      <div style="margin-left:2%;float:left">
        <span class="fa fa-star checked"></span>
            <span class="fa fa-star checked "></span>
            <span class="fa fa-star checked"></span>
            <span class="fa fa-star checked"></span>
            <span class="fa fa-star"></span>
        </div>
         <Modal
      v-show="isModalVisible"
      @close="closeModal"
    /> 
    <RankModal  v-show="isRateDocVisable" @close="closeRateDocModal" ></RankModal>
      

      <button class="button" @click="OpenRatingDetails" style="margin-left:10%;float:left">Rating Details</button> 

    </div>
    <button  @click="OpenDocRateModal" class="button" style="float:left">Rank Document</button>
         
  </div>
</div>

        </div>
        <div class="embedZone">
            <embed style="height:105%;width:100%" src="http://www.africau.edu/images/default/sample.pdf">
        </div>
        <div></div>
      </div>
      <div   class="commentsArea">
        <div style="height:10%;width:100%;padding:5%;">
           <div class="btn-group btn-group-toggle" role="group" aria-label="Basic example">
    <button  @click="showOAllIssues" style="border-radius:15%;" type="button" class="btn btn-secondary">All</button>

  <button @click="showOnlyNewIssues" style="border-radius:15%;" type="button" class="btn btn-secondary">New</button>
  <button @click="showOnlyOldIssues"  type="button" class="btn btn-secondary">Old</button>
  <button  @click="showPopIssues" style="border-radius:15%;"  type="button" class="btn btn-secondary">Votes</button>
 
</div>
        </div>
        <div  ref="issues" id="issuesDiv" class="issuesArea">
           
        </div>
        
          <div class="addcommentDiv">
          <div>
            
                          <input type="text"   value="Issue Title" style="float:left;width:380px"  id="title">

             <textarea  style="float:left" id="commentText" class="form-control" aria-label="With textarea"></textarea>
          </div>
          
            <button @click="AddComment"  class="button">Add A Comment</button>
            <img :src="urlImg"/>
            <div class="type-3">
  
  </div>


        </div>
        
       
    
       
    
      </div>
       </div>
       
       <div style="height:20%;width:100%;">
            <DocsViewer></DocsViewer>
       </div>
      
  </div>
  
</template>
<script>
 import Issue from '../components/Issue.vue'
import RankModal from '../components/RankModal.vue'
import DocsViewer from '../components/DocsViewer.vue'
import Modal from '../components/Modal.vue'
// import { createApp,defineComponent } from 'vue'
 import Vue from 'vue'



export default {
 components:{
   DocsViewer,
    // Issue,
    RankModal,
    Modal
 },
 

 data(){
   return{
        urlImg:'book.jpg',
        issues:[],
         VIEWS_FILTER:10,
        lastIssueNumber:1,
       isModalVisible: false,
       isRateDocVisable:false
   }
 },
 methods:{

   showOAllIssues(){
      this.issues.forEach(x=>{
      
         var element=document.getElementsByClassName("issueDiv")[x.$props["issueNumber"]-1]
         element.style.display="block"
      })
   },
    ShowIssue(issue) {
        console.log(issue)
   },
   showOnlyNewIssues(){
     //cancel last filter first
     this.showOAllIssues()
     this.issues.forEach(x=>{
       console.log(x)
       if(x.$props["status"]!=="New"){
         var removeElement=document.getElementsByClassName("issueDiv")[x.$props["issueNumber"]-1]
         removeElement.style.display="none"
        // var elem=document.getElementById("issuesDiv")
         //elem.removeChild(removeElement)

       //  document.getElementById("issuesDiv").removeChild(x.$parent)
       }
       console.log(x.$props["status"])
     })
   },
   showOnlyOldIssues(){
       //cancel last filter first
     this.showOAllIssues()
     this.issues.forEach(x=>{
       console.log(x)
       if(x.$props["status"]=="New"){
         var removeElement=document.getElementsByClassName("issueDiv")[x.$props["issueNumber"]-1]
         removeElement.style.display="none"
        // var elem=document.getElementById("issuesDiv")
         //elem.removeChild(removeElement)

       //  document.getElementById("issuesDiv").removeChild(x.$parent)
       }
      
     })
   },
   showPopIssues(){
      //cancel last filter first
     this.showOAllIssues()
     this.issues.forEach(x=>{
       console.log(x)
       var views=x.$props["currentviews"]
       views=parseInt(views,10)
       if(views<this.VIEWS_FILTER){
         var removeElement=document.getElementsByClassName("issueDiv")[x.$props["issueNumber"]-1]
         removeElement.style.display="none"
        // var elem=document.getElementById("issuesDiv")
         //elem.removeChild(removeElement)

       //  document.getElementById("issuesDiv").removeChild(x.$parent)
       }
       console.log(x.$props["status"])
     })
   },

   closeModal() {
        this.isModalVisible = false;
      },
    closeRateDocModal(){
        this.isRateDocVisable=false
    },
   OpenRatingDetails(){
              this.isModalVisible = true;

   },
    OpenDocRateModal(){
              this.isRateDocVisable = true;

   },
   AddComment(){





var issueTitle=document.getElementById("title").value
var issueContent=document.getElementById("commentText").value
const div = document.createElement('div');
div.className="issueDiv"
var status="New"
var views="1"
var date=new Date()
//debug purpose for comment filter
if((this.lastIssueNumber+1)%2==0){
    status="Old"
  
}
if((this.lastIssueNumber+1)%3==0){
    views="134"
  
}
if((this.lastIssueNumber+1)%5==0){
     date=new Date(2015, 4, 2, 13, 45, 0, 0)
   
}
/*
this.$refs.issues.appendChild(div);
 var comp= createApp(Issue,{title:issueTitle,
                    content:issueContent,
                    Publishdate:date,
                    issueNumber:this.lastIssueNumber,
                    currentviews:views,
                    status:status}).mount(div)
  this.lastIssueNumber=this.lastIssueNumber+1
  this.issues.push(comp)

  */

     var ComponentClass = Vue.extend(Issue)
      var newIssue = new ComponentClass({
    propsData: {title:issueTitle,
                    content:issueContent,
                    Publishdate:date.getHours().toString()+":"+date.getMinutes().toString(),
                    issueNumber:this.lastIssueNumber,
                    currentviews:views,
                    status:status

    }})
        newIssue.$mount() // pass nothing
        this.$refs.issues.appendChild(newIssue.$el)
              
 }

 }
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
    width:2000px;
    height:1000px;
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