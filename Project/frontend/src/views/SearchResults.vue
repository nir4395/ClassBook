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
         
           <v-col style="border-right:1px solid black"> Particinpts: {{item.student_count}}</v-col>
            <v-col style="border-right:1px solid black"> Date  Updated: {{item.date_created}}</v-col>
              <v-col>Go to course page</v-col>
            <v-col><v-icon>link</v-icon></v-col>
      
      </v-row>
     
  </li>
</ul>

   <ul  v-if="results.documents.length!=0" style="margin-top:10%;float:left" class="list-group">
            <li class="list-group-item active">Docuemnts</li> 
  <li class="list-group-item">
      
       <v-row style="border-bottom:1px solid black" v-for="item in results.documents" :key="item">
            <v-col  style="border-right:1px solid black" >
                <v-icon color="red">code</v-icon>{{item.name}}</v-col>
             <v-col  style="border-right:1px solid black"> Category {{item.category}}</v-col>
             <v-col  style="border-right:1px solid black"> Rating :{{item.rating}}</v-col>
             <v-col  style="border-right:1px solid black"> Views: {{item.view_count}}</v-col>
             <v-col  > Upload Date: {{item.category}}</v-col>

               
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