<template>
 <div id="sep1" class="sep">
             <div  rating class="recDocRating">
        <span class="fa fa-star checked"></span>
            <span class="fa fa-star checked "></span>
            <span class="fa fa-star checked"></span>
            <span class="fa fa-star checked"></span>
            <span class="fa fa-star"></span>
        </div>
            <a href="http://www.africau.edu/images/default/sample.pdf">  <img data-pdf-thumbnail-file="../assets/example.pdf"
         :src="require(`@/assets/${thumbNailsrc}`)" class="itemThumb"> </a></div>


</template>
<script>
export default {
    props:['thumbNailsrc','pdf']
}
</script>
<style scoped>
.sep:hover{
    background-color: gray;
}
.sep{
    height: 120%;
    width:14%;
    border: 2px black solid;
    
    background-color: #313638;
    float:left
}
.itemThumb{
    width:100%;
    height:100%;
    padding: 5%;
}
.recDocRating{
        background: lightgoldenrodyellow;
    position: absolute;
    margin-top: -9%;
    margin-left: 2%;
    float: left;
    margin-top: 1%;
}


</style>