<template>
    <!-- <v-container>
      
     
<v-card width="500px" v-for="category in courseCategories.categories" :key="category"
  elevation="24"
  outlined
  shaped
  tile
>
<v-card-title>{{ category }}</v-card-title>
<v-card-subtitle> Browse Documents<v-icon  @click="gotoDocuments(category)" color="blue">description</v-icon></v-card-subtitle>
</v-card>
</v-container> -->
<div>
   <CourseCard v-for="category in courseCategories.categories" :key="category" :name="category" @nav="gotoDocuments(category)"></CourseCard>
    <!-- <v-container>
     <v-row>
       <v-card  style="margin-left:50px;margin-top:50px" width="500px" v-for="category in courseCategories.categories" :key="category"
  elevation="24"
  outlined
  shaped
  tile
>
<v-card-title>{{ category }}</v-card-title>
<v-card-subtitle> Browse Documents<v-icon  @nav="gotoDocuments(category)" color="blue">description</v-icon></v-card-subtitle>
</v-card>
     </v-row>
    </v-container> -->

  
  </div>


</template>

<script>
import CourseCard from '../Courses/CourseCard.vue'
export default {
  components: {
    CourseCard
  
  },
    props:['courseCategories','name','id'],
    methods:{
            gotoDocuments(categroy){
                    return this.$router.push({ name: 'DocumentSelection', params: { cat:categroy,courseName:this.name, courseID: this.id } })
            }
    },
     data: () => ({
      alignments: [
        'start',
        'center',
        'end',
      ],
    }),
}
</script>