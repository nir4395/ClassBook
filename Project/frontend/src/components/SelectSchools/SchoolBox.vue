<template>
  

<div class="serviceBox white">
                <div style="padding:20px" class="service-content blue">
                    <div class="service-icon">
                      
                    </div>
                    <h3 class="title">{{name}}</h3>
                </div>
                 <div class="routeDiv"><router-link class="route"  to="/"></router-link> </div>
                <img  style="cursor:pointer" height="200" width="200"  @click="NavToPage()" :src="require(`@/assets/${img}`)">


                 
            </div>

       
   
</template>
<script>
export default {
    props:['name','img','href'],
    methods:{
            NavToPage(){
                  return this.$router.push('/schoolCourseNav');
            }
    }
}
</script>
<style scoped>
    .mainSchoolBoxDiv{
        height:400px;
        box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
        width:400px;
        padding:15px;
        border-radius: 10%;
        box-shadow: lightblue;
        /* background-color: gray; */
    }
    .serviceBox{
    background-color: #fff;
    font-family: 'Poppins', sans-serif;
    text-align: center;
    padding: 0 0 20px;
    border-radius: 20px;
    box-shadow: 0 0 15px -2px rgba(0,0,0,0.2);
}
.serviceBox .service-content{
    color: #fff;
    /* background: linear-gradient(to right,#E54A71, #F3235F); */
    padding: 22px 15px;
    margin: 0 0 20px;
    border-radius: 18px 18px 0 0;
}
.serviceBox .service-icon{
    font-size: 40px;
    line-height: 40px;
    margin: 0 0 12px;
}
.serviceBox .title{
    font-size: 20px;
    font-weight: 400;
    letter-spacing: 0.5px;
    text-transform: capitalize;
    margin: 0;
}
.serviceBox .description{
    color: #999;
    font-size: 14px;
    line-height: 24px;
    margin: 0 15px 15px;
}
.serviceBox .read-more{
    color: blue;
    transition: all 0.3s ease 0s;
}
.serviceBox .read-more:hover{ color: #555; }
.serviceBox.purple .service-content{ background: linear-gradient(to right, #0087C9, #0087C9); }
.serviceBox.purple .read-more{ color: #0670BC; }
.serviceBox.orange .service-content{ background: linear-gradient(to right, #FA9E0D, #FF5A1A); }
.serviceBox.orange .read-more{ color: #FF5A1A; }
.serviceBox.blue .service-content{ background: linear-gradient(to right, #0087C9, #0670BC); }
.serviceBox.blue .read-more{ color: #0670BC; }
@media only screen and (max-width: 990px){
    .serviceBox{ margin: 0 0 30px; }
}
</style>