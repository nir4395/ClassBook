<template>
  <div class="about">
    <h1></h1>


        <div class="mx-auto">
    <div   class="row mx-auto">
        <div @click="NavToPage(1)" class="col-md-3 col-sm-6">
           <SchoolBox  name="Computing" img="Instutitons/coding.jpg"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
        <div class="col-md-3 col-sm-6">
           <SchoolBox  name="Nursing" img="Instutitons/nursing.jpg"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
          <div class="col-md-3 col-sm-6">
           <SchoolBox  name="Economics" img="Instutitons/economy.jpg"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
    </div>
    <div  style="margin-top:50px;" class="row mx-auto">
        <div class="col-md-3 col-sm-6">
            <SchoolBox  name="Informatics" img="Instutitons/datas.jpg"></SchoolBox>
             
        </div>
        <div class="col-md-3 col-sm-6">
           <SchoolBox  name="Physcology" img="Instutitons/psyc.jpg"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
          <div class="col-md-3 col-sm-6">
           <SchoolBox  name="Political Science" img="Instutitons/politics.jpg"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
        <!-- <div><v-btn @click="SendLogin()">GO BACK</v-btn></div> -->
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


   SendLogin(){
           var url='http://localhost:8000/users/sign_in/'
           let headers={
             Cookie:" csrftoken=FDGChyFNudqJBm8Rdg5KkNaHdDpZVlUZN8LngUuN3HOUzCsQlZFmrTDJjZfkxlpy; sessionid=cwpu1ygr0wb8fniktiowhn60oo7pepuw"

           }
           
            var bodyFormData = new FormData();
              bodyFormData.append('username', 'guyno1');
              bodyFormData.append('password', 'password123');
        
        this.$http.post(url,bodyFormData,headers).then(response => (console.log(response.data)))
      
      
      },
  
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

