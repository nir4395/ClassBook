<template>

    <div class="drop-zone">
      <div>Upload Your Document Here</div>
      <div>
         <img style="height:100px;width:100px" src='../assets/upload.png'/>
      </div>
   
    <!-- <input type="file" name="myFile" class="drop-zone__input"> -->
  </div>


</template>
<script>
export default {
    
}
</script>
<style scoped>
    .drop-zone {
  max-width: 100%;
  height: 200px;
  padding: 25px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  font-family: "Quicksand", sans-serif;
  font-weight: 500;
  font-size: 20px;
  cursor: pointer;
  color: #cccccc;
  border: 4px dashed black;
  border-radius: 10px;

}
.drop-zone:hover{
    background: #C8ECF9;
}
    
.drop-zone--over {
  border-style: solid;
}

.drop-zone__input {
  display: none;
}

.drop-zone__thumb {
  width: 100%;
  height: 100%;
  border-radius: 10px;
  overflow: hidden;
  background-color: #cccccc;
  background-size: cover;
  position: relative;
}

.drop-zone__thumb::after {
  content: attr(data-label);
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 5px 0;
  color: #ffffff;
  background: rgba(0, 0, 0, 0.75);
  font-size: 14px;
  text-align: center;
}
</style>