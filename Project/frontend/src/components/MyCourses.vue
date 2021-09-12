<template>
<v-container v-if="courses.length!==0">
    <v-toolbar
      color="blue"
      dark
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>My Courses </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
    
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-checkbox-marked-circle</v-icon>
      </v-btn>
    </v-toolbar>
    <div v-if="courses.length!==0">
       <MyCoursesViewer :info="courses"></MyCoursesViewer>
    </div>
   
      


</v-container>

<v-container v-else>
  <v-card style="height:100px;background-color:white"
  elevation="3"

>
  <h2>Not Follwing Courses yet?</h2>
      
     <v-btn  color="gray" @click="goToCourses()">Add Courses</v-btn>
</v-card>
   
</v-container>
</template>
<script>
import MyCoursesViewer from '../components/Courses/MyCoursesViewer.vue'
export default {
    props:['courses'],
   components:{
       MyCoursesViewer
   },
   methods:{
      goToCourses(){
         return this.$router.push({ name: "SchoolSelection", params: { ins: 1 } });
      }
   },

}
</script>