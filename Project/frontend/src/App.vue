<template>
  <v-app class="gray fontfam">
    <span class="bg"></span>
    <Navbar></Navbar>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import Navbar from "@/components/Navbar";
export default {
  name: "App",
  components: { Navbar },
  data: () => ({
    image2: "Covers/back2.jpg",
    //
  }),
};
</script>
<style scoped>
.bg {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  background: url("assets/Covers/back5.jpg") no-repeat center center;
  background-size: cover;
  /* background-color: gray; */
  transform: scale(1.1);
}
.fontfam {
  font-family: "Rubik", sans-serif;
}
</style>
