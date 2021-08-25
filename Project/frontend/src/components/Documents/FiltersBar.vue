<template>
  <v-container fluid>
    <v-row align="center">
      <v-col cols="3">
        <v-subheader>
          Select Filters:
        </v-subheader>
      </v-col>

      <v-col cols="2">
        <v-select
        @change="sortByRanking($event)"
          :items="itemsRanking"
          item-text="state"
          item-value="abbr"
          label="Ranking"
          persistent-hint
          return-object
          single-line
        ></v-select>
      </v-col>
      <v-col cols="2">
        <v-select
         @change="sortByUploadDate($event)"
          :items="itemsNew"
          item-text="state"
          item-value="abbr"
          label="Upload Date"
          persistent-hint
          return-object
          single-line
        ></v-select>
      </v-col>
      <v-col cols="2">
        <v-select
        @change="sortByviews($event)"
          :items="itemsViews"
          item-text="state"
          item-value="abbr"
          label="Views Amount"
          persistent-hint
          return-object
          single-line
        ></v-select>
      </v-col>
      <v-col cols="2">
        <v-select
          @change="ApplyFilters($event)"
          :items="filters"
          item-text="state"
          item-value="abbr"
          label="Show Only"
          persistent-hint
          return-object
          single-line
        ></v-select>
      </v-col>
      
        <v-col>
        
        <v-icon   @click="clearFilters()" color="blue">clear</v-icon>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-toolbar flat color="transparent">
          <v-btn icon>
            <v-icon>mdi-arrow-left</v-icon>
          </v-btn>

          <v-text-field
            width="20px"
            append-icon="mdi-magnify"
            label="Search Documents In This course"
            single-line
            ><v-icon>magnify</v-icon></v-text-field
          >
        </v-toolbar>
      </v-col>
    
    </v-row>
  </v-container>
</template>
<script>

export default {
  props: ["enuMSrt"],
  data() {
    return {
      itemsRanking: [
        { state: "Ranking High to Low" },
        { state: "Ranking Low to High" },
      ],
      filters: [
        { state: "10 Highest ranked" },
        { state: "10  Most viewed" },
        { state: "10  Lastest uploaded" },
      ],
      itemsViews: [
        { state: "Views High to Low" },
        { state: "Views Low to High" },
      ],
      itemsNew: [
        
        { state: "Uploaded Newest to Oldest" },
        { state: "Ranking Oldest to Newest" },
      ],
    };
  },
  methods: {
    clearFilters(){
      this.$emit('clear')
    },
     sortByRanking(value){ 

       var selected = value.state;
       console.log("X")
       if (selected === "Ranking High to Low") {
          this.$emit("sortRankings",this.enuMSrt.DOWN);
       }
        if (selected === "Ranking Low to High") {
           this.$emit("sortRankings",this.enuMSrt.UP);
       }

    },
    sortByviews(value){
      var selected = value.state;
       if (selected === "Views High to Low") {
          this.$emit("sortViews",this.enuMSrt.DOWN);
       }
        if (selected === "Views Low to High") {
           this.$emit("sortViews",this.enuMSrt.UP);
       }

    },
      sortByUploadDate(value){
        var selected = value.state;
       if (selected === "Uploaded Newest to Oldest") {
          this.$emit("sortByDate",this.enuMSrt.DOWN);
       }
        if (selected === "Ranking Oldest to Newest") {
           this.$emit("sortByDate",this.enuMSrt.UP);
       }

    },
    
    ApplyFilters(value) {
      var selected = value.state;
      console.log(selected);
      if (selected === "10  Most viewed") {
        //fire filter event for top ranked
        
        this.$emit("showOnlyMostViews");
      }
      if (selected === "10 Highest ranked") {
        //fire filter event for top ranked
        console.log("going to fire event!!!!");
        this.$emit("showOnlyHighesrRanked");
      }
        if (selected === "10  Lastest uploaded") {
        //fire filter event for top ranked
        console.log("going to fire event!!!!");
        this.$emit("showOnlyTenLastUploaded");
      }
    },
  },
};
</script>
