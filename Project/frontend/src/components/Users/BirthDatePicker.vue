<template>
  <v-row justify="center">
      
    <v-date-picker v-model="picker"></v-date-picker>
  </v-row>
</template>
<script>
  export default {
    created(){
        console.log(this.picker)
    },
    data () {
      return {
      //  selected: new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000).getMonth().toISOString(),
        picker: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      }
    },
    methods:{
        getDateAsText(){
                 var d=new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000).toString()
                 d=d.split(" ")
                 return d[1]+" "+d[2]+" "+d[3]
        }
       
    }
  }
</script>
