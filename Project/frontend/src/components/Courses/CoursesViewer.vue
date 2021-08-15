<template>
   <v-container class="my-5">


      <v-card v-for="course in courses" :key="course.name">
        <v-layout row wrap class="pa-8">
          <!-- <v-flex xs4 sm4 md2 d-flex>
            <v-img :src="require('../assets/' + course.name + '.png')"></v-img>
          </v-flex> -->
          <v-flex xs6 sm2 md5>
            <div class="caption grey--text">Course Name</div>
            <div>{{ course.name }}</div>
          </v-flex>
          <v-divider class="mx-4"
  vertical
></v-divider>
          <!-- <v-flex xs3 sm2 md2>
            <div class="caption grey--text">Lecturer</div>
            <div>{{ course.lecturer }}</div>
          </v-flex> -->
          <!-- <v-flex xs3 sm2 md2>
            <div class="caption grey--text">Participants</div>
            <div>{{ course.rank }}</div>
          </v-flex> -->
         <v-flex  xs3 sm2 md2>
               <v-list-item-subtitle  style="margin-top:4px;font-size:16px">View Categories</v-list-item-subtitle>

          </v-flex>
         
            <v-flex xs3 sm2 md1>

                <v-icon @click="navToCourseCategorySelection(course.name,course.id)" style="margin-top:4px;font-size:24px">find_in_page</v-icon>
          </v-flex>
           <v-flex  v-if="!course.isReg" xs2 sm2 md2>
              <v-list-item-subtitle  style="display:flex;margin-top:4px;font-size:16px">Register to course</v-list-item-subtitle>
          </v-flex>
          <v-flex  xs2 sm2 md1>
               <v-icon   v-if="course.isReg"  @click="RegistertoCourse(course.id)" style="margin-top:4px;font-size:24px">how_to_reg</v-icon>

               <v-icon v-if="!course.isReg" @click="RegistertoCourse(course.id)" style="margin-top:4px;font-size:24px">add</v-icon>
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
    RegistertoCourse(courseId){
          var url='http://localhost:8000/course/register/'
          var data={'course_id':courseId}
         this.$http.post(url,data).then(response => (console.log(response.data)
        ))
    }

     
    }

   
}
</script>

<style>

</style>