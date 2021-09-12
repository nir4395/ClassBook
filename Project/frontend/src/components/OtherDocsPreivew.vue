<template>
  <VueDocPreview
    style="border:1px solid black"
    :mdStyle="mdStyle"
    type="code"
    :url="getURL()"
  />
  <!-- <VueDocPrevi ew value="newteach.pbworks.com%2Ff%2Fele%2Bnewsletter.docx" type="office" /> -->
</template>

<script>
import VueDocPreview from "vue-doc-preview";
export default {
  props:['id'],
  data: function() {
    return {
      mdStyle: {
        pre: {
          // 'background-color': 'rgb(255, 255, 12)'
        },
        code: {
          "background-color": "#4C5454",
          "font-weight": "bold",
          "font-size": "20px",
          "z-index": "30px",
          "border-radous": "2%",
          "text-align": "left",
          color: "orange",
          "line-height": "40px",
        },
      },
    };
  },
  methods:{
    getURL(){
      return 'documents/'+this.id
    }
  },
  components: {
    VueDocPreview,
  },
};
</script>
