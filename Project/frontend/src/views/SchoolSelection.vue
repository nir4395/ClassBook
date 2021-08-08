<template>
  <div class="about">
    <h1></h1>


        <div class="container">
    <div  style="margin-top:50px;" class="row">
        <div @click="NavToPage(1)" class="col-md-3 col-sm-6">
          <v-btn @click="showSchoolData()" color="blue">Show School Data</v-btn>
            <SchoolBox   :name="name" img="coding.png"></SchoolBox>
             
        </div>
        <div @click="NavToPage(2)" class="col-md-3 col-sm-6">
           <SchoolBox  name="Nursing" img="nurse.png"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
          <div class="col-md-3 col-sm-6">
           <SchoolBox  name="Economics And Managment" img="gdp.png"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
    </div>
    <div  style="margin-top:50px;" class="row">
        <div class="col-md-3 col-sm-6">
            <SchoolBox  name="Informatics" img="analysis.png"></SchoolBox>
             
        </div>
        <div class="col-md-3 col-sm-6">
           <SchoolBox  name="Physcology" img="think.png"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
          <div class="col-md-3 col-sm-6">
           <SchoolBox  name="Political Science" img="politics.png"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
    </div>
</div>




    
  </div>
</template>
<script>
import axios from 'axios'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken";
import SchoolBox from '../components/SelectSchools/SchoolBox.vue'
export default {
  data(){
      return {
        info:"",
        name:"Computer Siecne"
      }
},
methods:{

  
  NavToPage(ins){

           return this.$router.push({ name: 'Catergories', params: { ins: ins } })
    
  },
  showSchoolData(){
    let headers = {
         "X-CSRFToken": axios.defaults.xsrfCookieName,
         "Content-Type": "application/x-www-form-urlencoded"
       }
              axios
    .post('http://localhost:8000/course/get/course_id=3/cat=Exams', {
      email : "test@gmail.com",
      username : 'test',
      password:'101duckontheroad',
      csrfmiddlewaretoken : '{{ csrf_token }}'
    },headers)
    .then(response => (this.info = response.data))
    console.log(this.info)

  },
  
},
  components:{
    SchoolBox
  }
}
</script>
<style scoped>

</style>

