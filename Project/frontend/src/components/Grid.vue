<template>
   <div id="app1">
  
    <ul :style="gridStyle" class="card-list">
         <li  v-for="(category) in data" :key="category" >
   
      <CourseCard   :name="category"  @nav="gotoDocuments(category)" ></CourseCard>
    </li>
          
      

  </ul>
  
</div>
</template>
<script>
import CourseCard from '../components/Courses/CourseCard.vue'
export default {
    props:['data','name','id'],
    components:{
            CourseCard
    },
    data(){
        return{
            numberOfColumns:2,
            cards:[1,2]
        }
    },
    methods:{
           gotoDocuments(categroy){
                    console.log(this.name)
                    return this.$router.push({ name: 'DocumentSelection', params: { cat:categroy,courseName:this.name, courseID: this.id } })
            }
    },
     computed: {
    gridStyle() {
      return {
        gridTemplateColumns: `repeat(${this.numberOfColumns}, minmax(100px, 1fr))`
      }
    },
     },
}
</script>
<style scoped>
.card-list {
  display: grid;
  grid-gap: 1em;
}

.card-item {
  background-color: dodgerblue;
  padding: 2em;
}

body {
  background: #20262E;
  padding: 20px;
  font-family: Helvetica;
}

#app1 {
  /* background: #fff; */
  border-radius: 4px;
  padding: 20px;
  transition: all 0.2s;
}

ul {
  list-style-type: none;
}
</style>