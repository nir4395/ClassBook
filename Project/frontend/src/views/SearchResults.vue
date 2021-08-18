<template>
<div  class="mx-auto" style="height:1000px;width:1000px">
        <h1>Search Results: {{q}}</h1>
        <DocumentListing ref="docListing" :name="q" :docs="res"></DocumentListing>


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
            q:this.$route.params.query,
            search:'Operating Systems',
                res:[],
                //used for tests
               results:[{"id": 6, "name": "Summary", "doc_type": "pdf", "author_id": 4, "course_id": 3, "category": "summary", "view_count": 0, "rating": 5.0, "upload_date": "2021-08-08"}
              ,{"id": 6, "name": "Operating Systems Exam 1", "doc_type": "pdf", "author_id": 4, "course_id": 3, "category": "summary", "view_count": 0, "rating": 2.0, "upload_date": "2021-08-08"},
              {"id": 6, "name": "Bibi Is the king", "doc_type": "pdf", "author_id": 4, "course_id": 3, "category": "summary", "view_count": 0, "rating": 2.0, "upload_date": "2021-08-08"},

              {"id": 6, "name": "Summary", "doc_type": "pdf", "author_id": 4, "course_id": 3, "category": "summary", "view_count": 0, "rating": 3.0, "upload_date": "2021-08-08"},
              {"id": 6, "name": "Operating Systems 2", "doc_type": "pdf", "author_id": 4, "course_id": 3, "category": "summary", "view_count": 0, "rating": 3.0, "upload_date": "2021-08-08"},
              {"id": 6, "name": "Intro TO CS 1 Summary", "doc_type": "pdf", "author_id": 4, "course_id": 3, "category": "summary", "view_count": 0, "rating": 5.0, "upload_date": "2021-08-08"},
              {"id": 6, "name": "Intro TO CS 1 Summary Exam 2015", "doc_type": "pdf", "author_id": 4, "course_id": 3, "category": "summary", "view_count": 0, "rating": 5.0, "upload_date": "2021-08-08"},
              {"id": 6, "name": "Operating  in Diffuclt situations", "doc_type": "pdf", "author_id": 4, "course_id": 3, "category": "summary", "view_count": 0, "rating": 3.0, "upload_date": "2021-08-08"}
              ],
            
        }
    },
    created(){
            for(var index=0;index<this.results.length;index++){
                if(this.results[index].name.includes(this.q)){
                    this.res.push(this.results[index])
                }
            }
    }
    
}
</script>