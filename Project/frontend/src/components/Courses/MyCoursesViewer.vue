<template>
   <v-container class="my-5">
     
      <v-card v-for="course in info" :key="course.name">
        <v-layout row wrap class="pa-6">
          <!-- <v-flex xs4 sm4 md2 d-flex>
            <v-img :src="require('../assets/' + course.name + '.png')"></v-img>
          </v-flex> -->
          <v-flex xs3 sm2 md2>
            <div class="caption grey--text">Course Name</div>
            <div>{{ course.name }}</div>
          </v-flex>
          <v-flex xs3 sm2 md2>
            <div class="caption grey--text">Year</div>
            <div>{{ course.year_code }}</div>
          </v-flex>
          <v-flex xs3 sm2 md2>
            <div class="caption grey--text">Student Count</div>
            <div>{{ course.student_count }}</div>
          </v-flex>
          <v-flex xs3 sm2 md2>
            <div class="caption grey--text">Date Updated</div>
            <div>{{ course.date_updated }}</div>
          </v-flex>
          <!-- <v-flex xs3 sm2 md2>
            <div class="caption grey--text">School</div>
            <div>{{ course.school }}</div>
          </v-flex> -->
            <!-- <v-flex xs3 sm2 md2>
                <v-icon  color="red"  v-if="course.isfav" style="margin-top:4px;font-size:20px">favorite</v-icon>
          </v-flex> -->
            <v-flex xs3 sm2 md2>
            <div class="caption grey--text">Unregirster Course</div>
            <v-icon>delete</v-icon>
          </v-flex>

        </v-layout>
        <v-divider></v-divider>
      </v-card>

    </v-container>
</template>
// courses should be an array of { name: , lecturer: , rank: , courseStage: , school:}
<script>
export default {
    props: ['info'],
    methods:{
         navToCourseCategorySelection(nameOfCourse,id){
    
           return this.$router.push({ name: 'CourseCategorySelection', params: { courseName:nameOfCourse, courseID: id } })
    },
     
    }
   
}
</script>

<style>

</style>