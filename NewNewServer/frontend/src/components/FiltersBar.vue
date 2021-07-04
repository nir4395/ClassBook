<template>
  <div class="mainFilterDiv">
      <div style="margin-left:8%;height:50%;width:100%">
          <div style="float:left" class=col-sm-2><h2 style="text-align:center">Filters</h2></div>
           <div style="float:left" class=col-sm-4>
               <div style="float:left">
                      <div class="btn-group btn-group-toggle" role="group" aria-label="Basic example">
      

                        <button class="button">All Documents</button>
                        <button class="button" >Top Rated</button>
                          <button class="button ">Newest</button>
                     <button class="button ">Oldest</button>
                        <button class="button ">Tests</button>
 
</div>
               </div>
               n
           </div>
      \
      </div>
       <div style="height:50%;width:100%">
           <div style="float:left" class=col-sm-4></div>
          <div style="margin-left:12%;float:left" class=col-sm-2>
              <input   class="form-control form-control-lg form-control-borderless" type="search" placeholder="Search topics or keywords">             
          </div>
           <div  style="border-color: #76B3FA;float:left" class="col-auto"><button  style="backgrround:#76B3FA" class="btn btn-lg btn-success" type="submit">Search</button></div>
         <div style="float:left" class="col-sm-1">
                <select  style="width:100%;height:47px" class="form-control">
           <option>2021</option>
          <option>2020</option>
            <option>2019</option>
              <option>2018</option>
                <option>2017</option>
                  <option>2016</option>
        </select>
          </div>
            <div style="float:left" class="col-sm-1">
                <select   style="width:100%;height:47px" class="form-control">

          <option>With Soulotions</option>
            <option>Without Soloutions</option>
              <option>School Soulotions</option>
                <option>Tofes 0</option>
              
        </select>
          </div>
           <div style="float:left" class="col-sm-1">
                <select  style="width:100%;height:47px" class="form-control">

          <option>All Terms</option>
            <option>Fall Term</option>
              <option>Spring Term</option>
                <option>Summer Term</option>
                
        </select>
          </div>
           
            <div style="float:left" class="col-sm-1">
                <select  style="width:100%;height:47px" class="form-control">

          <option>First Year Course</option>
            <option>Second Year Course</option>
              <option>Third Year Course</option>
                <option>After Third Year</option>
               
                
        </select>
          </div>
             <div style="float:left" class="col-sm-1">
            <button style="background: #76B3FA" class="btn btn-lg btn-success" type="submit">Apply</button></div>
       </div>
      </div>
  
</template>

<script>
export default {

}
</script>

<style>
.mainFilterDiv{
    margin-top:3%;
    height:10%;
    width:100%;
    
}
.filterselect{
  
    width: 20%;
    height: 47px;
}
</style>