<template>
  <v-card class="pa-2" outlined tile>
    <v-row>
      <v-col color="gray">Profile details</v-col>
    </v-row>
    <v-divider></v-divider>

    <v-row>
      <v-col color="gray">
        <!-- <v-img
                class="mx-auto"
                height="100px"
                width="100px"
                style="border-radius:100%"
                :src="require(`@/assets/${user}`)"
              >
              </v-img> -->

        <div class="profile-pic">
          <label class="-label" for="file">
            <span class="glyphicon glyphicon-camera"></span>
            <span>Change Image</span>
          </label>
          <input id="file" type="file" @change="loadFile($event)" />
    
          <img v-if="isDeafultPic!==null" :src="img" id="output" width="200" />
          <img style="border: 2px solid black"  v-else src="static/profile_pic/default.png" >
        </div>
      </v-col>
      <v-col>
        <v-subheader class="mx-auto" color="gray">
          {{ userInfo.first_name }} {{ userInfo.last_name }}</v-subheader
        >
        <v-subheader class="mx-auto" color="gray">{{
          userInfo.email
        }}</v-subheader>
        <v-subheader class="mx-auto" color="gray">
          Date Joined {{ getJoinDate() }}</v-subheader
        >
      </v-col>
    </v-row>

    <v-row>
      <v-col>
        <label>First Name</label>

        <input
          id="firstNameInput"
          class="form-control"
          :value="userInfo.first_name"
      /></v-col>

      <v-col>
        <label>Last Name </label>
        <input
          id="lastNameInput"
          class="form-control"
          :value="userInfo.last_name"
      /></v-col>
    </v-row>
    <v-row>
      <v-col>
        <label ref="dudu">Birth date</label>

        <input type="date" id="birthdate" :value="birth" class="form-control" />
      </v-col>

      <v-col> </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-btn
          @click="changeProfileDetails()"
          style="border-radius:12%;color:white"
          color="blue"
          >Save Changes</v-btn
        >
      </v-col>
    </v-row>
  </v-card>
</template>
<script>
// import BirthDatePicker from '../components/Users/BirthDatePicker.vue'
// import ProfileImageUpdate from '../components/Users/ProfileImageUpdate.vue'
export default {
  props: ["userInfo", "birth", "img","isDeafultPic"],
  components: {
    //  ProfileImageUpdate
    //  BirthDatePicker
  },
  data() {
    return {
      //  img: "Covers/campus3.jpg",
      deafultImage:'userProfiles/deafultPic.png',
      imagePath: this.img,
      currentImage: "",
      // user: this.img.split('/')[0]
      user: "userProfiles/pic2.jpg",
      // user:'ClassBook\\Project\\profile_pictures\\default_profile_picture.jpg'
      //user: "userProfiles/profile2.jpg",
    };
  },

  methods: {
    loadFile(event) {
      console.log("xxxxxxxxx")
  //    var image = document.getElementById("output");
      this.currentImage = event.target.files[0];
     // image.src = URL.createObjectURL(event.target.files[0]);
      console.log("xxxxxxxxx")
      //     document.getElementById("file").files[0]=event.target.files[0]
      this.$emit("updateImage", {
        url: "userProfiles/" + this.currentImage.name,
        file: event.target.files[0],
      });
      // this.imagePath="userProfiles/"+this.currentImage.name
    },
    changeImageValue(value) {
      console.log("image change");
      this.img = value;
    },
    getJoinDate() {
      return this.userInfo.date_joined.split("T")[0];
    },
    getNewProfileImageDetails() {
      this.$refs["profileImage"].getImage();
      // var formDataProfile=new FormData()
      // formDataProfile.append()
    },
    async changeProfileDetails() {
      try {
        var firstName = document.getElementById("firstNameInput").value;
        var lastName = document.getElementById("lastNameInput").value;
        var birthDate = document.getElementById("birthdate").value;
        var dateValues = new Date(birthDate);
        dateValues = dateValues.toDateString().split(" ");
        dateValues = dateValues[1] + " " + dateValues[2] + " " + dateValues[3];
        var url =
          "http://localhost:8000/users/user_profile/change_profile_details";
        var data = {
          first_name: firstName,
          last_name: lastName,
          birth_date: dateValues,
        };

        const response = await this.$http.post(url, data);
        console.log(response);
     //   this.$forceUpdate();
this.$router.push('/profile')
        // this.$emit("profile")
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>
<style scoped>
.editimage {
  z-index: 39;
  height: 25px;
  width: 25px;
  border-radius: 100%;
  background-color: lightgreen;
  position: relative;
  margin-left: -572px;
  margin-top: -60px;
}
</style>
<style lang="scss" scoped>
@mixin object-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

$circleSize: 100px;
$radius: 100px;
$shadow: 0 0 10px 0 rgba(255, 255, 255, 0.35);
$fontColor: rgb(250, 250, 250);

.profile-pic {
  color: transparent;
  transition: all 0.3s ease;
  @include object-center;
  position: relative;
  transition: all 0.3s ease;

  input {
    display: none;
  }

  img {
    position: absolute;
    object-fit: cover;
    width: $circleSize;
    height: $circleSize;
    box-shadow: $shadow;
    border-radius: $radius;
    z-index: 0;
  }

  .-label {
    cursor: pointer;
    height: $circleSize;
    width: $circleSize;
  }

  &:hover {
    .-label {
      @include object-center;
      background-color: rgba(0, 0, 0, 0.8);
      z-index: 10000;
      color: $fontColor;
      transition: background-color 0.2s ease-in-out;
      border-radius: $radius;
      margin-bottom: 0;
    }
  }

  span {
    display: inline-flex;
    padding: 0.2em;
    height: 2em;
  }
}

/////////////////////////
// Body styling 🐾
/////////---------->

body {
  height: 100vh;
  background-color: rgb(25, 24, 21);
  @include object-center;

  a:hover {
    text-decoration: none;
  }
}
</style>

<script>
// import BirthDatePicker from '../components/Users/BirthDatePicker.vue'
// import ProfileImageUpdate from '../components/Users/ProfileImageUpdate.vue'
export default {
  props: ["userInfo", "birth", "img"],
  components: {
    //  ProfileImageUpdate
    //  BirthDatePicker
  },
  data() {
    return {
      //  img: "Covers/campus3.jpg",
      deafultImage:'userProfiles/deafultPic.png',
      imagePath: this.img,
      currentImage: "",
      // user: this.img.split('/')[0]
      user: "userProfiles/pic2.jpg",
      // user:'ClassBook\\Project\\profile_pictures\\default_profile_picture.jpg'
      //user: "userProfiles/profile2.jpg",
    };
  },

  methods: {
    loadFile(event) {
      var image = document.getElementById("output");
      this.currentImage = event.target.files[0];
      image.src = URL.createObjectURL(event.target.files[0]);
      //     document.getElementById("file").files[0]=event.target.files[0]
      this.$emit("updateImage", {
        url: "userProfiles/" + this.currentImage.name,
        file: event.target.files[0],
      });
      // this.imagePath="userProfiles/"+this.currentImage.name
    },
    changeImageValue(value) {
      console.log("image change");
      this.img = value;
    },
    getJoinDate() {
      return this.userInfo.date_joined.split("T")[0];
    },
    getNewProfileImageDetails() {
      this.$refs["profileImage"].getImage();
      // var formDataProfile=new FormData()
      // formDataProfile.append()
    },
    async changeProfileDetails() {
      try {
        var firstName = document.getElementById("firstNameInput").value;
        var lastName = document.getElementById("lastNameInput").value;
        var birthDate = document.getElementById("birthdate").value;
        var dateValues = new Date(birthDate);
        dateValues = dateValues.toDateString().split(" ");
        dateValues = dateValues[1] + " " + dateValues[2] + " " + dateValues[3];
        var url =
          "http://localhost:8000/users/user_profile/change_profile_details";
        var data = {
          first_name: firstName,
          last_name: lastName,
          birth_date: dateValues,
        };

        const response = await this.$http.post(url, data);
        console.log(response);
     //   this.$forceUpdate();
this.$router.push('/profile')
        // this.$emit("profile")
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>
<style scoped>
.editimage {
  z-index: 39;
  height: 25px;
  width: 25px;
  border-radius: 100%;
  background-color: lightgreen;
  position: relative;
  margin-left: -572px;
  margin-top: -60px;
}
</style>
<style lang="scss" scoped>
@mixin object-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

$circleSize: 100px;
$radius: 100px;
$shadow: 0 0 10px 0 rgba(255, 255, 255, 0.35);
$fontColor: rgb(250, 250, 250);

.profile-pic {
  color: transparent;
  transition: all 0.3s ease;
  @include object-center;
  position: relative;
  transition: all 0.3s ease;

  input {
    display: none;
  }

  img {
    position: absolute;
    object-fit: cover;
    width: $circleSize;
    height: $circleSize;
    box-shadow: $shadow;
    border-radius: $radius;
    z-index: 0;
  }

  .-label {
    cursor: pointer;
    height: $circleSize;
    width: $circleSize;
  }

  &:hover {
    .-label {
      @include object-center;
      background-color: rgba(0, 0, 0, 0.8);
      z-index: 10000;
      color: $fontColor;
      transition: background-color 0.2s ease-in-out;
      border-radius: $radius;
      margin-bottom: 0;
    }
  }

  span {
    display: inline-flex;
    padding: 0.2em;
    height: 2em;
  }
}

/////////////////////////
// Body styling 🐾
/////////---------->

body {
  height: 100vh;
  background-color: rgb(25, 24, 21);
  @include object-center;

  a:hover {
    text-decoration: none;
  }
}
</style>
