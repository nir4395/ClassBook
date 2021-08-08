<template>
   <v-container class="my-5">

      {{courses}}

      <v-card v-for="course in courses" :key="course.name">
        <v-layout row wrap class="pa-6">
          <!-- <v-flex xs4 sm4 md2 d-flex>
            <v-img :src="require('../assets/' + course.name + '.png')"></v-img>
          </v-flex> -->
          <v-flex xs3 sm2 md2>
            <div class="caption grey--text">Course Name</div>
            <div>{{ course.name }}</div>
          </v-flex>
          <v-flex xs3 sm2 md2>
            <div class="caption grey--text">Lecturer</div>
            <div>{{ course.lecturer }}</div>
          </v-flex>
          <v-flex xs3 sm2 md2>
            <div class="caption grey--text">Participants</div>
            <div>{{ course.rank }}10</div>
          </v-flex>
          <v-flex xs3 sm2 md2>
            <div class="caption grey--text">Stage</div>
            <div>{{ course.courseStage }}</div>
          </v-flex>
          <v-flex xs3 sm2 md2>
            <div class="caption grey--text">School</div>
            <div>{{ course.school }}</div>
          </v-flex>
            <v-flex xs3 sm2 md2>

                <v-icon @click="navToCourseCategorySelection(course.name,course.id)" style="margin-top:4px;font-size:40px">find_in_page</v-icon>
          </v-flex>
           <v-flex xs2 sm2 md2>
              <v-list-item-subtitle  style="margin-top:4px;font-size:12px">Add to favorites</v-list-item-subtitle>
                <v-icon style="margin-top:4px;font-size:20px">add_to_home_screen</v-icon>
          </v-flex>

        </v-layout>
        <v-divider></v-divider>
      </v-card>

    </v-container>
</template>
// courses should be an array of { name: , lecturer: , rank: , courseStage: , school:}
<script>
export default {

    props: ['courses'],
    methods:{
         navToCourseCategorySelection(nameOfCourse,id){
    
           return this.$router.push({ name: 'CourseCategorySelection', params: { courseName:nameOfCourse, courseID: id } })
    },
     
    }

   
}
</script>

<style>

</style>