<template>
  <div>
      <CardDisplay></CardDisplay>
    <div
      class="mx-auto"
      style="font-weight:bold;font-size:24px;text-align:center;width:1000px"
    >
      {{ name }} - Docuemnts Catergories
    </div>
    <CourseCatergories
      :name="name"
      :id="id"
      :courseCategories="courseCategoriesInfo"
    ></CourseCatergories>
  </div>
</template>
<script>
import CourseCatergories from "../components/Courses/CourseCatergories.vue";
import CardDisplay from '../components/CardDisplay.vue'
export default {
  data() {
    return {
      id: this.$route.params.courseID,
      name: this.$route.params.courseName,
      courseCategoriesInfo: "",
    };
  },
  created() {
    var url =
      "http://localhost:8000/course/get/course_id=" + this.id + "/categories";
    this.$http
      .get(url)
      .then((response) => (this.courseCategoriesInfo = response.data));
  },
  components: {
    CourseCatergories,
    CardDisplay
  },
};
</script>
