<template>
  <v-container  class="grey lighten-5">
    <v-row style="height:1200px" no-gutters>
      <v-col style="height:100%" cols="6" md="4">
        <v-card class="pa-2" outlined tile>
          <v-row>
            <v-col style="font-weight:bold" color="gray">Edit Profile</v-col>
         
             <v-col><v-icon style="cursor:pointer" @click="showDetails()"> settings</v-icon></v-col>
          </v-row>
          <v-divider></v-divider>
          
            <v-row>
              
            <v-col >My Courses</v-col>
              <v-col><v-icon style="cursor:pointer" @click="showCourses()">school</v-icon></v-col>
              
          </v-row>
        
            <v-divider></v-divider>
            <v-row>
            <v-col>Logout</v-col>
              <v-col><v-icon @click="logout()">logout</v-icon></v-col>
          </v-row>
          <v-divider></v-divider>
          <v-row  style="height:289px">
         
          </v-row>
        </v-card>
      </v-col>
       <v-col style="height:100%"  cols="12" sm="6" md="8">
       
          <ProfileDetails :def="def"  @profile="getUsersInfo()" @updateImage="changeImage($event)" :img="img" :birth="birth" :userInfo="userData" v-if="details===true"></ProfileDetails>
          <MyCourses  v-if="courses===true" :courses="coursesData"></MyCourses>
       </v-col>
     
    
    </v-row>
  </v-container>
</template>
<script>
import ProfileDetails from '../components/ProfileDetails.vue'
import MyCourses from '../components/MyCourses.vue'

// import ChangeImage from '../components/Documents/ChangeImage.vue'
export default {
  components: {
    ProfileDetails,MyCourses
    //   ChangeImage
  },
 
  data(){
    return{
      birth:'',
      uerData:'',
      def:null,
      img:'',
      details:true,
      coursesData:'',
      courses:false
    }
  },
  created(){
    this.getUsersInfo()
  },
  methods:{
      async getUsersInfo() {
      try {
        var url = "users/user_profile/";
        const response = await this.$http.get(url);
        console.log(response)
        this.birth=response.data.profile_details.birth_date
        this.userData = response.data.profile_details.user;
        this.img=response.data.profile_details.picture_URL
        this.def=response.data.profile_details.picture_URL
      } catch (error) {
        console.log(error);
      }
    },
    async updateProfileImage(file){
        try {

        var url = "users/user_profile/upload_profile_picture";
        var data=new FormData();
        data.append("profile_picture",file)
        const response = await this.$http.post(url,data);

        console.log(response)
        this.getUsersInfo()
      } catch (error) {
        console.log(error);
      }
    },
   async  changeImage(value){
       console.log(this.img)
       console.log(value.url)
     await this. updateProfileImage(value.file)
    this.img=value.url
  },
    showDetails(){
       this.details=true
      this.courses=false
    },
    showCourses(){
      this.details=false
      this.courses=true
        var url='course/user_registered/'
        this.$http.get(url).then(response => (this.coursesData = response.data['registered_courses']))
      
    },
    
  async  logout(){
     try {
          var url = "users/sign_out/"

       await this.$http.get(url);
       window.location.href='users/sign_in'
       
     }
     catch(error){
       console.log(error)
     }
     
    },
    
  },
 
};
</script>
<style scoped>
.profilepicDiv {
  margin-left: 27px;
  height: 100px;
  margin-top: -50px;
  width: 100px;
  border-radius: 50%;
}
</style>
