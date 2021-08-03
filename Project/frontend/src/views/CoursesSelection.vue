<template>
    <div>
   
        <CourseViewer :courses="info"></CourseViewer>
    </div>
    
</template>

<script>
import CourseViewer from '../components/Courses/CoursesViewer.vue'
import axios from 'axios'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken";
export default {

     data(){
        return{
            category:this.$route.params.category,
            info:[{name:'Calculus 1',lecturer:'Romina Zigdon',rank:'2',courseStage:'A',school:'CS',id:1},
            {name:'Linear Algebra 1',lecturer:'Dan Levy',rank:'5',courseStage:'A',school:'CS',id:2},
            {name:'Introduction to CS 1',lecturer:'Hadar Binsky',rank:'5',courseStage:'A',school:'CS',id:3} ]
                
        }
    },

    components:{
        CourseViewer
    },
    methods:{
        getCourses(){
            
            //course/get/ins=1,year='+this.category
        let url='http://localhost:8000/course/get/course_id=2/cat=2'
        console.log(url)
                 let headers = {
         "X-CSRFToken": axios.defaults.xsrfCookieName,
         "Content-Type": "application/x-www-form-urlencoded"
       }
              axios
     
    .get(url,headers)
    .then(response => (this.info = response.data.courses_by_year))
        },
               
    },
    created(){
        //this.getCourses()
    }
}
   
</script>
<style scoped>

</style>