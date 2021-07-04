<template>

    <div class="mainSelectionDiv">
        
        <div style="margin-bottom:5%;font-size:55px" class="jumbotron jumbotron-fluid">Document Selection
               
                <img style="position:absloute;height:100px;width:100px;background-color:white" src='../assets/docs.jpg'/>
        </div>
        <FiltersBar></FiltersBar>
         <div style="width:100%;hegight:30%;padding:1%">
              <DragNdrop></DragNdrop>
        </div>
         <toggle-button @change="LoadPreview()"><span>dfg</span></toggle-button>
         <div >{{status}}</div>
        <div ref="gallery" style="height:80%;background-color:lightgray;width:100%">
             
            
            <!-- <div><button @click="LoadDataAsGallery()" class="button">Add Gallery</button></div> -->
               
        </div>
       
      
       
        <!-- <div class="mainPapersSection">
            <SingleDocSelect></SingleDocSelect>
                <hr>
          <SingleDocSelect></SingleDocSelect>
            <hr>
              <SingleDocSelect></SingleDocSelect>
              <hr>
        </div> -->
        
    </div>
</template>
<script>
import ToggleButton from 'vue-js-toggle-button'
Vue.use(ToggleButton)
import SingleDocSelect from '../components/SingleDocSelect.vue'
import DragNdrop from '../components/DragNdrop.vue'
import LoadingBox from '../components/LoadingBox.vue'
import FiltersBar from '../components/FiltersBar.vue'
import ListItemDoc from '../components/ListItemDoc.vue'
 import Vue from 'vue'

export default {
  
    data(){
    //   this.galleryOrList='ffffffffffff'
                            this.galleryOrList="List"

return{
            staticDocumentsData:{
                listPreview:true,
                galleryPreivew:false,
                docs:[
                    {'name':'PDF1.pdf','img':'doc1.png','author':'Daniel Greenbaum','date':'Few Hours ago','stars':4},
                    {'name':'PDF2.pdf','img':'doc2.png','author':'Daniel Greenbaum','date':'Few Hours ago','stars':3},
                    {'name':'PDF3.pdf','img':'doc3.png','author':'Elad Noy','date':'Yesterday','stars':2},
                    {'name':'PDF4.pdf','img':'doc4.png','author':'Guy Ronen','date':'Today','stars':5}
                    // {'name':'PDF5.pdf','img':'doc1.png','author':'Daniel GreenBaum','date':'Few Hours ago'},
                    // {'name':'PDF6.pdf','img':'doc2.png','author':'Daniel GreenBaum','date':'Few Hours ago'},
                    // {'name':'PDF7.pdf','img':'doc3png','author':'Elad Noy','date':'Yesterday'},
                    // {'name':'PDF8.pdf','img':'doc4.png','author':'Jeff Brown','date':'Old'},
                ]
            }
        }
    },
    computed: {
    // a computed getter
    status: function () {
      // `this` points to the vm instance
     this.x='3'
      if(this.listPreview===true){
            this.galleryOrList="fd"
          return "List preview"
      }
      else{
           this.galleryOrList="Gallery"
          return "Gallery Preview"
      }
    }
  },
    components:{
        FiltersBar,
        // SingleDocSelect,
        // ListItemDoc,
        // LoadingBox,
        DragNdrop
        
    },
    methods:{
        LoadPreview(){
          var mainDiv=   this.$refs.gallery
          mainDiv.querySelectorAll('*').forEach(n => n.remove());
            if(this.listPreview===true){
                    this.LoadDataAsList()
                    this.listPreview=false
                 //   this.galleryOrList='Gallery View'

            }
            else{
                this.LoadDataAsGallery()
                 this.listPreview=true
              //   this.galleryOrList='List View'
            }
        },
        createSingleListItemDocuemnt(info){
                   var ComponentClass = Vue.extend(ListItemDoc)
                 var newDocument = new ComponentClass({
                    propsData: {name:info.name,
                    img:info.img,
                    author:info.author,
                    date:info.date,
                    stars:info.stars
                

    }})
      return newDocument
        },
        createSingleDocument(info){

              var ComponentClass = Vue.extend(SingleDocSelect)
                 var newDocument = new ComponentClass({
                    propsData: {name:info.name,
                    img:info.img,
                    author:info.author,
                    date:info.date,stars:info.stars
                

    }})
      return newDocument
        },
        LoadDataAsGallery(){
            
            var row=document.createElement("div")
            row.className="row"
            row.style.marginLeft="8%"
            var i
            var data=this.staticDocumentsData.docs
            console.log(data[0])
            console.log("here")
            for ( i= 0; i < data.length; i++) {
                var newDocument=this.createSingleDocument(data[i])
                newDocument.$mount() // pass nothing
                row.appendChild(newDocument.$el)
                this.$refs.gallery.appendChild(newDocument.$el)
        }
    },
    LoadDataAsList(){
        var i
            var data=this.staticDocumentsData.docs
            console.log(data[0])
            console.log("here")
            for ( i= 0; i < data.length; i++) {
                var newDocument=this.createSingleListItemDocuemnt(data[i])
                newDocument.$mount() // pass nothing
                // row.appendChild(newDocument.$el)
                this.$refs.gallery.appendChild(newDocument.$el)
        }
    
    }
    

}
}
</script>
<style scoped>
.mainSelectionDiv{
  
    height:2000px;
    width:2000px;
    
  
}
.mainPapersSection{
    position: absolute;
    padding: -28%;
    height: 70%;
    width: 96%;
    border-radius: 5%;
    border: 1px gray solid;
    background-color: white;
    margin: 4% 1% 1% 1%;
}
.move{
    margin-left:8%
}
</style>