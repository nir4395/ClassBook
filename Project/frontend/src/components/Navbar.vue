<template>
  <nav>

    <v-app-bar app text>
      <v-app-bar-nav-icon
 @click="drawer = !drawer" class="grey--text"></v-app-bar-nav-icon
>
      <v-toolbar-title style="height:64px" class="text-uppercase grey--text">
         <span><img height="36" width="36" src="../assets/classbookLogo.png" ></span>
        <span style="margin-left:8px;font-size:20px" class="color:gray;font-weight-light">CLASS</span>
        <span style="font-size:20px;color:#007bff">BOOK</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn  text color="grey">
        <span>Sign Out</span>
        <v-icon right>exit_to_app</v-icon>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer app v-model="drawer" class="primary">
      <v-list>
        <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
          <v-list-item-action>
            <v-icon class="white--text">{{ link.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <h1>{{bobo}}</h1>
            <v-list-item-title class="white--text">{{ link.text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

  </nav>
</template>

<script>

export default {
  data() {
    
    return {
      drawer: false,
      links: [
        { icon: 'home', text: 'Home', route: '/' },
        { icon: 'school', text: 'Schools', route: '/about' },
        { icon: 'picture_as_pdf', text: 'Documents', route: '/doc' },
        { icon: 'login', text: 'Login', route: '/login' },
          { icon: 'find_in_page', text: 'Document Selection', route: '/selection' },
          { icon: 'login', text: 'Sign Up', route: '/signup' },
          
          

        
      ]
    }
  }
}
</script>

<style>
</style>



<!-- <v-toolbar flat app>
      <v-toolbar-title class="text-uppercase grey--text">
          <span><img height="36" width="36" src="../assets/classbookLogo.png" ></span>
        <span style="margin-left:8px" class="color:gray;font-weight-light">Class</span>
        <span style="color:cyan">BOOK</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn flat color="grey">
        <span>Sign Out</span>
        <v-icon right>exit_to_app</v-icon>
      </v-btn>
    </v-toolbar> -->