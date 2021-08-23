<template>
  <v-container>
    <v-row class="mx-auto" style="height:600px;width:1000px">
      <div
        class="image"
        :style="{
          backgroundImage: 'url(' + require(`@/assets/${image}`) + ')',
          width: '100%',
          height: '100%',
        }"
      >
        <img
          src="../assets/Covers/large_studentsmarts.png"
          style="height:40px;width:40px"
        />
        <h1 class="mx-auto" style="color:black;margin-top:10px">
          All Your Study Materials in one place
        </h1>
        <p class="mx-auto lead" style="color:black">
          View,Upload Share and rate your course in few clicks a way
        </p>
      </div>
    </v-row>
    <v-row class="mx-auto homePageRow">
      <v-col><h3>Discover & Enjoy our Key features</h3></v-col>
    </v-row>
    <v-row class="mx-auto homePageRow">
      <v-col><v-icon color="black" class="circle-icon">school</v-icon></v-col>
      <v-col>View Study Materials</v-col>

      <v-col><v-icon color="#F5BB00" class="circle-icon">star</v-icon></v-col>
      <v-col>Rate Documents</v-col>
    </v-row>
    <v-row class="mx-auto homePageRow">
      <v-col
        ><v-icon color="blue" class="circle-icon">upload_file</v-icon></v-col
      >
      <v-col>Upload Files</v-col>

      <v-col
        ><v-icon color="black" class="circle-icon"
          >question_answer</v-icon
        ></v-col
      >
      <v-col>Discuss with your friends</v-col>
    </v-row>
  </v-container>
</template>
<script>
export default {
  data() {
    return {
      image: "Covers/campus2.jpg",
    };
  },
};
</script>
<style scoped>
.homePageRow {
  height: 100px;
  width: 1000px;
  background-color: white;
}
.image {
  padding: 14%;
  box-shadow: 100px;
}
.circle-icon {
  background: lightgray;
  padding: 30px;
  border-radius: 50%;
  height: 50px;
  width: 50px;
}
</style>
