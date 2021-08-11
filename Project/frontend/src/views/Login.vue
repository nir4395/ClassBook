<template>
  <div style=" padding-left: 30px; float: left; height: 100%; width: 80%">
    <div style="text-align: left; padding-top: 50px;"><h1>Hey! Login Here</h1></div>
    <div class="loginBox">
      <form class="loginForm">
        <div style="margin-top: 10%" class="row">
          <div class="col-sm-3">
            <label for="exampleInputEmail1" class="form-label"
              >Email:</label
            >
          </div>
          <div class="col-sm-3">
            <input
              type="email"
              class="form-control"
              style="width: 280px;"
              id="exampleInputEmail1"
              aria-describedby="emailHelp"
            />
          </div>
        </div>
        <div style="margin-top: 5%" class="row">
          <div class="col-sm-3">
            <label for="exampleInputPassword1" class="form-label"
              >Password:</label
            >
          </div>
          <div class="col-sm-3">
            <input
              style="width: 280px;"
              type="password"
              class="form-control"
              id="exampleInputPassword1"
            />
          </div>
        </div>
        <div class="row">
          <button
            style="margin-left: 46%; margin-top: 4%"
            type="submit"
            class="btn btn-primary"
          >
            Submit
          </button>
        </div>
      </form>
      <div class="loginBoxImageBox">
        <!-- <img style="float:left" src='../assets/cover1.jpg'/> -->
        <img style="height: 100%; width: 100%" src="../assets/Covers/cover2.jpg" />
      </div>
      <div></div>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style scoped>

.loginForm {
  float: left;
  width: 55%;
  height: 100%;
}
.loginBoxImageBox {
  float: left;
  height: 100%;
  width: 20%;
  border-radius: 10%;
}
</style>