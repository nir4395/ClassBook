<template>
  <div class="about">
    <h1></h1>

    <div class="container">
      <div style="margin-top:50px;" class="row">
        <div @click="GoToCourses(1, '')" class="col-md-3 col-sm-6">
          <SchoolBox
            name="First Year Courses"
            img="Instutitons/maths.jpg"
          ></SchoolBox>
          <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
        <div
          @click="GoToCourses(2, 'Second Year Courses')"
          class="col-md-3 col-sm-6"
        >
          <SchoolBox
            name="Second Year Courses"
            img="Instutitons/hardwere.jpg"
          ></SchoolBox>
        </div>
      </div>
      <div style="margin-top:50px;" class="row">
        <div
          @click="GoToCourses(3, 'Third Year Courses')"
          class="col-md-3 col-sm-6"
        >
          <SchoolBox
            name="Third Year Courses"
            img="Instutitons/computers2.jpg"
          ></SchoolBox>
        </div>
        <div
          @click="GoToCourses(10, 'Selection Courses')"
          class="col-md-3 col-sm-6"
        >
          <SchoolBox
            name="Selection Courses"
            img="Instutitons/mobile.jpg"
          ></SchoolBox>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import SchoolBox from "../components/SelectSchools/SchoolBox.vue";
import axios from "axios";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
export default {
  data() {
    return {
      ins: this.$route.params.ins,

      data: null,
    };
  },
  components: {
    SchoolBox,
  },

  methods: {
    GoToCourses(year_code_param, categoryName) {
      return this.$router.push({
        name: "CoursesSelection",
        params: {
          catName: categoryName,
          ins: this.ins,
          yearCode: year_code_param,
        },
      });
    },
    getCatergories() {
      let headers = {
        "X-CSRFToken": axios.defaults.xsrfCookieName,
        "Content-Type": "application/x-www-form-urlencoded",
      };
      axios

        .get("http://localhost:8000/course/get/course_id=3/categories", headers)
        .then((response) => (this.data = response.data));
      console.log(this.info);
    },
  },
  //onload events
  created() {
    this.getCatergories();
  },
};
</script>
<style scoped></style>
