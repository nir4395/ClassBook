<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
       
           color="#007bff"
      class="ma-2 white--text"
          v-bind="attrs"
          v-on="on"
        >
         <v-icon  right
        dark>file_upload</v-icon>
           Upload File
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="text-h5">Drag Your File Here</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
                <!-- <img src="../assets/stor.png" draggable="true"/>
                    <div  id="dropPDF" class="dropzone" @dragenter;.prevent @dragover.prevent @drop="HandleUpload($event)" dropzone style="height:200px;width:100%;border:3px dashed  black;border-radius:5px">
                        <v-icon  color="red" class="iconPDF">picture_as_pdf</v-icon>
                         </div> -->
                         <Dropzone :id="id" :cat="cat"></Dropzone>

            
              
             
            
            
           
            </v-row>
          </v-container>
        
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="dialog = false"
          >
            Close
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="dialog = false"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>
import Dropzone from '../Documents/Dropzone.vue'
  export default {
    props:['id','cat'],
      components:{
          Dropzone
      },
      methods:{
          HandleUpload(e){
                console.log(e)
                console.log("Dropped me!")
          }
      },
    data: () => ({
      dialog: false,
      
      
    }),
  }
  
</script>
<style scoped>
    .iconPDF{
            margin-top: 11%;
    /* padding: 58px; */
    /* height: 400px; */
    font-size: 68px;
    margin-left: 40%;
    }
</style>