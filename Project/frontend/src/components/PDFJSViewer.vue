<template>
<div>
  <iframe height="100%" width=100% src="http://mozilla.github.io/pdf.js/web/viewer.html" ></iframe>
  <!-- <iframe height="100%" width=100% src="http://mozilla.github.io/pdf.js/web/viewer.html?file=https://cors-anywhere.herokuapp.com/https://academdoc.co.il/materials/computer_science/year_1/%D7%97%D7%A9%D7%91%D7%95%D7%9F%20%D7%93%D7%99%D7%A4%D7%A8%D7%A0%D7%A6%D7%99%D7%90%D7%9C%D7%99%20%D7%95%D7%90%D7%99%D7%A0%D7%98%D7%92%D7%A8%D7%9C%D7%99%201/%D7%A1%D7%99%D7%9B%D7%95%D7%9E%D7%99%D7%9D/%D7%A1%D7%99%D7%9B%D7%95%D7%9D%202015.pdf" ></iframe> -->
   <v-rating class="mx-auto"
  background-color="grey lighten-1"
  color="yellow"
  hover
  length="5"
  size="50"
  value="4.5"
></v-rating>
</div>
</template>

<script>
import axios from 'axios'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken";

// import bus from '../main.js'
export default {
 name: 'PDFJSViewer',
  props: {
    fileName: String,
    path:String
  },
  computed:{ 
    getFilePath: () => {
      if(this.fileName!==''){
          console.log(this.path +'?file=' + this.fileName)
          return this.path +'?file=' + this.fileName
      }
      return this.path 
    }
  },
  methods:{
    askForPDF(){
    let headers = {
         "X-CSRFToken": axios.defaults.xsrfCookieName,
         "Content-Type": "application/x-www-form-urlencoded"
       }

    axios.get('http://localhost:8000/course/get/doc_id=2',
     headers)
    .then(response => (console.log(response.data)))
    console.log(this.info)

  }

  },
  created() {
//     bus.on('pagechanging', function pagechange(e) { 
//    console.log('pageNumber: ' + e.pageNumber + '\n' + 'previous: ' + e.previous)
// });
this.askForPDF()
    console.log('PDFJSViewer Created!!!!!!Yaaaa :)')

  }
}
</script>

<style scoped>
div {
   display: block;
  margin-left: 20%;
  margin-right: auto;
  /* display: flex; */
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 79vh;
  min-width: 200px;
}
</style>