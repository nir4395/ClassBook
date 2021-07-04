<template>
  <div >
    <div class="modal">
      <header class="modal-header">
        <slot name="header">
       Rank document
        </slot>
        <button
          type="button"
          class="btn-close"
          @click="closeModal"
        >
          x
        </button>
      </header>

      <section class="modal-body">
        <slot  name="body">
          
            <div style="    margin-left: 15%;
    float: left;
    width: 77%;">
    <img style="height:40px;width:40px" src='../assets/stars.png'/>
    <img style="height:40px;width:40px" src='../assets/stars.png'/>
    <img style="height:40px;width:40px" src='../assets/stars.png'/>
    <img style="height:40px;width:40px" src='../assets/stars.png'/>
    <img style="height:40px;width:40px" src='../assets/stars.png'/>
         <select style="margin-top:3%" class="form-control" id="sel1">

          <option>1</option>
            <option>2</option>
              <option>3</option>
                <option>4</option>
                  <option>5</option>
        </select>
                          <span><button class="button">Sumbit</button></span>

        </div>
        </slot>
       </section>

      <footer class="modal-footer">
        <slot name="footer">
        </slot>
        <button class="button"
          type="button"
         
          @click="closeModal"
        >
          Close Modal
        </button>
      </footer>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'RankModal',
    methods: {
      closeModal() {
          console.log("close it")
        this.$emit('close');
      },
    },
  };
</script>
<style scoped>
  .modal-backdrop {
     height: 200px;
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
      height: 300px;
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