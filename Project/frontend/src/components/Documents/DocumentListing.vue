<template>
  <v-container>
   <v-toolbar
      color="blue"
      dark
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>{{name}} - {{cat}}  </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
    
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-checkbox-marked-circle</v-icon>
      </v-btn>
    </v-toolbar>
     <v-card v-for="doc in docs" :key="doc.name">
         <v-list-item-group
        v-model="selected"
        active-class="pink--text"
        multiple
      >
        <template>
          <v-list-item width="1000px" :key="doc.id">
            <template >
                          <v-list-item-action>
               <v-icon color="red">picture_as_pdf</v-icon>
               
              </v-list-item-action>

                <v-list-item-content style="width:500px">
                <v-list-item-title  width="100px" v-text="doc.name"></v-list-item-title>
                <v-list-item-subtitle v-text="doc['upload_date']" ></v-list-item-subtitle>
              </v-list-item-content>
                
                 <v-list-item-content>
                <v-list-item-title v-text="doc['author_id']"></v-list-item-title>
              </v-list-item-content>
               <v-list-item-content>
                <v-list-item-title v-text="doc['view_count']"></v-list-item-title>
                <v-icon color="blue">visibility</v-icon>
              </v-list-item-content>
                <v-list-item-content>
                <v-list-item-title v-text="doc.rating"></v-list-item-title>
                 <v-icon color="#FFD600" >star</v-icon>
              </v-list-item-content>
              
               <!-- <v-list-item-content>
                <v-list-item-title v-text="item.lastComment"><h1>Last Comment</h1></v-list-item-title>
              </v-list-item-content> -->
               





              <v-list-item-action>
               <v-icon  @click="goToDocument()" cursor="pointer">open_in_new</v-icon>
           

          
              </v-list-item-action>
            </template>
          </v-list-item>

        </template>
      </v-list-item-group>
     </v-card>
     </v-container>
   <!-- <v-container>
  <v-card v-for="doc in docs" :key="doc.name"
 
    class="mx-auto"
    max-width="1000"
  >
  <h1>{{docs}}</h1>
    <v-toolbar
      color="blue"
      dark
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>{{name}} - Exams  </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
    
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-checkbox-marked-circle</v-icon>
      </v-btn>
    </v-toolbar>

    <v-list two-line>
      <v-list-item-group
        v-model="selected"
        active-class="pink--text"
        multiple
      >
        <template v-for="(doc, index) in docs">
          <v-list-item width="1000px" :key="doc.id">
            <template >
                          <v-list-item-action>
               <v-icon color="red">picture_as_pdf</v-icon>
               
              </v-list-item-action>

                <v-list-item-content style="width:500px">
                <v-list-item-title  width="100px" v-text="doc.name"></v-list-item-title>
                <v-list-item-subtitle v-text="item.uploadDate" ></v-list-item-subtitle>
              </v-list-item-content>
                
                 <v-list-item-content>
                <v-list-item-title v-text="item.author"></v-list-item-title>
              </v-list-item-content>
               <v-list-item-content>
                <v-list-item-title v-text="item.views"></v-list-item-title>
                <v-icon color="blue">visibility</v-icon>
              </v-list-item-content>
                <v-list-item-content>
                <v-list-item-title v-text="item.rating"></v-list-item-title>
                 <v-icon color="#FFD600" >star</v-icon>
              </v-list-item-content>
              
               <v-list-item-content>
                <v-list-item-title v-text="item.lastComment"><h1>Last Comment</h1></v-list-item-title>
              </v-list-item-content>
               





              <v-list-item-action>
               <v-icon  @click="goToDocument()" cursor="pointer">open_in_new</v-icon>
           

          
              </v-list-item-action>
            </template>
          </v-list-item>

          <v-divider
            v-if="index < items.length - 1"
            :key="index"
          ></v-divider>
        </template>
      </v-list-item-group>
    </v-list>
  </v-card> -->

</template>
<script>
import axios from 'axios'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken";

  export default {
    props:['docs','name','cat'],
      methods:{
        
        goToDocument(){
        
              // axios.get('http://localhost:8000/course/get/course_id=3/doc_id=3')
              // .then(response => (this.info = response.data))
                return this.$router.push('/doc');
        
        
      },
      showDocumentsSelectionData(){
    let headers = {
         "X-CSRFToken": axios.defaults.xsrfCookieName,
         "Content-Type": "application/x-www-form-urlencoded"
       }
              axios
    .post('http://localhost:8000/course/get/course_id=2/cat=homework', {
      email : "test@gmail.com",
      username : 'test',
      password:'101duckontheroad',
      csrfmiddlewaretoken : '{{ csrf_token }}'
    },headers)
    .then(response => (this.info = response.data))
    console.log(this.info)

  },
      },
      created() {
        this.showDocumentsSelectionData()
    console.log('Component has been created!')
      },
  
    //  data: () => ({
    //    z:22,
    // info:'',
    //  y:this.x,
    //  docsData:[
    //    {name:'Calculus 1 -Exam 2019 Term A First Exam 2019.2.3',author:'Marina Slovotichx',views:34,rating:4,uploadDate:'6.6.2020',lastComment:'20.6.2021'},
    //    {name:'Calculus 1 -Exam 2019 Term A  Second Exam  2019.29.3',author:'Gal Braun',views:122,rating:4,uploadDate:'6.6.2020',lastComment:'20.6.2021'},
    //    {name:'Calculus 1 -Exam 2021 Term B  First Exam  2021.7.6',author:'Tomer Shavit',views:23,rating:5,uploadDate:'6.6.2020',lastComment:'20.7.2021'},
    //    {name:'Calculus 1 -Exam 2021 Term B  Second Exam  2021.8.6',author:'Tomer Shavit',views:5,rating:5,uploadDate:'19.7.2020',lastComment:'31.7.2021'},
    //  ],
    //  }),
    data(){
      return {
        // name:this.name,
        z:4444
      }
    }
  
  }
</script>