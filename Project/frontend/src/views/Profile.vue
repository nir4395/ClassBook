<template>
<v-container>
      <v-card  style="width:5000px;" class="mx-auto" max-width="900" tile>
        
          <v-img height="100%" :src="require(`@/assets/${img}`)"></v-img>
             <v-img @click="editImage()" class="profilepicDiv" :src="require(`@/assets/${user}`)">
             </v-img>
            
              
          <!-- <v-col>
            <v-avatar size="100" style="position:absolute; top: 130px">
              <v-img src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"></v-img>
            </v-avatar>
          </v-col> -->
            <v-list-item color="rgba(0, 0, 0, .4)">'
              <v-list-item-content>
                <v-list-item-title class="title">Marcus Obrien</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
         
          
           
              

            
      </v-card>
     
      <v-divider></v-divider>
       <v-card  style="width:5000px;" class="mx-auto" max-width="900" tile>
      
           <ProfileDetails></ProfileDetails>
            <ChangeImage></ChangeImage>
           
          
           
              

            
      </v-card>
      </v-container>
 
    </template>
<script>
  import ProfileDetails from '../components/ProfileDetails.vue'
  import ChangeImage from '../components/Documents/ChangeImage.vue'
export default {
  components:{
    ProfileDetails,
    ChangeImage
  },
  methods:{
      editImage(){

      }
  },
    data(){
        return{
            img:'Covers/campus3.jpg',
            user:'userProfiles/profile2.jpg'
        }
    }
}
</script>
<style scoped>
    .profilepicDiv{
        margin-left: 27px;
    height: 100px;
    margin-top: -50px;
    width: 100px;
    border-radius: 50%;
   
}
    
</style>