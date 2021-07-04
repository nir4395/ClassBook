<template>
  <div >
    <div class="modal">
      <header class="modal-header">
        <slot name="header">
       Rating Details
        </slot>
        <button
          type="button"
          class="btn-close"
          @click="close"
        >
          x
        </button>
      </header>

      <section class="modal-body">
        <slot  name="body">
          <div  class="progressbarDiv">
            <div style="float:left">Rating: 4/5</div> 
          <div style="margin-left:2%;float:left">
          
        <span class="fa fa-star checked"></span>
            <span class="fa fa-star checked "></span>
            <span class="fa fa-star checked"></span>
            <span class="fa fa-star checked"></span>
            <span class="fa fa-star"></span>
        </div>
          </div>
           
          <div class="progressbarDiv">
              <div style="float:left;width:30%">5 Stars</div>
          <div class="progress progresbarstyles">
            <div  style="width:65%" class="progress-bar bg-warning" role="progressbar" aria-valuenow="65" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
           <div style="float:left">65</div>
          </div>
          <div   class="progressbarDiv">
              <div style="float:left;width:30%">4 Stars</div>
          <div class="progress progresbarstyles">
            <div   style="width:32%" class="progress-bar bg-warning" role="progressbar" aria-valuenow="32" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
           <div style="float:left">32</div>
          </div>
          <div  class="progressbarDiv">
              <div style="float:left;width:30%">3 Stars</div>
          <div class="progress progresbarstyles">
            <div  style="width:47%" class="progress-bar bg-warning" role="progressbar" aria-valuenow="47" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
           <div style="float:left">47</div>
          </div>
          <div  class="progressbarDiv">
              <div style="float:left;width:30%">2 Stars</div>
          <div  class="progress progresbarstyles">
            <div style="width:5%" class="progress-bar bg-warning" role="progressbar" aria-valuenow="5" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
           <div style="float:left">5</div>
          </div>
          <div  class="progressbarDiv">
              <div style="float:left;width:30%">1 Stars</div>
          <div class="progress progresbarstyles">
            <div   style="width:12%" class="progress-bar bg-warning" role="progressbar" aria-valuenow="12" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
           <div style="float:left">12</div>
          </div>
          
          
        </slot>
       </section>

      <footer class="modal-footer">
        <slot name="footer">
        </slot>
        <button class="button"
          type="button"
         
          @click="close"
        >
          Close Modal
        </button>
      </footer>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'Modal',
    methods: {
      close() {
        this.$emit('close');
      },
    },
  };
</script>
<style scoped>
  .modal-backdrop {
     height: 600px;
    width: 500px;
     margin-left: 20%;
       margin-top: 20%;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1040;
    width: 475px;
    height: 439px;
    margin-left: 30%;
  }
  .progresbarstyles{
        margin-top: 1%;
    width: 55%;
    margin-left: 2%;
    float: left;
    margin-right: 3%;
  }

  .modal {
  
     margin-top: 10%;
    margin-left: 30%;
      height: 500px;
    width: 500px;
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
  }

  .modal-header,
  .modal-footer {
    padding: 15px;
    display: flex;
  }

  .modal-header {
    position: relative;
    border-bottom: 1px solid #eeeeee;
    color: #76B3FA;
    justify-content: space-between;
  }

  .modal-footer {
    border-top: 1px solid #eeeeee;
    flex-direction: column;
    justify-content: flex-end;
  }

  .modal-body {
    position: relative;
    padding: 20px 10px;
  }

  .btn-close {
    position: absolute;
    top: 0;
    right: 0;
    border: none;
    font-size: 20px;
    padding: 10px;
    cursor: pointer;
    font-weight: bold;
    color: #76B3FA;
    background: transparent;
  }

  .btn-green {
    color: white;
    background: #4AAE9B;
    border: 1px solid #4AAE9B;
    border-radius: 2px;
  }
  .progressbarDiv{
    width:100%;height:16%
  }
</style>