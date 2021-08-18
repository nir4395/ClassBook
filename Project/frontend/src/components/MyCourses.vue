<template>
<v-container>
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
       <MyCoursesViewer :info="courses"></MyCoursesViewer>


</v-container>
</template>
<script>
import MyCoursesViewer from '../components/Courses/MyCoursesViewer.vue'
export default {
    props:['courses'],
   components:{
       MyCoursesViewer
   },

}
</script>