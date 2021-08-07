<template>

  <div class="mx-auto mainCommentSection">

    
    <div  class="outerissuesDiv">
      <div>
        <div class="searchissuebar">
        <span class="issuesbarspan">
          <!-- <label>Search Course Issues</label> -->
          <input placeholder="Search Course Issues" type="text" id="search-issues" class="form-control" value>
        </span>
        <span class="input-group-btn searchbuttonSpan">
            <button type="button" class="searchButton btn btn-secondary">
              <span></span>
            </button>
          </span>
      </div>
      <div class="issusFiltersDiv">
        <section style="margin-left:80px">
          <div  class="dropdown btn-group fildiv">
            <button class="dropdown-toggle btn btn-default">All Issues</button>
          </div>
          <div class="dropdown btn-group fildiv">
             <button class="dropdown-toggle btn btn-default">Top Rated Issues</button>
          </div>
          <div  class="dropdown btn-group fildiv">
             <button class="dropdown-toggle btn btn-default">Only From Today</button>
          </div>
           
        </section>
      </div>
      <div style="font-weight:bold;font-size:16px;">All Issues About this document (233)</div>
      <!--  outer container for issues -->
      <div ref="issues" style="overflow:auto">
      
  
    </div>
    <div v-for="comment in commentsData" :key="comment.profile">
       <DocumentIssue :title="comment.title" :content="comment.content" :id="comment.id" :author="comment.author" :img="comment.profile"></DocumentIssue>
    </div>


            <div  ref="avc" style="margin-top:5px;padding:5px" class="mx-auto" ><p style="border:none;background-color:white;font-size:16px;font-weight:bold">Add a new issue</p></div>


        <AddIssueBox ref="issueBox"></AddIssueBox>
        <div  class="issuecontainerMenu"><button @click="addNewIssue()" style="width:200px;" class="submit button">Submit new Issue</button></div>

     
      <!-- <IssuesReplies></IssuesReplies> -->
      </div>
      
    </div>
  </div>
</template>
<script>
//'id','title','author','date','content','img','rate','coms
 import DocumentIssue from '../Comments/DocumentIssue.vue'
  import AddIssueBox from '../Comments/AddIsueBox.vue'
    import Vue from 'vue'
    import Vuetify from 'vuetify'
import { VIcon } from 'vuetify/lib'
    Vue.use(Vuetify)
//  import IssuesReplies from '../components/IssuesReplies.vue'
export default {
  
   components:{
  // IssuesReplies,
  AddIssueBox,DocumentIssue
 },
 data(){
   return{
     //to be removed static data for intro
     commentsData:[{id:1,author:"David Cohen",profile:"pic2.jpg",title:"Epic Content",content:"This Paper really helped me study for my last test"},
                    {id:2,author:"Shir Ben Harush",profile:"pic3.jpg",title:"Good Paper",content:"High Quality Well Done"},
                    {id:3,author:"Dudi Bar",profile:"pic4.jpg",title:"Not so good , missing info",content:"the important proofs are not inside"},
                    {id:4,author:"Alon Vered",profile:'sample.jpg',title:"I was hoping to find answers here.. , missing info",content:"Can't read it. too long and not clear ,you shoud rank this low!"}],                                        
      //this should be updated with VueX
      LastissueID:0,
      author:"Chen Ben Ezra",
      profile:'sample.jpg'
   }
 },
 methods:{
   getDate(){
     var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();

      today = mm + '/' + dd + '/' + yyyy;
      return today
  
   },
   addNewIssue(){
     this.LastissueID=this.LastissueID+1
     console.log(this.$refs)
     var issueData=this.$refs["issueBox"]
     issueData=issueData.submitnewIssue()
   
         var ComponentClass = Vue.extend(DocumentIssue,VIcon)
            var newDocumentIssue = new ComponentClass(
                {
                propsData: {title:issueData.issueTittle,
                    content:issueData.content,
                    date:this.getDate(),
                    author:this.author,
                    rate:0,
                    coms:0,
                    img:this.profile,
                    id:this.LastissueID
                   
    }}
            )

            //newDocumentIssue.$el["id"]="issue"+this.LastissueID.toString()

        newDocumentIssue.$mount() // pass nothing
        this.$refs['issues'].appendChild(newDocumentIssue.$el)
   }
 }
}
</script>
<style scoped>


.mainCommentSection{
  display: block;
 margin-top:10%;
}

.fildiv{
 float:left;border: 1px solid black;margin-left:20px;margin-top:20px;
}
.buttonIssueFilter{
  position: relative;
    float: left;
    width: 100%;
    text-align: left;
    padding-right: 32px!important;
    padding-top: 9px;
    padding-bottom: 9px;
    font-size: 16px;
    margin-left:50px;
    font-weight: 400;
    line-height: 1.5em;
    color: #3e4143;
    /* border-color: #6a6f73; */
    background-color: transparent;
    border: 1px solid #1c1d1f;
}
.outerissuesDiv{

  /* width: 1500px; */

    padding: 0 159px;
}
.sectionissues{
  margin-top: 8px;
    margin-right: 8px;
    flex: 1;
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
.issusFiltersDiv{
  display: flex;
    flex-wrap: wrap;
    width: 100%;
    padding-bottom: 32px;
}
.searchissuebar{
      display: flex;
    flex-direction: row;
    align-items: center;
    padding-top: 32px;
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

.issuesbarspan{
  font-size: 14px;
    font-weight: 400;
    line-height: 1.43em;
    width: 100%;
}
  input{
     position: relative;
    z-index: 2;
    float: left;
    width: 100%;
    margin-bottom: 0;
    background-color: #f7f9fa;
    border-color: #fff;
}
.searchbuttonSpan{
  display: table-cell;
  position: relative;
    font-size: 0;
    white-space: nowrap;
    width: 1%;
    white-space: nowrap;
    vertical-align: middle;
    box-sizing: border-box;
    margin: 0;
    font-weight: 400;
    line-height: 1.43em;
    padding: 0;




}
.searchButton{
  background-color: #1c1d1f;
    color: #fff;
    border-left: none;
    border-color: #6a6f73;
    border-bottom-left-radius: 0;
    border-top-left-radius: 0;
    display: inline-block;
    margin-bottom: 0;
    font-weight: 700;
    text-align: center;
    vertical-align: middle;
    touch-action: manipulation;
    cursor: pointer;
    background-image: none;
    border: 1px solid transparent;
    white-space: nowrap;
    padding: 11px 12px;
    font-size: 15px;
    line-height: 1.35135;
    border-radius: 0;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
}
.innerspanButton{
  vertical-align: -8%;
  font-family: udemyicons!important;
    speak: none;
    font-style: normal;
    font-weight: 400;
    font-variant: normal;
    text-transform: none;
    line-height: 1;
    -webkit-font-smoothing: antialiased;
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
  


</style>