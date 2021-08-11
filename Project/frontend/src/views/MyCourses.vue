<template>
   <MyCoursesViewer :info="registeredCourses"></MyCoursesViewer>
</template>
<script>
import MyCoursesViewer from '../components/Courses/MyCoursesViewer.vue'
export default {
   components:{
       MyCoursesViewer
   },
   data(){
       return {
            registeredCourses:''
       }
   },
   created(){
       //on page load show all courses user is registered to
         var url='http://localhost:8000/course/user_registered/'
        
         this.$http.get(url).then(response => (this.registeredCourses = response.data))
        
   }
}
</script>