<template>
    <div style="background-color:lightgray;height:2000px;width:1500px">
        <div style="float:left;height:100%;width:80%">
            <div style="width:100%:height:10%"><h1>Login</h1></div>
            <div class="loginBox">
               
                         <form class="loginForm">
                    <div  style="margin-top:5%" class="row">
                        <div class="col-sm-3"><label for="exampleInputEmail1" class="form-label">Email address</label></div>
                         <div class="col-sm-3"><input type="email" class="form-control" style="width:600px;border-radius:5%" id="exampleInputEmail1" aria-describedby="emailHelp"></div>
                    </div>
                     <div  style="margin-top:5%" class="row">
                        <div class="col-sm-3">  <label for="exampleInputPassword1" class="form-label">Password</label></div>
                         <div class="col-sm-3"> <input  style="width:600px;border-radius:5%" type="password" class="form-control" id="exampleInputPassword1"></div>
                    </div>
                    <div class="row">
                       <button style="margin-left: 46%;margin-top: 4%;" type="submit" class="btn btn-primary">Submit</button>
                    </div>
                </form>
                  <div class="loginBoxImageBox">
             <!-- <img style="float:left" src='../assets/cover1.jpg'/> -->
               <img style="height:100%;width:100%" src='../assets/cover2.jpg'/>
         </div>
                <div>
                   
                
                </div>
               
            

            </div>
        </div>
        

    </div>
</template>
<script>
export default {
    
}
</script>
<style scoped>
.loginBox{
    margin-top:4%;width:100%;height:20%;background-color:white;padding:2%;margin-left:4%;border-radius:3%
}
.loginForm{
    float:left;width:85%;height:100%
}
.loginBoxImageBox{
    float:left;height:100%;width:15%;border-radius:10%
}
</style>