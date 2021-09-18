<template>
  <v-container>
    <v-toolbar color="blue" dark>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>{{ name }} - {{ cat }} </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon> </v-btn>

      <v-btn icon>
        <v-icon>mdi-checkbox-marked-circle</v-icon>
      </v-btn>
    </v-toolbar>
    <v-card v-for="doc in docs" :key="doc.name">
      <v-list-item-group>
        <template>
          <v-list-item width="1000px" :key="doc.id">
            <template>
              <v-list-item-action>
                <v-icon color="red">{{ getIconForDocType(doc.doc_type)}}</v-icon>
              </v-list-item-action>

              <v-list-item-content style="width:500px">
                <v-list-item-title
                  width="100px"
                  v-text="doc.name"
                ></v-list-item-title>
                <v-list-item-subtitle
                  v-text="showDate(doc['upload_date'])"
                ></v-list-item-subtitle>
              </v-list-item-content>

              <v-list-item-content>
                <v-list-item-title
                  v-text="doc['author_id']"
                ></v-list-item-title>
              </v-list-item-content>
              <v-list-item-content>
                <v-list-item-title
                  v-text="doc['view_count']"
                ></v-list-item-title>
                <v-icon color="blue">visibility</v-icon>
              </v-list-item-content>
              <v-list-item-content>
                <v-list-item-title v-text="doc.rating"></v-list-item-title>
                <v-icon color="#FFD600">star</v-icon>
              </v-list-item-content>
              <v-list-item-action>
                <v-icon @click="goToDocument(doc.id, doc.name,doc.rating,doc.doc_type)" cursor="pointer"
                  >open_in_new</v-icon
                >
              </v-list-item-action>
            </template>
          </v-list-item>
        </template>
      </v-list-item-group>
    </v-card>
  </v-container>
</template>
<script>
import axios from "axios";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
const DOC='docx'
const ICONS={'cpp':'code','pdf':'picture_as_pdf','docx':'doc','cs':'code'}
const PPT='ppt'
export default {
  props: ["docs", "name", "cat"],

  methods: {
    showDate: function(date) {
      return date.split("T")[0];
    },
     getIconForDocType(docType){
        switch(docType){
          case 'pdf':
            return ICONS['pdf']
        
        case 'cpp':
          return ICONS['cpp']
            case 'cs':
          return ICONS['cpp']
        default:
          return 'description'
        }
    },
    goToDocument(id, docName,rating,type) {
      if(type===DOC || type==PPT){
         window.location.href='course/get/doc_id='+id
      }
      else{

           console.log("this is the id " + id);
    
      return this.$router.push({
        name: "DocumentPreview",
        params: {  id: id, name: docName ,rating:rating,docType:type},
      });
        //should be rendered after url is changed
         
      }
    

      // return this.$router.push({ name: 'DocumentPreview', params: { id:id}});
    },
    showDocumentsSelectionData() {
      let headers = {
        "X-CSRFToken": axios.defaults.xsrfCookieName,
        "Content-Type": "application/x-www-form-urlencoded",
      };
      axios
        .post(
          "course/get/course_id=2/cat=homework",
          {
            email: "test@gmail.com",
            username: "test",
            password: "101duckontheroad",
            csrfmiddlewaretoken: "{{ csrf_token }}",
          },
          headers
        )
        .then((response) => (this.info = response.data));
      console.log(this.info);
    },
  },
  created() {
    this.showDocumentsSelectionData();

    console.log("Component has been created!");
  },

  //  data: () => ({
  //    z:22,
  // info:'',
  //  y:this.x,
  //  docsData:[
  //    {name:'Calculus 1 -Exam 2019 Term A First Exam 2019.2.3',author:'Marina Slovotichx',views:34,rating:4,uploadDate:"2019-08-16T08:37:09.098Z",lastComment:'20.6.2021'},
  //    {name:'Calculus 1 -Exam 2019 Term A  Second Exam  2019.29.3',author:'Gal Braun',views:122,rating:4,uploadDate:'2021-06-16T08:37:09.098Z',lastComment:'20.6.2021'},
  //    {name:'Calculus 1 -Exam 2021 Term B  First Exam  2021.7.6',author:'Tomer Shavit',views:23,rating:5,uploadDate:'2021-08-16T02:37:09.098Z',lastComment:'20.7.2021'},
  //    {name:'Calculus 1 -Exam 2021 Term B  Second Exam  2021.8.6',author:'Tomer Shavit',views:5,rating:5,uploadDate:'2021-01-01T08:37:09.098Z',lastComment:'31.7.2021'},
  //  ],
  //  }),
  data() {
    return {
      // name:this.name,
      z: 4444,
      //     docsData:[
      //    {name:'Calculus 1 -Exam 2019 Term A First Exam 2019.2.3',author:'Marina Slovotichx',views:34,rating:4,upload_date:"2019-08-16T08:37:09.098Z",lastComment:'20.6.2021'},
      //    {name:'Calculus 1 -Exam 2019 Term A  Second Exam  2019.29.3',author:'Gal Braun',views:122,rating:4,upload_date:'2021-06-16T08:37:09.098Z',lastComment:'20.6.2021'},
      //    {name:'Calculus 1 -Exam 2021 Term B  First Exam  2021.7.6',author:'Tomer Shavit',views:23,rating:5,upload_date:'2021-08-16T02:37:09.098Z',lastComment:'20.7.2021'},
      //    {name:'Calculus 1 -Exam 2021 Term B  Second Exam  2021.8.6',author:'Tomer Shavit',views:5,rating:5,upload_date:'2021-01-01T08:37:09.098Z',lastComment:'31.7.2021'},
      //  ],
    };
  },
};
</script>
