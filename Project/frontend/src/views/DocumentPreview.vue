<template>
  <div class="mx-auto mainDocumentDiv">
    <Rating
      @updateRating="UpdateRating($event)"
      :canRate="isDocRated"
      :name="name"
      :rating="rating"
      :id="id"
    ></Rating>
    <OtherDocsPreivew v-if="type !== 'pdf'"></OtherDocsPreivew>
    <PDFView :id="id"></PDFView>
    <!-- <PDFJSViewer v-else :fileURL="getFile()" :fileName="name" :id="id" /> -->

    <CommentsSection
      @updateData="getData()"
      ref="comSection"
      :comments="doc"
      :id="id"
    ></CommentsSection>
  </div>
</template>
<script>
const POLLING_INTERVAL = 10000;

import axios from "axios";

import OtherDocsPreivew from "../components/OtherDocsPreivew.vue";
import CommentsSection from "../components/Comments/CommentsSection.vue";
// import PDFJSViewer from "../components/PDFJSViewer.vue";
import Rating from "../components/Rating.vue";
import PDFView from "../components/Documents/PDFView.vue";

export default {
  components: {
    PDFView,
    OtherDocsPreivew,
    CommentsSection,
    // PDFJSViewer,
    Rating,
  },

  data() {
    return {
      type: this.$route.params.docType,
      name: this.$route.params.name,
      id: this.$route.params.id,
      rating: this.$route.params.rating,
      docInfo: "",
      date: "",
      doc: [],
      documnetComments: "",
      polling: null,
      rated: false,
      fileURL: "course/get/doc_id=14",
      urlImg: "book.jpg",
      issues: [],
      VIEWS_FILTER: 10,
      lastIssueNumber: 1,
      isModalVisible: false,
      isRateDocVisable: false,
      isDocRated: "",
    };
  },
  methods: {
    async isDocumentRatedByUser() {
      let url = "doc_id/" + this.id + "/is_document_rated_by_user";
      try {
        let response = await this.$http.get(url);
        this.isDocRated = response.data.is_document_rated;
      } catch (error) {
        console.log(error);
      }
    },
    UpdateRating(newRating) {
      console.log("xxxx");
      this.isDocRated = true;
      this.rating = newRating;
    },
    getFile() {
      var url = "http://localhost:8000/course/get/doc_id/6";
      //    var url = 'http://localhost:8000/course/get/doc_id/'+this.id
      console.log(url);
      return url;
    },
    setRating(number) {
      this.rated = true;
      let params = {
        document_id: this.id,
        user_rating: number,
      };
      const url = "course/rate/";
      axios
        .post(url, params)
        .then((response) => {
          this.rating = response.data.new_rating
            ? response.data.new_rating
            : this.rating;
          console.log(response.data);
        })
        .catch((e) => console.log(e));
    },
    async getData() {
      try {
        console.log("fire!");
        var urlDocumentComments =
          "doc_id/" + this.id + "/get_all_document_comments";
        const response = await this.$http.get(urlDocumentComments);
        this.documnetComments = response.data;
        var comments = this.documnetComments.all_comments;

        this.doc = this.buildComments(comments);
        console.log("getting the data!");
      } catch (error) {
        console.log(error);
      }
    },

    getComments() {
      var urlDocumentComments =
        "doc_id/" + this.id + "/get_all_document_comments";
      var allComments = "";
      this.$http
        .get(urlDocumentComments)
        .then((response) => (this.documnetComments = response.data));
      var comments = this.$data.documnetComments.all_comments;
      allComments = this.buildComments(comments);
      console.log(allComments);
      this.doc = allComments;
    },
    buildComments(comments) {
      var newComments = [];
      for (var index = 0; index < comments.length - 1; index++) {
        var replyIndex = index + 1;
        var commentID = comments[index].id;
        if (comments[index].replied_to_comment === null) {
          // add the replys
          var replies = [];
          console.log(replyIndex);
          while (comments[replyIndex].replied_to_comment === commentID) {
            replies.push(comments[replyIndex]);
            replyIndex++;
          }
          comments[index].replies = replies;
          newComments.push(comments[index]);

          // var newComment= this.createIssue(comments[index],replies)
          //    newComment.$mount() // pass nothing
          // this.$refs['issues'].appendChild(newComment.$el)
          index = replyIndex;
        }
      }
      console.log("comments return");
      return newComments;
    },
    pollData() {
      this.polling = setInterval(() => {
        this.getData();
      }, POLLING_INTERVAL);
    },
  },

  beforeDestroy() {
    clearInterval(this.polling);
  },
  created() {
    // console.log("poll!");
    this.isDocumentRatedByUser();
    this.getData();
    //this.pollData();
  },
};
</script>
<style>
.previewImg {
  margin-left: -15%;
  height: 100px;
  float: left;
  width: 100px;
  margin-top: 2%;
  position: absolute;
}
.mainDocumentDiv {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 70%;
  /* height: 79vh; */
  min-width: 250px;
}
.documentArea {
  padding: 3%;
  height: 100%;
  width: 75%;
  float: left;
}
.reviewsBox {
  width: 100%;
  height: 11%;
  background-color: lightgrey;
}
.checked {
  color: orange;
}
.embedZone {
  margin-top: 14%;
  height: 75%;
  width: 100%;
}
.commentsArea {
  padding: 3%;
  height: 100%;
  width: 25%;
  float: left;
  background-color: #e9ecef;
  margin-top: 3%;
}
.addcommentDiv {
  height: 10%;
  background-color: lightgrey;
  width: 100%;
}
body {
  font-family: Helvetica;
}
.issuesArea {
  height: 75%;
  width: 100%;
  overflow: auto;
}
</style>
