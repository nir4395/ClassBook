<template>
  <div>
    <h1>Courses Selection - {{catName}}</h1>
    <CourseViewer :courses="coursesInfo"></CourseViewer>
  </div>
</template>

<script>
import CourseViewer from "../components/Courses/CoursesViewer.vue";
export default {
  data() {
    return {
      ins: this.$route.params.ins,
      year_code: this.$route.params.yearCode,
      catName:this.$route.params.catName,
      // courses:[{name:'Calculus 1',lecturer:'Romina Zigdon',rank:'2',courseStage:'A',school:'CS',id:1,isReg:true},
      // {name:'Linear Algebra 1',lecturer:'Dan Levy',rank:'5',courseStage:'A',school:'CS',id:2,isReg:false},
      // {name:'Introduction to CS 1',lecturer:'Hadar Binsky',rank:'5',courseStage:'A',school:'CS',id:3,isReg:false} ]
      coursesInfo: "",
    };
  },

  components: {
    CourseViewer,
  },

  created() {
    //this.getCourses()
    var url =
      "http://localhost:8000/course/get/ins=" +
      this.ins +
      ",year=" +
      this.year_code;

    this.$http
      .get(url)
      .then((response) => (this.coursesInfo = response.data.courses_by_year));
  },
};
</script>
<style scoped></style>
