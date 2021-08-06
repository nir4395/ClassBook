<template>
  <div class="commentstyle">{{commentText}}</div>
</template>

<script>
export default {
  
  props:['commentText']
 
  
}
</script>

<style>
.commentstyle{
   width: 55%;
    height: 14%;
    margin-left: 16%;
    margin-top: 15%;
    background-color: 023E8A;
    font-size: 20px;
    font-weight: bold;
    border-radius: 10px;
}
</style>