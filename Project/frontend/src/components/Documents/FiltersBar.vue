<template>

 <v-container fluid>
    <v-row align="center">
      <v-col cols="3">
        <v-subheader>
          Select Filters:
        </v-subheader>
      </v-col>

      <v-col cols="2">
        <v-select
         
          :items="itemsRanking"
          item-text="state"
          item-value="abbr"
          label="Ranking"
          persistent-hint
          return-object
          single-line
        ></v-select>
      </v-col>
       <v-col cols="2">
        <v-select
          
          :items="itemsNew"
          item-text="state"
          item-value="abbr"
          label="Views"
          persistent-hint
          return-object
          single-line
        ></v-select>
      </v-col>
       <v-col cols="2">
        <v-select
        
          :items="itemsViews"
          item-text="state"
          item-value="abbr"
          label="Upload Date"
          persistent-hint
          return-object
          single-line
        ></v-select>
      </v-col>
       <v-col cols="2">
        <v-select @change="ApplyFilters($event)"
        
          :items="filters"
          item-text="state"
          item-value="abbr"
          label="Show Only"
          persistent-hint
          return-object
          single-line
        ></v-select>
      </v-col>
     
    </v-row>
    <v-row>
      <v-col>
        <v-toolbar
      flat
      color="transparent"
    >
      <v-btn icon>
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>

      <v-text-field
         width="20px"
        
        append-icon="mdi-magnify"
        label="Search Documents In This course"
        single-line
      ><v-icon>magnify</v-icon></v-text-field>
    </v-toolbar>
      </v-col>
    </v-row>
  </v-container>
<!-- <div>

  <v-row justify="space-around">
    <v-col
      cols="12"
      sm="10"
      md="8"
    >
      <v-sheet
        elevation="10"
        class="py-4 px-1"
      >
        <v-chip-group 
          multiple
          active-class="primary--text"
        >
        <v-chip><v-icon>clear</v-icon></v-chip>
          <v-chip
            v-for="tag in tags"
            :key="tag"
          >
            {{ tag }}
          </v-chip>
         <v-btn border-radius="50%" color="cyan">Apply Filters</v-btn>
        </v-chip-group>
        
      </v-sheet>
      
   
  
    </v-col>
   
   
  </v-row>
  <v-toolbar
      flat
      color="transparent"
    >
      <v-btn icon>
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>

      <v-text-field
         width="20px"
        
        append-icon="mdi-magnify"
        label="Search Documents In This course"
        single-line
      ><v-icon>magnify</v-icon></v-text-field>

    </v-toolbar>
 

</div> -->

  
  
  
</template>
<script>

  // export default {
  //   data: () => ({
  //     tags: [
  //       'Most Views',
  //       'High Rankings',
  //       'Exams',
  //       'Homework',
  //       'Notes',
  //       'Presentitions',
      
  //       'Quiz',

        
  //     ],
  //   }),
  // }

 export default {
    data () {
      return {
      
        itemsRanking: [
          { state: 'Ranking High to Low'},
          { state: 'Ranking Low to High'},
          
        ],
        filters: [
          { state: ' 10 Highest ranked'},
          { state: ' 10  Most viewed'},
           { state: '10  Lastest uploaded'},
          
        ],
          itemsViews: [
          { state: 'Views High to Low' },
          { state: 'Views Low to High'},
          
        ],
        itemsNew: [
          { state: 'Uploaded Newest to Oldest'},
          { state: 'Ranking Oldest to Newest'},
          
        ],
      }
    },
    methods:{
        ApplyFilters(value){
          var selected= value.state
          console.log(selected)
          if(selected===' 10 Highest ranked'){
            //fire filter event for top ranked
            console.log("going to fire event!!!!")
            this.$emit('showOnlyHighesrRanked');
          }

        }
    }
  }

</script>
