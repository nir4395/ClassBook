<template style="background-color:red">
<div>
  <div v-if="newUser">
  <Intro></Intro>
</div>

<div v-if="!newUser" style="height:300px;width:100%" class="divStyle">
  <MyCourses :courses="registeredCourses"></MyCourses>

</div>


<div style="margin-top:10px" v-if="!newUser">
  <MyRecentDocuments   class="divStyle"></MyRecentDocuments>
</div>
</div>

</template>

<script>
import axios from 'axios'
import Intro from '../components/Intro.vue'
import MyRecentDocuments from '../components/Documents/MyRecentDocuments.vue'
import MyCourses from '../components/MyCourses.vue'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken";

  export default {
    name: 'Home',
    data(){
      return{
        resp:"",
        newUser:false,
        registeredCourses:''
          
        //  "Covers/back3.png"
        
        // imgage:"../assets/Covers/back2.png"
      }
        
    },
    components: {
      Intro,MyRecentDocuments,MyCourses
    },
    created(){
       //on page load show all courses user is registered to
       console.log('sddd')
         var url='http://localhost:8000/course/user_registered/'
        
         this.$http.get(url).then(response => (this.registeredCourses = response.data['registered_courses: ']))
         console.log(this.registeredCourses)
        
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
     
    }
  }
</script>
<style scoped>
.homePageRow{
  height:100px;width:1000px;background-color:white
}
.image{
  padding:14%;
  box-shadow: 100px;
  
}
.circle-icon {
    background: lightgray;
    padding:30px;
    border-radius: 50%;
    height:50px;
    width:50px
}
.divStyle {
       transform:
    perspective(1250px)
        translate3d(0px, 0px, -250px)

    rotateX(-5deg)
    scale(0.9, 0.9);
  /* border-radius: 20px;
  border: 5px solid #e6e6e6; */
  transition: 0.4s ease-in-out transform;

}
  
</style>
