<template>
  <div class="about">
   


    <div class="container">
      <div style="margin-top:50px;" class="row">
      
        <div v-for="(year) in years-1" :key="year" @click="GoToCourses(year)" class="col-md-3 col-sm-6">
          
          <SchoolBox
            :name="text[year]"
            :img="getImage(year)"
          ></SchoolBox>
          <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
           <div  @click="GoToCourses(10)" class="col-md-3 col-sm-6">
          
          <SchoolBox
            :name="text[10]"
            :img="getImage(4)"
          ></SchoolBox>
          <!-- <SchoolBox  name="Bar Ilan University" img="ba.png"></SchoolBox> -->
        </div>
        
      </div>
      
    </div>
  </div>
</template>
<script>
import SchoolBox from "../components/SelectSchools/SchoolBox.vue";
import axios from "axios";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
export default {
  data() {
    return {
      text:{1:'First Year Courses'
      ,2:'Second Year Courses',
      3:'Third Year Courses',
      10:'Opt Courses'},
        name:'',
          years:'',
      ins: this.$route.params.ins,
      STAM:'',

      data: null,
    };
  },
  components: {
    SchoolBox,
  },

  methods: {
    getImage(value){
      return 'numbers/'+value+'.jpg'
    },
     async getData(year){
     
     var url = "course/ins/1/year/"+year;
     console.log(url)
      const response =    

  await  this.$http
      .get(url)
      console.log(response)
      this.STAM=response.data
    },
  
  async  GoToCourses(value) {
     await this.getData(value)
     
      console.log(this.text[value])
        //  var url = "course/ins/" + this.ins + "/year/" + this.year_code;
 return this.$router.push({name: "CoursesSelection",
  params:{
    courses:this.STAM,
    ins:this.ins,
    catName: this.text[value],
  }})


      // return this.$router.push({
      //   name: "CoursesSelection",
      //   params: {
      //     catName: this.text[year_code_param],

      //     ins: this.ins,
      //     yearCode: year_code_param,
        
      //   },
      // });
    },
    async getCatergories() {
     const response = await this.$http.get('academic_degrees/deg/2')
     this.name=response.data.name
     this.years=response.data.year_count

    },
  },
  //onload events
  created() {
    this.getCatergories();
  },
};
</script>
<style scoped></style>
