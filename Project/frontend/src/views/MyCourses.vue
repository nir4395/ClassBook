<template>
   <MyCoursesViewer :info="info"></MyCoursesViewer>
</template>
<script>
import MyCoursesViewer from '../components/Courses/MyCoursesViewer.vue'
export default {
   components:{
       MyCoursesViewer
   },
   data(){
       return {
            info:[
                {name:'Calculus 1',isfav:0,Lecturer:'a',rating:3,stage:'A',school:'CS'},
                 {name:'Linear Algebra 1',isfav:1,Lecturer:'a',rating:3,stage:'A',school:'CS'},
                  {name:'Operating Systems',isfav:0,Lecturer:'a',rating:3,stage:'A',school:'CS'},
                   {name:'Introduction to CS 1',isfav:1,Lecturer:'a',rating:3,stage:'A',school:'CS'}
                   
            ]
       }
   }
}
</script>