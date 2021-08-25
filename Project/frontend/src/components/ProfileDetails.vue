<template>
 
        <v-card class="pa-2" outlined tile>
          <v-row>
            <v-col color="gray">Profile details</v-col>
          </v-row>
          <v-divider></v-divider>

          <v-row>
            <v-col color="gray">
              <!-- <v-img
                class="mx-auto"
                height="100px"
                width="100px"
                style="border-radius:100%"
                :src="require(`@/assets/${user}`)"
              >
              </v-img> -->
                <ProfileImageUpdate :img="user"></ProfileImageUpdate>
            
             
            
             
            </v-col>
            <v-col>
              <v-subheader class="mx-auto" color="gray">{{userInfo.first_name}}  {{userInfo.last_name}}</v-subheader>
               <v-subheader class="mx-auto" color="gray">{{userInfo.email}}</v-subheader>
                 <v-subheader class="mx-auto" color="gray"> Date Joined   {{getJoinDate() }}</v-subheader>
            </v-col>
          </v-row>

          <v-row>
            <v-col>
              <label>First Name</label>
              <input  id="firstNameInput" class="form-control" :value="userInfo.first_name"
            /></v-col>

            <v-col>
              <label>Last Name </label>
              <input id="lastNameInput" class="form-control" :value="userInfo.last_name"
            /></v-col>
          </v-row>
          <v-row>
            <v-col>
              <label ref="dudu">Birth date</label>
            
            
              <input type="date"  id="birthdate" :value="birth" class="form-control">
            </v-col>

            <v-col> </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-btn @click="changeProfileDetails()" style="border-radius:12%;color:white" color="blue"
                >Save Changes</v-btn
              >
            </v-col>
          </v-row>
        
        </v-card>
     
</template>
<script>
// import BirthDatePicker from '../components/Users/BirthDatePicker.vue'
import ProfileImageUpdate from '../components/Users/ProfileImageUpdate.vue'
export default {
  props:['userInfo','birth'],
 components: {
   ProfileImageUpdate
 //  BirthDatePicker

}, 
  data() {
    return {
      img: "Covers/campus3.jpg",
      user: "userProfiles/profile2.jpg",
    }
    

},

methods:{
   getJoinDate(){
       return this.userInfo.date_joined.split('T')[0]
    
   },
 async changeProfileDetails(){
    
     try {
          var firstName=document.getElementById("firstNameInput").value
          var lastName=document.getElementById("lastNameInput").value
          var birthDate=document.getElementById("birthdate").value
          var dateValues= new Date(birthDate)
          dateValues=dateValues.toDateString().split(" ")
          dateValues=dateValues[1]+" "+dateValues[2]+" "+dateValues[3]
          console.log(dateValues)
          var url = "http://localhost:8000/users/user_profile/change_profile_details"
          var data={'first_name':firstName,'last_name':lastName,'birth_date':dateValues}

          const response=  await this.$http.post(url,data);
          console.log(response)
       
   
     }
     catch(error){
       console.log(error)
     }
  }
}
}
</script>
<style scoped>
  .editimage {
  z-index: 39;
  height: 25px;
  width: 25px;
  border-radius: 100%;
  background-color: lightgreen;
  position: relative;
  margin-left: -572px;
  margin-top: -60px;
}
</style>