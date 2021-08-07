<template>
    <div>
        <div style="width:100%;height:40%">

              <!-- {{name}} -->
                   <FiltersBar></FiltersBar>
        </div>
    
        <div  style="width:100%;height:500px ">

            <DocumentListing :cat="cat" :name="name"  :docs="docsInfo"></DocumentListing>
        </div>
       
       
        <!-- <v-divider></v-divider> -->
         <!-- <DocumentListing></DocumentListing> -->
           <!-- <v-divider></v-divider> -->
         <UploadModal></UploadModal>
       
    </div>
  
</template>
<script>
 import DocumentListing from '../components/Documents/DocumentListing.vue'
import FiltersBar from '../components/Documents/FiltersBar.vue'
import UploadModal from '../components/Documents/UploadModal.vue'
export default {

    data(){
        return{
            id:this.$route.params.courseID,
             name:this.$route.params.courseName,
             cat:this.$route.params.cat,
             docsInfo:'',
             ddddd:''
        }
    },
    methods:{
        getDocs(){
            return this.docs
        }
    },
    components:{
         DocumentListing,
        UploadModal,FiltersBar
    },

    created(){
        var url='http://localhost:8000/course/get/course_id='+this.id+'/cat='+this.cat
        
        this.$http.get(url).then(response => (this.docsInfo = response.data.documents))
       
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