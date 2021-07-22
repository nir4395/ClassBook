<template>
  <div class="about">
    <h1></h1>


        <div class="container">
    <div  style="margin-top:50px;" class="row">
       
        <div class="col-md-3 col-sm-6">
           <SchoolBox  name="First Year Courses" img="math.png"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
          <div class="col-md-3 col-sm-6">
           <SchoolBox  name="Second Year Courses" img="memory.png"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
    </div>
    <div  style="margin-top:50px;" class="row">
     
        <div class="col-md-3 col-sm-6">
           <SchoolBox  name="Third Year Courses" img="stor.png"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
          <div class="col-md-3 col-sm-6">
           <SchoolBox  name="Selection Courses" img="mobile.png"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
    </div>
</div>




    
  </div>
</template>
<script>
import SchoolBox from '../components/SelectSchools/SchoolBox.vue'
export default {
  components:{
    SchoolBox
  }
}
</script>
<style scoped>

</style>

