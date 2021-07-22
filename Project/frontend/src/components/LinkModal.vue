<template>
  <div >
    <div style="height:400px" class="modal">
      <header class="modal-header">
        <slot name="header">
       Add Your Link
        </slot>
        <button
          type="button"
          class="btn-close"
          @click="close"
        >
          x
        </button>
      </header>

      <section  class="modal-body">
        <slot  name="body">
         
        
          <div style="height:200px">
            <div style="height:50%">
               <label style="float:left">URL</label>
               <input  id="inputURL" style="float:left">
          </div>
          <div style="height:40%">
               <label style="float:left">Text</label>
                <input id="inputText" style="float:left">
          </div>
          <div style="height:10%">
            <button @click="getLink()" class="btn btn-secondary">Insert</button>
          </div>
        
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
    data(){
      return {
          linkInfo:{}
      }
    },
    name: 'Modal',
    methods: {
      close(value) {
        this.$emit('close',value);
      },
      getLink(){
        console.log("Sdfsfsf")
          var url=document.getElementById("inputURL").value
          var text=document.getElementById("inputText").value
          var value={url:url,text:text}
           this.$emit('close',value);
        
      },
      getLinkInfo(){
        return this.linkInfo
      }
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