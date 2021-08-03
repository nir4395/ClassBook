<template>
  <v-app class="gray">
    <Navbar></Navbar>
    <!-- <pdf src="..\assets\comp1.pdf"></pdf> -->
    
  <v-btn blue>GO TO SIGN UP</v-btn>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import Navbar  from '@/components/Navbar'
export default {
  name: 'App',
  components:{Navbar},
  data: () => ({
    //
  }),
};
</script>
<style scoped>

</style>
