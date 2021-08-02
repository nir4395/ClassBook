<template>
<div>
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
 
</div>
  
  
  
</template>
<script>
  export default {
    data: () => ({
      tags: [
        'Most Views',
        'High Rankings',
        'Exams',
        'Homework',
        'Notes',
        'Presentitions',
      
        'Quiz',

        
      ],
    }),
  }
</script>
