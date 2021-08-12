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
        <!-- <v-col>
         <v-btn color="yellow">Sign Up</v-btn>
        </v-col>
         <v-col>
         <v-btn @click="SendLogin()">Login</v-btn>
        </v-col> -->
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
      }
        
    },
    components: {
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

  
</style>
