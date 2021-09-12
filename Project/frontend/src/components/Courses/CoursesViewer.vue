<template>
  <v-container class="my-5">
    <v-card v-for="(course, index) in courses" :key="course.name">
      <v-layout row wrap class="pa-8">
        <v-flex xs6 sm2 md5>
          <div class="caption grey--text">Course Name</div>
          <div>{{ course.name }}</div>
        </v-flex>
        <v-divider class="mx-4" vertical></v-divider>
        <v-flex xs3 sm2 md2>
          <v-list-item-subtitle style="margin-top:4px;font-size:16px"
            >View Categories</v-list-item-subtitle
          >
        </v-flex>

        <v-flex xs3 sm2 md1>
          <v-icon
            @click="navToCourseCategorySelection(course.name, course.id)"
            style="margin-top:4px;font-size:24px"
            >find_in_page</v-icon
          >
        </v-flex>
        <v-flex v-if="!course.is_registered" xs2 sm2 md2>
          <v-list-item-subtitle
            style="display:flex;margin-top:4px;font-size:16px"
            >Register to course</v-list-item-subtitle
          >
        </v-flex>
        <v-flex xs2 sm2 md1>
          <v-icon
            v-if="course.is_registered"
            @click="RegistertoCourse(course.id, index)"
            style="margin-top:4px;font-size:24px"
            >how_to_reg</v-icon
          >

          <v-icon
            v-if="!course.is_registered"
            @click="RegistertoCourse(course.id, index)"
            style="margin-top:4px;font-size:24px"
            >add</v-icon
          >
        </v-flex>
      </v-layout>
      <v-divider></v-divider>
    </v-card>
  </v-container>
</template>
<script>
export default {
  components: {},
  props: ["courses"],
  methods: {
    navToCourseCategorySelection(nameOfCourse, id) {
      return this.$router.push({
        name: "CourseCategorySelection",
        params: { courseName: nameOfCourse, courseID: id },
      });
    },
    RegistertoCourse(courseId, index) {
      var url = "course/register/";
      var data = { course_id: courseId };
      this.$http.post(url, data).then((response) => console.log(response.data));
      this.courses[index].is_registered = true;
    },
  },
};
</script>

<style></style>
