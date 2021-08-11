<template>
    <div>
        <div style="width:100%;height:40%">

              <!-- {{name}} -->
                   <FiltersBar @showOnlyHighesrRanked="FilterData()"></FiltersBar>
        </div>
    
        <div  style="width:100%;height:500px ">

            <DocumentListing ref="docListing" :cat="cat" :name="name"  :docs="exampleDocs"></DocumentListing>
        </div>
       
       
        <!-- <v-divider></v-divider> -->
         <!-- <DocumentListing></DocumentListing> -->
           <!-- <v-divider></v-divider> -->
         <UploadModal></UploadModal>
       
    </div>
  
</template>
<script>
const HIGHEST_RANK=5.0
//const VIEWS_FILTER=10
 import DocumentListing from '../components/Documents/DocumentListing.vue'
import FiltersBar from '../components/Documents/FiltersBar.vue'
import UploadModal from '../components/Documents/UploadModal.vue'
export default {

    data(){
        return{
            id:this.$route.params.courseID,
             name:this.$route.params.courseName,
             cat:this.$route.params.cat,
             //filteredDocs:'',
             exampleDocs:[{"id": 2, "name": "Homework_3", "doc_type": "pdf", "author_id": 2, "course_id": 2, "category": "homework", "view_count": 3, "rating": 5.0, "upload_date": "2021-08-08"},
                          {"id": 3, "name": "Homework_5", "doc_type": "pdf", "author_id": 2, "course_id": 2, "category": "homework", "view_count": 32, "rating": 3.0, "upload_date": "2021-08-08"},
                          {"id": 3, "name": "Homework_5", "doc_type": "pdf", "author_id": 2, "course_id": 2, "category": "homework", "view_count": 4, "rating": 3.0, "upload_date": "2021-08-08"},
                          {"id": 2, "name": "Homework_3", "doc_type": "pdf", "author_id": 2, "course_id": 2, "category": "homework", "view_count": 1239, "rating": 5.0, "upload_date": "2021-08-08"},
                          {"id": 3, "name": "Homework_5", "doc_type": "pdf", "author_id": 2, "course_id": 2, "category": "homework", "view_count": 23423, "rating": 5.0, "upload_date": "2021-08-08"},
                          {"id": 3, "name": "Homework_5", "doc_type": "pdf", "author_id": 2, "course_id": 2, "category": "homework", "view_count": 55, "rating": 2.0, "upload_date": "2021-08-08"},
                          {"id": 2, "name": "Homework_3", "doc_type": "pdf", "author_id": 2, "course_id": 2, "category": "homework", "view_count": 12, "rating": 5.0, "upload_date": "2021-08-08"},
                          {"id": 3, "name": "Homework_5", "doc_type": "pdf", "author_id": 2, "course_id": 2, "category": "homework", "view_count": 2344, "rating": 5.0, "upload_date": "2021-08-08"},
                          {"id": 3, "name": "Homework_5", "doc_type": "pdf", "author_id": 2, "course_id": 2, "category": "homework", "view_count": 33, "rating": 5.0, "upload_date": "2021-08-08"},
                          ],
             docsInfo:'',
             ddddd:''
        }
    },
    methods:{
        getDocs(){
            return this.docs
        },
        //numeric sorter for a given array of docuemnt JSON array, iterates the obejct and sorts acording to given key
        sortData(data,key){
            data.sort(function(firstDocuemnt, secondDocument) {
    return parseFloat(firstDocuemnt[key]) - parseFloat(secondDocument[key]);
            })
        },
        FilterData(){
            var filteredDocs=[]
            console.log("was called by filters bar")
            for  (var i=0;i<this.exampleDocs.length;i++){
                    if(this.exampleDocs[i].rating===HIGHEST_RANK){
                        filteredDocs.push(this.exampleDocs[i])
                    }
            }
            //update the proprety with the filtered infomartion
            this.sortData(filteredDocs,'view_count')
            this.exampleDocs=filteredDocs
            //this.$refs['docListing'].$props["docs"]=filteredDocs
        }
    },
    components:{
         DocumentListing,
        UploadModal,FiltersBar
    },

    created(){
        var url='http://localhost:8000/course/get/course_id='+this.id+'/cat='+this.cat
        
        this.$http.get(url).then(response => (this.docsInfo = response.data.documents
        ))
        this.filteredDocs=this.docsInfo
       
    },
    computed:{
        getName(){
            return this.$route.params.courseName
        },
         getID(){
            return this.$route.params.courseID
        },
         getcat(){
            return this.$route.params.cat
        }
    }
    
    
}
</script>
<style scoped>
.uploadButton{
        background-color: red;
    padding: 5%;
    margin-left: 84%;
    margin-top: 5%;
}
</style>