<template>
    <div>
        <div style="width:100%;height:40%">
              
                   <FiltersBar></FiltersBar>
        </div>
    
        <div  style="width:100%;height:500px ">
            <DocumentListing></DocumentListing>
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
    components:{
         DocumentListing,
        UploadModal,FiltersBar
    },
    
    
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