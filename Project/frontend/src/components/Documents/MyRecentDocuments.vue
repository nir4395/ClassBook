<template>
  <v-container>
    
       <v-toolbar
      color="blue"
      dark
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Recently Viewed Docuemnts</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
    
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-checkbox-marked-circle</v-icon>
      </v-btn>
    </v-toolbar>
   
    <v-row
      v-for="n in 1"
      :key="n"
      :class="n === 1 ? 'mb-2' : ''"
      no-gutters
    >
      <v-col
        v-for="k in n + 4"
        :key="k"
      >
     <RecentDoc></RecentDoc>
     
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import RecentDoc from '../Documents/RecentDoc.vue'
export default {
    components:{
        RecentDoc
    }
    
}
</script>