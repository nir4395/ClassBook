<template>
  <div class="about">
    <h1></h1>


        <div class="container">
    <div  style="margin-top:50px;" class="row">
        <div class="col-md-3 col-sm-6">
            <SchoolBox  name="Computer Science" img="coding.png"></SchoolBox>
             
        </div>
        <div class="col-md-3 col-sm-6">
           <SchoolBox  name="Nursing" img="nurse.png"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
          <div class="col-md-3 col-sm-6">
           <SchoolBox  name="Economics And Managment" img="gdp.png"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
    </div>
    <div  style="margin-top:50px;" class="row">
        <div class="col-md-3 col-sm-6">
            <SchoolBox  name="Informatics" img="analysis.png"></SchoolBox>
             
        </div>
        <div class="col-md-3 col-sm-6">
           <SchoolBox  name="Physcology" img="think.png"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
          <div class="col-md-3 col-sm-6">
           <SchoolBox  name="Political Science" img="politics.png"></SchoolBox>
              <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
        <div><v-btn @click="SendLogin()">GO TO HOME PAGE</v-btn></div>
    </div>
</div>




    
  </div>
</template>
<script>
import SchoolBox from '../components/SelectSchools/SchoolBox.vue'
export default {
  components:{
    SchoolBox
  },
 
  
}
</script>
<style scoped>

</style>

