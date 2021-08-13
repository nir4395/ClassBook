<template>
  <div style="border:3px dashed black;height:70%;width:100%">
    <vue-dropzone
ref="myVueDropzone"
:useCustomSlot="true"
id="dropzone"

@vdropzone-upload-progress="uploadProgress"
:options="dropzoneOptions"
@vdropzone-file-added="fileAdded"
@vdropzone-sending-multiple="sendingFiles"
@vdropzone-success-multiple="success"
></vue-dropzone>
 <v-btn
            color="blue darken-1"
            text
           @click="accFiles()"
          >
            Accept Files
          </v-btn>
  </div>
</template>

<script>
import vue2Dropzone from 'vue2-dropzone';
import 'vue2-dropzone/dist/vue2Dropzone.min.css';
export default {
  props:['id'],
  name: 'App',
  components: {
    vueDropzone: vue2Dropzone
  },
  data: function () {
    return {
      dropzoneOptions: {
          url: 'https://httpbin.org/post',
          thumbnailWidth: 150,
          maxFiles: 1,
          maxFilesize: 1,
          headers: { "My-Awesome-Header": "header value" }
      }
    }
  },
  methods:{
      accFiles(){
        var fileData=this.$refs.myVueDropzone.getAcceptedFiles()
        console.log(fileData[0])
        var idOfCourse=this.$props['id']
        var bodyFormData = new FormData();
        bodyFormData.append('file', fileData[0]);
        bodyFormData.append('course_id', idOfCourse);
        
          var url='http://localhost:8000/course/upload_file/'
        
        this.$http.post(url,bodyFormData).then(response => (console.log(response.data))
        )
      }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
