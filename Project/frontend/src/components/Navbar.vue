<template>
  <nav>
    <v-app-bar app text>
      <v-app-bar-nav-icon
        @click="drawer = !drawer"
        style="margin-bottom:20px"
        class="black--text"
        ><v-icon>menu</v-icon></v-app-bar-nav-icon
      >
      <v-toolbar-title style="height:64px" class="text-uppercase grey--text">
        <span><img @click="Home()" class="logo" src="../assets/Covers/logo.png"/></span>
      </v-toolbar-title>

      <v-btn text color="grey">
        <span>
          <input
            ref="searchInput"
            @keypress="DoSearch($event)"
            type="text"
            class="form-control inputSearch"
            placeholder="Search for Documents and Courses..."
          />

          <!-- <input placeholder="Search" style="background-color:white;length:100px"> -->
        </span>
        <span class="material-icons-outlined">
          <v-icon
            style="margin-left: -46px;margin-top: -12px;"
            @click="Search()"
            >search</v-icon
          >
        </span>
      </v-btn>
      <span
        >Logout
        <v-icon @click="logout()">logout</v-icon>
      </span>

      <v-spacer></v-spacer>
    </v-app-bar>

    <v-navigation-drawer app v-model="drawer">
      <v-list>
        <v-list-item>
          <v-list-item-action>
            <div  class="mx-auto" style="width:100%">
           <img style="margin-left:50%;border-radius:200%;height:100px;width:100px" v-if="def!==null" :src="img" id="output" width="200" />
          <img style="border: 2px solid black"  v-else src="static/profile_pic/default.png" >
            </div>
             <div style="width:100%">
           <!-- <img style="border-radius:200%;height:100px;width:100px" v-if="def!==null" :src="img" id="output" width="200" />
          <img style="border: 2px solid black"  v-else src="http://localhost:8000/static/profile_pic/default.png" > -->

              <h3
                style="float: left;
    width: 30%;
    padding: 11%;
    margin-left: 36%;"
              >
                {{name}}
              </h3>
            </div>
            
          </v-list-item-action>
        </v-list-item>

        <v-list-item
          v-for="link in links"
          :key="link.text"
          router
          :to="link.route"
        >
          <v-list-item-action>
            <v-icon class="black--text">{{ link.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title class="black--text">{{
              link.text
            }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        

        <!-- <v-list-item
          style="color:black;font-size:20px;"
          href="http://localhost:8000/users/sign_up"
          target="_blank"
        >
          <v-list-item-action>
            <v-icon class="black--text">login</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title class="black--text">Sign Up</v-list-item-title>
          </v-list-item-content>
        </v-list-item> -->

        <v-list-item
          style="cursor:pointer;color:black;font-size:20px;"
         
        >
          <v-list-item-action>
            <v-icon class="black--text">search</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title class="black--text"> Advnaced Search</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>

<script>
const ENTER = 13;
export default {
  props:['name','def','img'],
  data() {
    return {
      // img: "userProfiles/pic2.jpg",
      results:'',
      drawer: false,
      links: [
        { icon: "home", text: "Home", route: "/" },
        { icon: "school", text: "Schools", route: "/schools" },
        // { icon: 'picture_as_pdf', text: 'Documents', route: '/doc' },
        // { icon: 'login', text: 'Login', route: '/login' },
        //  { icon: 'school', text: 'My Courses', route: '/mycourses' },
        // { icon: 'find_in_page', text: 'Document Selection', route: '/selection' },
        // { icon: 'doc', text: 'Documents', route: '/doc' },
        { icon: "person", text: "Profile", route: "/profile" },
        // { icon: 'school', text: 'Categories', route: '/nav' },
      ],
    };
  },
  methods: {
     async getData(query){
             const repsonse = await this.$http.get('documents/basic_search?q='+query)
             console.log(repsonse.data)
             this.results= repsonse.data
    },
    Home(){
        if (this.$route.path !== "/") {
        return this.$router.push({
          name: "Home",
          
        });
      } else {
        this.$router.go(this.$router.currentRoute);
      }
    },
    DoSearch(e) {
      if (e.keyCode == ENTER) {
        this.Search();
      }
    },

    async logout() {
      try {
        var url = "http://localhost:8000/users/sign_out/";

        await this.$http.get(url);
        window.location.href = "http://localhost:8000/users/sign_in";
      } catch (error) {
        console.log(error);
      }
    },
      
  async  Search() {
    var q = this.$refs["searchInput"].value;
    var query='' 
      var text=q.split(" ")
            for (var i=0;i<text.length;i++){
                query=query+text[i]+"+"
            }
           query= query.substring(0, query.length - 1);
      await this.getData(query)
      console.log("xxxxxxxxxxxxx")
      console.log(this.results)
       if (this.$route.path !== "/search") {
          return  this.$router.push({
          name: "SearchResults",
          params: { results: this.results },
       })
       }
       else{
         this.$route.params.query = this.results;
           this.$router.go(this.$router.currentRoute);
       }
     
        
     
       
    },
  },
};
</script>

<style></style>

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
<style scoped>
.inputSearch {
  margin-top: -7px;
  width: 1000px;
  margin-left: 50px;
}
.logo {
   cursor: pointer;
    margin-left: 27px;
    height: 92px;
    margin-top: -9px;
    padding: 5px;
    width: 168px;
}
</style>
