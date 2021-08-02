<template>

  <v-parallax

  
      dark
      :src="image">
      <div>
    <v-container
      v-for="align in alignments"
      :key="align"
      class="grey lighten-5 mb-6"
    >
      <v-row
        :align="align"
        no-gutters
        style="height: 150px;"
      >
        <v-col
          v-for="n in 3"
          :key="n"
        >
          <v-card
            class="pa-2"
            outlined
            tile
          >
            One of three columns
          </v-card>
        </v-col>
      </v-row>
    </v-container>

    <v-container class="grey lighten-5">
      <v-row
        no-gutters
        style="height: 150px;"
      >
        <v-col>
         <v-btn color="yellow">Sign Up</v-btn>
        </v-col>
         <v-col>
         <v-btn>Login</v-btn>
        </v-col>
      </v-row>
    </v-container>
               

  </div>


      </v-parallax>

</template>

<script>
import axios from 'axios'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken";
  export default {
    name: 'Home',
    data(){
      return{
        resp:"",
        image: require("../assets/back3.png")
      }
        
    },
    components: {
    },
    methods:{
      GoTosignUp(){
        axios.get('http://localhost:8000/users/sign_up/')
            .then(function( response ){
                this.resp = response.data
            }.bind(this));
      console.log("1233")
       console.log(this.resp)
      
      },
      sendPostToSignIn(){
        let headers = {
         "X-CSRFToken": axios.defaults.xsrfCookieName,
         "Content-Type": "application/x-www-form-urlencoded"
       }
        axios
    .post('http://localhost:8000/users/sign_in/', {
      email : "test@gmail.com",
      username : 'test',
      password:'101duckontheroad',
      csrfmiddlewaretoken : '{{ csrf_token }}'
    },headers)
    .then(response => (this.info = response.data))
      }
    }
  }
</script>
<style scoped>
.mainDiv{
   background-image: url("../assets/user2.png") no-repeat center center
}
  
</style>
