<template>
     <div class="panel-body bio-graph-info">
              <h1>Personal Information</h1>
              <div class="row">
                  <div class="bio-row">
                      <p><span>First Name </span>: Marcus</p>
                  </div>
                  <div class="bio-row">
                      <p><span>Last Name </span>: Obrien</p>
                  </div>
                  <div class="bio-row">
                      <p><span>Country </span>: Israel</p>
                  </div>
                  <div class="bio-row">
                      <p><span>Member Since</span>: 21 July 2020</p>
                  </div>
                
                  <div class="bio-row">
                      <p><span>Email </span>: marcu2196@mta.ac.il</p>
                  </div>
                   <div class="bio-row">
                      <p><span>School </span>: Computer Siecnce</p>
                  </div>
                  <div class="bio-row">
                      <p><span>Year </span>: Third</p>
                  </div>
                
               
              </div>
          </div>
</template>
<style scoped>
.bio-graph-heading {
    background: #fbc02d;
    color: #fff;
    text-align: center;
    font-style: italic;
    padding: 40px 110px;
    border-radius: 4px 4px 0 0;
    -webkit-border-radius: 4px 4px 0 0;
    font-size: 16px;
    font-weight: 300;
}

.bio-graph-info {
    color: #89817e;
}

.bio-graph-info h1 {
    font-size: 22px;
    font-weight: 300;
    margin: 0 0 20px;
}

.bio-row {
    width: 50%;
    float: left;
    margin-bottom: 10px;
    padding:0 15px;
}

.bio-row p span {
    width: 100px;
    display: inline-block;
}

.bio-chart, .bio-desk {
    float: left;
}

.bio-chart {
    width: 40%;
}

.bio-desk {
    width: 60%;
}

.bio-desk h4 {
    font-size: 15px;
    font-weight:400;
}

.bio-desk h4.terques {
    color: #4CC5CD;
}

.bio-desk h4.red {
    color: #e26b7f;
}

.bio-desk h4.green {
    color: #97be4b;
}

.bio-desk h4.purple {
    color: #caa3da;
}

</style>