<template>
  <v-card
    class="mx-auto"
    max-width="1000"
  >
    <v-toolbar
      color="blue"
      dark
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>{{info['course name']}} - Documents </v-toolbar-title>

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
        <template v-for="(item, index) in info.documents">
          <v-list-item :key="item.doc_id">
            <template >
              <v-list-item-content>
                <v-list-item-title v-text="item.name"></v-list-item-title>

                <v-list-item-subtitle
                  class="text--primary"
                  v-text="item.headline"
                ></v-list-item-subtitle>

          
               <span>{{item.view_count}}  Views</span>
               <span>{{item.rating}} <v-icon>star</v-icon></span>
              </v-list-item-content>

              <v-list-item-action>
               <v-icon  @click="goToDocument()" cursor="pointer">folder</v-icon>
                <v-list-item-action-text v-text="item.rating">
                  <v-icon>star</v-icon>
                </v-list-item-action-text>

                <!-- <v-icon
                  v-if="!active"
                  color="grey lighten-1"
                >
                  mdi-star-outline
                </v-icon>

                <v-icon
                  v-else
                  color="yellow darken-3"
                >
                  star
                </v-icon> -->
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
  </v-card>
</template>
<script>
import axios from 'axios'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken";
  export default {
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
    console.log('Component has been created!');
  },
    data: () => ({
    info:'',
      selected: [2],
      items: [
        {
          action: '15 min',
          headline: 'Brunch this weekend?',
          subtitle: `I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
          title: 'Ali Connors',
        },
        {
          action: '2 hr',
          headline: 'Summer BBQ',
          subtitle: `Wish I could come, but I'm out of town this weekend.`,
          title: 'me, Scrott, Jennifer',
        },
        {
          action: '6 hr',
          headline: 'Oui oui',
          subtitle: 'Do you have Paris recommendations? Have you ever been?',
          title: 'Sandra Adams',
        },
        {
          action: '12 hr',
          headline: 'Birthday gift',
          subtitle: 'Have any ideas about what we should get Heidi for her birthday?',
          title: 'Trevor Hansen',
        },
        {
          action: '18hr',
          headline: 'Recipe to try',
          subtitle: 'We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
          title: 'Britta Holt',
        },
      ],
    }),
  }
</script>