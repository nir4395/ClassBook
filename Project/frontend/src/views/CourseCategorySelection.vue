<template>
  <div>
    <div
      class="mx-auto"
      style="font-weight:bold;font-size:24px;text-align:center;width:1000px"
    >
      {{ name }} - Document Categories
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
export default {
  data() {
    return {
      id: this.$route.params.courseID,
      name: this.$route.params.courseName,
      courseCategoriesInfo: "",
    };
  },
  created() {
    var url = "course/get/course_id/" + this.id + "/categories";
    this.$http
      .get(url)
      .then((response) => (this.courseCategoriesInfo = response.data));
  },
  components: {
    CourseCatergories,
  },
};
</script>
