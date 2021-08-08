<template>
     <div class="outerIssuesContainer">
      <!--  inner container for issues -->
            <div class="innerIssuesContainer">
                
       
                <div class="issueDiv">
                    <div><img class="issueIcon" height="36"  width="36" :src="require(`@/assets/${img}`)">  {{author}}</div>
                    <div  :id="issueID" class="innerIssueDiv">
                      <div class="innerIssueDivData">
                        <div class="contentissueDiv"><h4 class="issueDivText">
                           
                                {{title}}
                          
                            </h4>
                             <div class="issueContent"> {{content}} </div>
                            </div>
                           
                        <div class="ratingDivIssue">
                            <div class="ratings">
                                <div class="ratingValue">{{rating}}</div>
                                <span class="gapSpan"></span>
                                <button class="btn starUnMarked"><img  height="20px" width="20px" src="https://img.icons8.com/fluency/48/000000/star.png"/></button>
                            </div>
                             <div class="ratings">
                                <div  style="margin-right: 4px; padding: 2px;" class="ratingValue">{{comments}}</div>
                                <!-- <span class="gapSpan"></span> -->
                               
                                <button  style="background-color:white;border:none;margin-right:3px;" :id="commentsID" class="commentsOnIt"  @click="openReplies()">
                                 
                                       <img  src="https://img.icons8.com/office/16/000000/speech-bubble-with-dots.png"/>
                                     <!-- <v-icon>chat</v-icon> -->
                                </button>
                            </div>
                        </div>
                     </div>
                    
                      
                     <!-- <Reply></Reply> -->
                    </div>
                   
                </div>
                 <div class="issueDiv">
                   <div>
                      <div style="margin-top:-45px;float:left"><img class="issueIcon" height="36"  width="36" :src="require(`@/assets/${imgReply}`)"></div>
                      <div style="margin-left:50px;float:left" ><input style="margin-top:-34px;width:1000px" :id="replyInputID" @keypress="createNewReply($event)"  maxlength="255" placeholder="Reply Here" class="replyInput form-control"></div>

                     </div>
                   
                </div>
                 
                 
            </div>


      </div >
</template>
<script>
 import Reply from '../Comments/Reply.vue'
     import Vuetify from 'vuetify'

   import Vue from 'vue'
   Vue.use(Vuetify)
export default {
     props:['id','title','author','date','content','img','rate','coms'],
    // components:{Reply},
     data(){  
   return{
       //to be changed later
       replyAuthor:"Yossi Levy",
       imgReply:'pic6.jpg',
       issueID:"mainIssue"+this.id.toString(),
       commentsID:"comButton"+this.id.toString(),
       replyInputID:"inputReply"+this.id.toString(),
       comments:0,
       rating : 0,
       isCommentsShown:false,
    //    header: "This Docuement is shit",
    //    author:"Dan Segev",
    //    date:"23.5.2021",
       //static comments data of course will be brought from server later --> debug purpose
       replies:[
        //    {title: "This Docuemnt is actully fine too much complaining",author:"Rina Bar",date:"26.5.2021",content:"good quality",rating:45,profile:'user7.png'},
        //    {title: "This Docuemnt is fine",author:"Yogev Bar David",date:"28.5.2021",content:"very good ",rating:34,profile:'user2.png'},
        //    {title: "This Docuemnt is bad",author:"Guy Ronen",date:"28.5.2021",content:"variable names are too short bro.. ",rating:59,profile:'user9.png'},  
       ]
   }
     },
    methods:{
          getDate(){
     var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); 
    var yyyy = today.getFullYear();

      today = mm + '/' + dd + '/' + yyyy;
      return today
  
   },
        createNewReply(e){
            if(e.keyCode==13){
                //means Enter was pressed
                var contentInput=document.getElementById(this.replyInputID).value
                var newReplyObject={
                  title:"sdf",author:this.replyAuthor,date:this.getDate().toString(),content:  contentInput,rating:0,profile:this.imgReply}
                this.replies.push(newReplyObject)
              
                document.getElementById(this.replyInputID).value=""
                this.comments=this.comments+1
                //if comments are open show also the new one
                if(this.isCommentsShown==true){
                      this.addReply(newReplyObject)
                }
            
                
            }
        },
        addReply(reply)
        {
         var ComponentClass = Vue.extend(Reply)
            var newReply = new ComponentClass(
                {
                propsData: {title:reply.title,
                    content:reply.content,
                    date:reply.date,
                    author:reply.author,
                    rating:reply.rating,
                    img:reply.profile
                

    }}
            )
        newReply.$mount() // pass nothing
        document.getElementById(this.issueID).appendChild(newReply.$el)
    
            console.log("show replies!!!!")
        },
        submitIssue(){

//                 axios({
//   method: 'post',
//   url: 'http://127.0.0.1:8000/api/users/',
//   data: {
//     email : "test@gmail.com",
//     username : 'test'
//   }
//                     })
// .then(response => (this.info = response.data))
        },
        CheckKeyPress(e){
                if(e.keyCode === 13){
            e.preventDefault(); // Ensure it is only this code that runs

            console.log("Enter was pressed was presses");
        }
        },
        openReplies(){
            if(this.isCommentsShown==false){

         for (var i = 0; i < this.replies.length; i++) {
         this.addReply(this.replies[i])
         }

          this.isCommentsShown=true
          document.getElementById(this.commentsID).className="commentShown"
          
         
        }
        else{
            var mainIssueDiv=document.getElementById(this.issueID)
            //delete the replys and leave only the comment itslf
            //TODO: check better soultion if content is large? is this heavy in runtime?(  probaly ain't no one better though)
            while (mainIssueDiv.childNodes.length > 1) {
                 document.getElementById(this.issueID).removeChild(mainIssueDiv.lastChild)
            }
            this.isCommentsShown=false
            document.getElementById(this.commentsID).className="commentsOnIt"

}
        //toggle the class to marked/unmarked
       
            
        }
    }
}
</script>
<style scoped>
.commentsOnIt{
    color:gray
}
.commentShown{
    color:lightblue
}
.commentShown:hover{
    color:gray
}
.commentsOnIt:hover{
    color:lightblue
}
.starUnMarked{
    color: gray;
}

.starUnMarked:hover{
    color: gold;
}
.gapSapn{
    position: absolute;
    width: 1px;
    height: 1px;
    margin: -1px;
    padding: 0;
    overflow: hidden;
    clip: rect(0,0,0,0);
    border: 0;
}
.iconrating{
    font-family: udemyicons!important;
    speak: none;
    font-style: normal;
    font-weight: 400;
    font-variant: normal;
    text-transform: none;
    line-height: 1;
    -webkit-font-smoothing: antialiased;
    vertical-align: 0;
}
.ratings{
    display: flex;
    align-items: center;
    justify-content: flex-end;
}
.ratebutton{
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
    color: #3e4143;
    background-color: transparent;
    border: 1px solid transparent;
    padding: 10px 11px;
    color: #d1d7dc;
    border-radius: 50%;
    margin-left: -4px;
}
.issueContent{
    margin-top: .4rem;
    display: block;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
.ratingValue{
    font-size: 14px;
    font-weight: 400;
    line-height: 1.43em;
    display: inline-block;
    color: #3e4143;
    font-weight: 700;
    position: relative;
    vertical-align: bottom;
    z-index: 1;
}
.hrefIssue{
    color: #1c1d1f;
    font-weight: 700;
}
.issueDivText{
      font-family: sf pro display,-apple-system,BlinkMacSystemFont,Roboto,segoe ui,Helvetica,Arial,sans-serif,apple color emoji,segoe ui emoji,segoe ui symbol;
    font-size: 14px;
    font-weight: 700;
    line-height: 1.43em;
    display: block;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    max-width:60rem;

}
.ratingDivIssue{
    display: flex;
    flex-direction: column;
}
.innerIssueDiv{
  flex: 1;
    min-width: 1px;
    padding-left: 1.6rem;



}
.contentissueDiv{
    display: block;
    flex: 1;
    min-width: 1px;
    padding-right: 4.8rem;



}
.innerIssueDivData{
    display: flex;
    border-top: 1px solid #f7f9fa;
    font-size: 14px;
    font-weight: 400;
    line-height: 1.43em;
    padding: 1.6rem 2.4rem;


}
 .issueIcon{
   display: inline-block;
    position: relative;
    max-width: 100%;
        border-radius: 50%;
    object-fit: cover;
 }
.innerIssuesContainer{
  border-top: 0;
      border-bottom: 1px solid #f7f9fa;
      display: block

}
.outerIssuesContainer{
      margin-bottom: 48px;
          display: block;

    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
.issueDiv{
  display: flex;
    border-top: 1px solid #f7f9fa;
    font-size: 14px;
    font-weight: 400;
    line-height: 1.43em;
    padding: 1.6rem 2.4rem;


}
.replyInput{
    border:1px solid dashed;
    height: 34px;
    padding: 0 10px;
    font-size: 13px;
    line-height: 1.287;
    border-radius: 0;
        width: 565px;
  }



</style>