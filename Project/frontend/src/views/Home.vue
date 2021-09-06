<template style="background-color:red">
  <div>
  Welcome Back  {{uerData.profile_details.user.first_name}} {{uerData.profile_details.user.last_name}} 
    <div v-if="newUser" class="divStyle">
      <Intro></Intro>
    </div>

    <div style="height:300px;width:100%;overflow:auto" v-if="!newUser">
      <MyCourses :courses="registeredCourses"></MyCourses>
    </div>

    <div style="height:500px;width:100%;margin-top:120px" v-if="!newUser">
      <!-- <v-btn @click="NOTFOUNDNAV()">not found</v-btn> -->
      <CardDisplay :docs="recentDoc.recently_accessed_documents"></CardDisplay>
    </div>
  </div>
</template>

<script>
import Intro from "../components/Intro.vue";
// import MyRecentDocuments from '../components/Documents/MyRecentDocuments.vue'
import CardDisplay from "../components/CardDisplay.vue";
import MyCourses from "../components/MyCourses.vue";



export default {
  name: "Home",
  data() {
    return {
      uerData: "",
     recentDoc :'',
      resp: "",
      newUser: false,
      registeredCourses: "",
      recentDocs: [
        {
          name: "Calculus 1 Exam 2019",
          id: 1,
          rate: 3,
        },
        {
          name: "Calculus 1 Exam 2018",
          id: 2,
          rate: 5,
        },
        {
          name: "Calculus 1 Exam 2014",
          id: 4,
          rate: 4,
        },
        {
          name: "Calculus 1 Exam 2013 Iris",
          id: 5,
          rate: 1,
        },
        {
          name: "Calculus 2 Exam 2013 ",
          id: 6,
          rate: 1,
        },
        {
          name: "Calculus 2 Exam 2013 ",
          id: 6,
          rate: 1,
        },
        {
          name: "Calculus 2 Exam 2013 ",
          id: 6,
          rate: 1,
        },
      ],
    };
  },
  components: {
    Intro,
    //MyRecentDocuments,
    MyCourses,
    CardDisplay,
  },
  created() {
    this.getUsersInfo();
    this.getUsersCoursesInfo();
    this.getRecentDocs();
  },
  methods: {
    async getUsersInfo() {
     
      try {
        var url = "http://localhost:8000/users/user_profile/";
        const response = await this.$http.get(url);
        console.log(response)
        this.uerData = response.data;
      } catch (error) {
        console.log(error);
      }
    },
     async getRecentDocs() {
      //course/get/recent_documents
      try {
        var url = "http://localhost:8000/course/get/recent_documents";
        const response = await this.$http.get(url);
        console.log(response)
        this.recentDoc = response.data;
      } catch (error) {
        console.log(error);
      }
    },
    async getUsersCoursesInfo() {
      try {
        var url = "http://localhost:8000/course/user_registered/";

        const response = await this.$http.get(url);
      this.registeredCourses = response.data["registered_courses"];
      } catch (error) {
        console.log(error);
      }
    },
    
    NOTFOUNDNAV() {
      return this.$router.push("notfound");
    },
    // SendLogin() {
    //   var url = "http://localhost:8000/users/sign_in/";
    //   let headers = {
    //     Cookie:
    //       " csrftoken=FDGChyFNudqJBm8Rdg5KkNaHdDpZVlUZN8LngUuN3HOUzCsQlZFmrTDJjZfkxlpy; sessionid=cwpu1ygr0wb8fniktiowhn60oo7pepuw",
    //   };

    //   var bodyFormData = new FormData();
    //   bodyFormData.append("username", "guyno1");
    //   bodyFormData.append("password", "password123");

    //   this.$http
    //     .post(url, bodyFormData, headers)
    //     .then((response) => console.log(response.data));
    // },
  },
};
</script>
<style scoped>
.homePageRow {
  height: 100px;
  width: 1000px;
  background-color: white;
}
.image {
  padding: 14%;
  box-shadow: 100px;
}
.circle-icon {
  background: lightgray;
  padding: 30px;
  border-radius: 50%;
  height: 50px;
  width: 50px;
}
.divStyle {
  transform: perspective(1250px) translate3d(0px, 0px, -250px) rotateX(-5deg)
    scale(0.9, 0.9);
  /* border-radius: 20px; */
  /* border: 5px solid #e6e6e6; */
  transition: 0.4s ease-in-out transform;
}
</style>
