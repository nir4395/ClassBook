<template>
  <v-container>  
         <v-toolbar
      color="blue"
      dark
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Recently Viewed Docuemnts</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
    
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-checkbox-marked-circle</v-icon>
      </v-btn>
    </v-toolbar>
  
    <div class="row">
    
      <div  style="height:300px;width:400px;margin-top:10px;margin-left:none;overflow-x:auto" v-for="item in docs" :key="item.id" class="col-md-4">
        <div class="card card-1">
            
            
                    <!-- style="display:flex" v-for="star in 5" :key="star" -->
                     <span>
                            <v-icon  v-for="star in item.rating" :key="star" color="yellow">star</v-icon>
                     </span>

            
          
          <p>
            <v-icon color="red " style="cursor:pointer"  @click="goToDocument(item.id,item.name,item.rating,item.doc_type)">{{getDocType(item.doc_type)}}</v-icon>
            {{ item.name }}
          </p>
           
        
            <div style="font-size:16px;font-weight:bold" class="row"><div style="margin-top:10px" class="col-md-6 mx-auto" > {{ item.course_name}}</div></div>
            <v-divider></v-divider>
              <div class="row">
                  <div  style="margin-top:10px;font-size:16px"  class="  col-md-6 mx-auto" >Exams {{ item.category}}
                  </div>
                 
                  </div>
        </div>
        
        
        
      </div>
      
    </div>
  </v-container>
</template>
<script>
export default {
  props: ["docs"],
  methods:{
    getDocType(value){
      if(value==='cpp' || value=='cs'){
        return 'code'
      }
      if(value==='pdf'){
        return 'picture_as_pdf'
      }
      if(value==='docx' || value=='ppt'){
        return 'description'
      }
    },
     goToDocument(id, docName,rating,type) {
      if(type==="docx" || type=='ppt'){
         window.location.href='http://localhost:8000/course/get/doc_id='+id
      }
      else{

        //   console.log("this is the id " + id);
      // axios.get('http://localhost:8000/course/get/course_id=3/doc_id=3')
      // .then(response => (this.info = response.data))
      return this.$router.push({
        name: "DocumentPreview",
        params: {  id: id, name: docName ,rating:rating,docType:type},
      });
        //should be rendered after url is changed
         
      }
    

      // return this.$router.push({ name: 'DocumentPreview', params: { id:id}});
    },
  },
  data() {
    return {
      l: ["a", "b", "c","d"],
    };
  },
};
</script>
<style scoped>
body {
  font-family: "Nunito", sans-serif;
  padding: 50px;
}
.card {
 
  border-radius: 4px;
  background: #fff;
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.08), 0 0 6px rgba(0, 0, 0, 0.05);
  transition: 0.3s transform cubic-bezier(0.155, 1.105, 0.295, 1.12),
    0.3s box-shadow,
    0.3s -webkit-transform cubic-bezier(0.155, 1.105, 0.295, 1.12);
  padding: 14px 80px 18px 36px;
  cursor: pointer;
}

.card:hover {
  transform: scale(1.05);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.12), 0 4px 8px rgba(0, 0, 0, 0.06);
}

.card h3 {
  font-weight: 600;
}

.card img {
  position: absolute;
  top: 20px;
  right: 15px;
  max-height: 120px;
}

.card-1 {

  /* background-image: url("../assets/pdf.png"); */
  height: 100%;
  width:100%;
  background-repeat: no-repeat;
  background-position: right;
  background-size: 80px;
}

.card-2 {
  background-image: url(https://ionicframework.com/img/getting-started/components-card.png);
  background-repeat: no-repeat;
  background-position: right;
  background-size: 80px;
}

.card-3 {
  background-image: url(https://ionicframework.com/img/getting-started/theming-card.png);
  background-repeat: no-repeat;
  background-position: right;
  background-size: 80px;
}

@media (max-width: 990px) {
  .card {
    margin: 20px;
  }
}
</style>
