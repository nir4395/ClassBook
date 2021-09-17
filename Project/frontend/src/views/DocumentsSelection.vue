<template>
  <div>
    <div style="width:100%;height:40%">
      <!-- {{name}} -->
      <FiltersBar
        :enuMSrt="sort"
        @clear="ResetData()"
        @showOnlyMostViews="FilterDataByViews()"
        @showOnlyHighesrRanked="FilterData()"
        @showOnlyTenLastUploaded="FilterDataByUploadDate()"
        @sortRankings="sortByRankings($event)"
        @sortViews="sortbyViews($event)"
        @sortByDate="sortByDates($event)"
      ></FiltersBar>
    </div>

    <div style="width:100%;height:500px ">
      <DocumentListing
        ref="docListing"
        :cat="cat"
        :name="name"
        :docs="docsInfo"
      ></DocumentListing>
    </div>

    <!-- <v-divider></v-divider> -->
    <!-- <DocumentListing></DocumentListing> -->
    <!-- <v-divider></v-divider> -->
    <UploadModal :id="id" :cat="cat"></UploadModal>
  </div>
</template>
<script>
const HIGHEST_RANK = 5.0;
const VIEWS_FILTER = 50;
//const VIEWS_FILTER=10
import DocumentListing from "../components/Documents/DocumentListing.vue";
import FiltersBar from "../components/Documents/FiltersBar.vue";
import UploadModal from "../components/Documents/UploadModal.vue";
export default {
  data() {
    return {
      id: this.$route.params.courseID,
      name: this.$route.params.courseName,
      cat: this.$route.params.cat,
      original: "",
      //   docsInfo:[
      //    {name:'Calculus 1 -Exam 2019 Term A First Exam 2019.2.3',author:'Marina Slovotichx',views:34,rating:4,upload_date:"2019-08-16T08:37:09.098Z",lastComment:'20.6.2021'},
      //    {name:'Calculus 1 -Exam 2019 Term A  Second Exam  2019.29.3',author:'Gal Braun',views:122,rating:4,upload_date:'2021-06-16T08:37:09.098Z',lastComment:'20.6.2021'},
      //    {name:'Calculus 1 -Exam 2021 Term B  First Exam  2021.7.6',author:'Tomer Shavit',views:23,rating:5,upload_date:'2021-08-16T02:37:09.098Z',lastComment:'20.7.2021'},
      //    {name:'Calculus 1 -Exam 2021 Term B  Second Exam  2021.8.6',author:'Tomer Shavit',views:5,rating:5,upload_date:'2021-01-01T08:37:09.098Z',lastComment:'31.7.2021'},
      //  ],
      docsInfo: "",
      ddddd: "",
      sort: { UP: 1, DOWN: 0 },
    };
  },
  methods: {
    async getData() {
      try {
        //course/course_id/<course_id>/categories/<doc_category>
        var url = "course/course_id/" + this.id + "/categories/" + this.cat;

        const response = await this.$http.get(url);
        // JSON responses are automatically parsed.
        this.original = response.data.documents;
        this.docsInfo = this.original;
      } catch (error) {
        console.log(error);
      }
    },
    ResetData() {
      console.log("Reset");
      this.docsInfo = this.original;
    },
    sortByRankings(arg) {
      console.log(arg);
      this.sortData(this.docsInfo, "rating", arg);
    },
    sortbyViews(arg) {
      console.log(arg);
      this.sortData(this.docsInfo, "view_count", arg);
    },
    sortByDates(arg) {
      console.log(arg);
      this.sortDataByDate(this.docsInfo, arg);
    },
    getDocs() {
      return this.docs;
    },
    //numeric sorter for a given array of docuemnt JSON array, iterates the obejct and sorts acording to given key
    sortDataByDate(data, arg) {
      if (arg === 0) {
        data.sort(function(firstDocuemnt, secondDocument) {
          return (
            parseFloat(secondDocument["date"].getTime()) -
            parseFloat(firstDocuemnt["date"].getTime())
          );
        });
      } else {
        data.sort(function(firstDocuemnt, secondDocument) {
          return (
            parseFloat(firstDocuemnt["date"].getTime()) -
            parseFloat(secondDocument["date"].getTime())
          );
        });
      }
    },
    sortData(data, key, arg) {
      if (arg === 0) {
        data.sort(function(firstDocuemnt, secondDocument) {
          return (
            parseFloat(secondDocument[key]) - parseFloat(firstDocuemnt[key])
          );
        });
      } else {
        data.sort(function(firstDocuemnt, secondDocument) {
          return (
            parseFloat(firstDocuemnt[key]) - parseFloat(secondDocument[key])
          );
        });
      }
    },
    FilterDataByViews() {
      var filteredDocs = [];
      for (var i = 0; i < this.docsInfo.length; i++) {
        if (this.docsInfo[i].view_count >= VIEWS_FILTER) {
          filteredDocs.push(this.docsInfo[i]);
        }
      }
    },
    FilterByDates() {
      for (var i = 0; i < this.docsInfo.length; i++) {
        var dateData = this.docsInfo[i].upload_date.split("T");
        this.docsInfo[i].date = new Date(dateData[0]);
        this.docsInfo[i].hours = new Date(dateData[1]);
      }
      this.this.docsInfo = this.sortDataByDate(this.docsInfo, 0);
    },
    FilterDataByUploadDate() {
      console.log("by dates");
      this.FilterByDates();
    },
    FilterData() {
      var filteredDocs = [];
      console.log("was called by filters bar");
      for (var i = 0; i < this.docsInfo.length; i++) {
        if (this.docsInfo[i].rating === HIGHEST_RANK) {
          filteredDocs.push(this.docsInfo[i]);
        }
      }
      //update the proprety with the filtered infomartion
      this.sortData(filteredDocs, "rating");
      this.docsInfo = filteredDocs;
      //this.$refs['docListing'].$props["docs"]=filteredDocs
    },
  },
  components: {
    DocumentListing,
    UploadModal,
    FiltersBar,
  },

  created() {
    this.getData();
  },
  computed: {
    getName() {
      return this.$route.params.courseName;
    },
    getID() {
      return this.$route.params.courseID;
    },
    getcat() {
      return this.$route.params.cat;
    },
  },
};
</script>
<style scoped>
.uploadButton {
  background-color: red;
  padding: 5%;
  margin-left: 84%;
  margin-top: 5%;
}
</style>
