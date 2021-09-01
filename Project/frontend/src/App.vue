<template>
  <v-app class="gray fontfam">
    <span class="bg"></span>
    {{uerData}}
    <Navbar :name="uerData.profile_details.user.username"></Navbar>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import Navbar from "@/components/Navbar";
export default {
  name: "App",
  components: { Navbar },
  created(){
    this.getUsersInfo()
  },
  methods:{
    async getUsersInfo() {
      try {
        console.log("ask for the data in App.vue")
        var url = "http://localhost:8000/users/user_profile/";
        const response = await this.$http.get(url);
        console.log(response)
        this.uerData = response.data;
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
  },
  data: () => ({
    uerData:'',
    registeredCourses:'',
    image2: "Covers/back2.jpg",
    //
  }),
};
</script>
<style scoped>
.bg {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  background: url("assets/Covers/back5.jpg") no-repeat center center;
  background-size: cover;
  /* background-color: gray; */
  transform: scale(1.1);
}
.fontfam {
  font-family: "Rubik", sans-serif;
}
</style>
