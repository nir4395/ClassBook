<template>
  <div class="about">
    <h1></h1>


        <div class="container">
    <div  style="margin-top:50px;" class="row">
       
        <div @click="GoToCourses(1)" class="col-md-3 col-sm-6">
           <SchoolBox  name="First Year Courses" img="math.png"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div >
          <div @click="GoToCourses(2)"  class="col-md-3 col-sm-6">
           <SchoolBox  name="Second Year Courses" img="memory.png"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
    </div>
    <div  style="margin-top:50px;" class="row">
     
        <div class="col-md-3 col-sm-6">
           <SchoolBox @click="GoToCourses(3)"  name="Third Year Courses" img="stor.png"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
          <div class="col-md-3 col-sm-6">
           <SchoolBox  @click="GoToCourses(4)"  name="Selection Courses" img="mobile.png"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
    </div>
</div>


  </div>
</template>
<script>
import SchoolBox from '../components/SelectSchools/SchoolBox.vue'
import axios from 'axios'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken";
export default {
    data(){
        return {

            data:null
        }
        
    },
  components:{
    SchoolBox
  },
  
  methods:{
    GoToCourses(category){
      console.log("sdfsdfsd")
           return this.$router.push({ name: 'CoursesSelection', params: { category: category } })
    },
        getCatergories(){
                 let headers = {
         "X-CSRFToken": axios.defaults.xsrfCookieName,
         "Content-Type": "application/x-www-form-urlencoded"
       }
              axios
              
    .get('http://localhost:8000/course/get/course_id=3/categories',headers)
    .then(response => (this.data = response.data))
    console.log(this.info)

        }
  },
  //onload events
  created(){
        this.getCatergories()
  }
}
</script>
<style scoped>

</style>

