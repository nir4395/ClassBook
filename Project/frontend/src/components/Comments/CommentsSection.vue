<template>
  <div style="background-color:white" class="mx-auto mainCommentSection">
    <div class="outerissuesDiv">
      <div>
        <!-- <div class="searchissuebar">
        <span class="issuesbarspan">
          
          <input placeholder="Search Course Issues" type="text" id="search-issues" class="form-control" value>
        </span>
           
          
          <v-icon style="color:black;background-color:#f7f9fa;border:1px dashed black">search</v-icon>
      </div> -->
        <div style="margin-left:64px" class="issusFiltersDiv">
          <section>
            <v-select
              dense
              @change="ApplyCommentsFilter($event)"
              outlined
              class="mx-auto"
              style="width:800px;margin-top:50px"
              :items="items"
              label="Choose Filter"
            >
            </v-select>
          </section>
          <v-icon
            style="margin-left:26px;margin-top: 19px;"
            class="cancelFiltersxfcv=="
            @click="clearfilters()"
            >clear</v-icon
          >
        </div>
        <div style="font-weight:bold;font-size:16px;">
          ({{ comments.length }}) Comments
        </div>
        <!--  outer container for issues -->
        <div ref="issues" style="overflow:auto"></div>

        <div v-for="comment in comments" :key="comment.id">
          <DocumentIssue
            :docID="id"
            :replies="comment.replies"
            :rate="comment.likes_count"
            :content="comment.content"
            :id="comment.id"
            :author="comment.author"
          ></DocumentIssue>
        </div>

        <div ref="avc" style="margin-top:5px;padding:5px" class="mx-auto">
          <p
            style="border:none;background-color:white;font-size:16px;font-weight:bold"
          >
            Add a new issue
          </p>
        </div>

        <AddIssueBox ref="issueBox"></AddIssueBox>
        <div class="issuecontainerMenu">
          <v-btn
            color="black"
            @click="addNewIssue()"
            style="color:white;cursor:pointer"
            >Submit new Issue</v-btn
          >
        </div>

        <!-- <IssuesReplies></IssuesReplies> -->
      </div>
    </div>
  </div>
</template>
<script>
//'id','title','author','date','content','img','rate','coms
import DocumentIssue from "../Comments/DocumentIssue.vue";
import AddIssueBox from "../Comments/AddIsueBox.vue";
import Vue from "vue";
import Vuetify from "vuetify";
import { VIcon } from "vuetify/lib";
Vue.use(Vuetify);
//  import IssuesReplies from '../components/IssuesReplies.vue'
export default {
  components: {
    DocumentIssue,
    // IssuesReplies,
    AddIssueBox,
  },
  props: ["id", "comments"],

  data() {
    return {
      items: [
        "Show Only From Today",
        "Top Rated Issues",
        "Most Disscussed Issues",
      ],

      //to be removed static data for intro

      commentsData: this.comments,
      //this should be updated with VueX
      // static:[{id:1,author:"David Cohen", comments: 34,rating:4,profile:"userProfiles/pic2.jpg",title:"Epic Content",content:"This Paper really helped me study for my last test",date:new Date()},
      //               {id:2,author:"Shir Ben Harush",comments:0, rating:5,profile:"userProfiles/pic3.jpg",title:"Good Paper",content:"High Quality Well Done",date:new Date(2018, 11, 24, 10, 33, 30, 0)},
      //               {id:3,author:"Dudi Bar", rating:5, comments:23,profile:"userProfiles/pic4.jpg",title:"Not so good , missing info",content:"the important proofs are not inside",date:new Date(2018, 11, 24, 10, 33, 30, 0)},
      //               {id:4,author:"Alon Vered",rating:2, comments:104,profile:'userProfiles/sample.jpg',title:"I was hoping to find answers here.. , missing info",content:"Can't read it. too long and not clear ,you shoud rank this low!",date:new Date()}],
      fil: this.$props["comments"],
      //  filtered:commentsData,

      LastissueID: 0,
      author: "Chen Ben Ezra",
      profile: "sample.jpg",
    };
  },
  methods: {
    buildComments(comments) {
      while (this.$refs["issues"].firstChild) {
        this.$refs["issues"].removeChild(this.$refs["issues"].lastChild);
      }
      console.log("sddkdkdkdk");
      //console.log(comments)
      // `this` points to the vm instance
      for (var index = 0; index < comments.length; index++) {
        var replyIndex = index + 1;
        var commentID = comments[index].id;
        if (comments[index].replied_to_comment === null) {
          //add to the DOM

          // add the replys
          var replies = [];
          while (this.comments[replyIndex].replied_to_comment === commentID) {
            replies.push(comments[replyIndex]);
            replyIndex++;
          }
          var newComment = this.createIssue(comments[index], replies);
          newComment.$mount(); // pass nothing
          this.$refs["issues"].appendChild(newComment.$el);
          index = replyIndex;
        }
      }
    },
    getDate() {
      var today = new Date();
      var dd = String(today.getDate()).padStart(2, "0");
      var mm = String(today.getMonth() + 1).padStart(2, "0"); //January is 0!
      var yyyy = today.getFullYear();

      today = mm + "/" + dd + "/" + yyyy;
      return today;
    },
    clearfilters() {
      this.fil = this.commentsData;
    },
    ApplyCommentsFilter(value) {
      console.log("filter");
      //this.fil=[]
      var today = new Date();
      if (value === "Show Only From Today") {
        for (var i = 0; i < this.commentsData.length; i++) {
          if (this.fil[i].date.getMonth() === today.getMonth()) {
            this.fil.push(this.fil[i]);
          }
        }
        //this.commentsData=this.fil
      }
      if (value === "Top Rated Issues") {
        for (var z = 0; z < this.fil.length; z++) {
          if (this.fil[z].rating === 5) {
            this.fil.push(this.fil[z]);
          }
        }
        //this.commentsData=this.fil
      }
      if (value === "Most Disscussed Issues") {
        for (var j = 0; z < this.fil.length; z++) {
          if (this.fil[j].comments >= 30) {
            this.fil.push(this.fil[j]);
          }
        }
      }
    },
   async addNewIssue() {
     try{
          var issueData = this.$refs["issueBox"];
      // var lastID = this.comments[this.comments.length - 1].id;

      issueData = issueData.submitnewIssue();
      var data = {
        comment_associated_document: this.id,
        comment_content: issueData.content,
        replied_to_comment_id: null,
      };

         var url = "http://localhost:8000/doc_id=" + this.id + "/post_comment";

      //  send the request to the server
     await this.$http.post(url, data).then((response) => console.log(response.data));
      //  this.comments.push(id:)
      // var comment = {
      //   content: issueData.content,
      //   author: "test1",
      //   rate: 0,
      //   id: lastID,
      //   replies: [],
      // };
   
    this.$emit('updateData');
     }
     catch(error){
       console.log(error)
     }
    
     

      // this.comments.push(comment);
      //var newIssue=createIssue(data,[])
    },
    createIssue(comment, repliesOfComment) {
      this.LastissueID = this.LastissueID + 1;
      var ComponentClass = Vue.extend(DocumentIssue, VIcon);
      var newDocumentIssue = new ComponentClass({
        propsData: {
          docID: this.id,
          content: comment.content,
          //  date:this.getDate(),
          author: comment.author,
          rate: comment.likes_count,
          replies: repliesOfComment,
          //  img:this.profile,
          id: comment.id,
        },
      });
      return newDocumentIssue;
    },
    mounted() {
      console.log("Zxxxxx");
    },
  },
};
</script>
<style scoped>
.mainCommentSection {
  display: block;
  margin-top: 10%;
}

.fildiv {
  float: left;
  border: 1px solid black;
  margin-left: 20px;
  margin-top: 20px;
}
.cancelFilters {
  height: 50px;
  width: 50px;
  color: red;
  /* background-color: gray; */
  margin-top: 40px;
  /* margin-right: 66px; */
  margin-left: -49px;
}
.buttonIssueFilter {
  position: relative;
  float: left;
  width: 100%;
  text-align: left;
  padding-right: 32px !important;
  padding-top: 9px;
  padding-bottom: 9px;
  font-size: 16px;
  margin-left: 50px;
  font-weight: 400;
  line-height: 1.5em;
  color: #3e4143;
  /* border-color: #6a6f73; */
  background-color: transparent;
  border: 1px solid #1c1d1f;
}
.outerissuesDiv {
  /* width: 1500px; */

  padding: 0 159px;
}
.sectionissues {
  margin-top: 8px;
  margin-right: 8px;
  flex: 1;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
.issusFiltersDiv {
  display: flex;
  flex-wrap: wrap;
  width: 100%;
  padding-bottom: 32px;
}
.searchissuebar {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding-top: 32px;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.issuesbarspan {
  font-size: 14px;
  font-weight: 400;
  line-height: 1.43em;
  width: 100%;
}
input {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
  background-color: #f7f9fa;
  border-color: #fff;
}
.searchbuttonSpan {
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
.searchButton {
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
.innerspanButton {
  vertical-align: -8%;
  font-family: udemyicons !important;
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
