<template>
<div  class="mx-auto" style="height:1000px;width:1000px">
        <h1>Search Results: {{q}}</h1>
        <div>
           
        </div>
          <div style="height:100%;width:100%">
               <ul v-if="results.courses.length!=0" style="float:left" class="list-group">
     <li class="list-group-item active">Courses</li>     
  <li class="list-group-item">
      <v-row style="border-bottom:1px solid black" v-for="item in results.courses" :key="item">
            <v-col style=";border-right:1px solid black">{{item.name}}</v-col>
         
           <v-col style="border-right:1px solid black"> Members: {{item.student_count}}</v-col>
            <v-col style="border-right:1px solid black"> Date  Updated: {{showDate(item.date_created)}}</v-col>
              <v-col>Go to course page</v-col>
            <v-col><v-icon style="cursor:pointer" @click="goToCourse(item.name,item.id)">link</v-icon></v-col>
      
      </v-row>
     
  </li>
</ul>

   <ul  v-if="results.documents.length!=0" style="margin-top:10%;float:left" class="list-group">
            <li class="list-group-item active">Docuemnts</li> 
  <li class="list-group-item">
      {{results.documents}}
       <v-row style="border-bottom:1px solid black" v-for="item in results.documents" :key="item">
            <v-col  style="border-right:1px solid black" >
                <v-icon style="cursor:pointer"  @click="goToDocument(item.id, item.name,item.rating,item.doc_type)" color="red">{{getDocType(item.doc_type)}}</v-icon>{{item.name}}</v-col>
             <v-col  style="border-right:1px solid black"> Category {{item.category}}</v-col>
             <v-col  style="border-right:1px solid black"> Rating :{{item.rating}}</v-col>
             <v-col  style="border-right:1px solid black"> Views: {{item.view_count}}</v-col>
             <v-col  > Upload Date: {{showDate(item.upload_date)}}</v-col>

               
      </v-row>
  </li>
</ul>
          </div>
         
        <DocumentListing ref="docListing" :name="q" :docs="results"></DocumentListing>


</div>
</template>
<script>
 import DocumentListing from '../components/Documents/DocumentListing.vue'
export default {
    components:{
        DocumentListing
    },
    methods:{
             getDocType(value) {
      if (value === "cpp" || value == "cs") {
        return "code";
      }
      if (value === "pdf") {
        return "picture_as_pdf";
      }
      if (value === "docx" || value == "ppt") {
        return "description";
      }
             },
              showDate: function (date){
            return date.split('T')[0]
        },
             goToCourse(name,id){
                       return this.$router.push({
                name: "CourseCategorySelection",
                params: { courseName: name, courseID: id },
      });
             },
            goToDocument(id, name,rating,type){
                  if(type==='docx' || type==='ppt'){
         window.location.href='http://localhost:8000/course/get/doc_id='+id
      }
      else{

           console.log("this is the id " + id);
      // axios.get('http://localhost:8000/course/get/course_id=3/doc_id=3')
      // .then(response => (this.info = response.data))
      return this.$router.push({
        name: "DocumentPreview",
        params: {  id: id, name: name ,rating:rating,docType:type},
      });
            }
   
            }
    },
    data(){
        return{
                    ex4: ['red', 'indigo', 'orange', 'primary', 'secondary', 'success', 'info', 'warning', 'error', 'red darken-3', 'indigo darken-3', 'orange darken-3'],

            results:this.$route.params.results,
            search:'Operating Systems',
                res:[],
                //used for tests
            //    results:[{"id": 6, "name": "Summary", "doc_type": "pdf", "author_id": 4, "course_id": 3, "category": "summary", "view_count": 0, "rating": 5.0, "upload_date": "2021-08-08"}
            //   ,{"id": 6, "name": "Operating Systems Exam 1", "doc_type": "pdf", "author_id": 4, "course_id": 3, "category": "summary", "view_count": 0, "rating": 2.0, "upload_date": "2021-08-08"},
            //   {"id": 6, "name": "Bibi Is the king", "doc_type": "pdf", "author_id": 4, "course_id": 3, "category": "summary", "view_count": 0, "rating": 2.0, "upload_date": "2021-08-08"},

            //   {"id": 6, "name": "Summary", "doc_type": "pdf", "author_id": 4, "course_id": 3, "category": "summary", "view_count": 0, "rating": 3.0, "upload_date": "2021-08-08"},
            //   {"id": 6, "name": "Operating Systems 2", "doc_type": "pdf", "author_id": 4, "course_id": 3, "category": "summary", "view_count": 0, "rating": 3.0, "upload_date": "2021-08-08"},
            //   {"id": 6, "name": "Intro TO CS 1 Summary", "doc_type": "pdf", "author_id": 4, "course_id": 3, "category": "summary", "view_count": 0, "rating": 5.0, "upload_date": "2021-08-08"},
            //   {"id": 6, "name": "Intro TO CS 1 Summary Exam 2015", "doc_type": "pdf", "author_id": 4, "course_id": 3, "category": "summary", "view_count": 0, "rating": 5.0, "upload_date": "2021-08-08"},
            //   {"id": 6, "name": "Operating  in Diffuclt situations", "doc_type": "pdf", "author_id": 4, "course_id": 3, "category": "summary", "view_count": 0, "rating": 3.0, "upload_date": "2021-08-08"}
            //   ],
            
        }
    },
  
 
    watch: {
        '$route' () {
            this.q=this.$route.params.query
        }
    }
    
}
</script>