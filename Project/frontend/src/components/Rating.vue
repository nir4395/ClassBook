<template>
  <div>
    
    <v-row>
   
      
      <v-col>
        <div>
          <h2 style="float:left"> {{name}}</h2>
          <v-icon style="float:left;margin-right" color="yellow">star</v-icon>
          <h3 style="font-size:12px"> {{rating}} / 5</h3>
        </div></v-col
      >
      <v-col  > <div style="float:left">
      <fieldset class="rating">
        <input
          @click="getRank($event)"
          type="radio"
          id="star5"
          name="rating"
          value="5"
        /><label class="full" for="star5" title="Awesome - 5 stars"></label>
        <input
          @click="getRank($event)"
          type="radio"
          id="star4half"
          name="rating"
          value="4.5"
        /><label
          class="half"
          for="star4half"
          title="Pretty good - 4.5 stars"
        ></label>
        <input
          @click="getRank($event)"
          type="radio"
          id="star4"
          name="rating"
          value="4"
        /><label class="full" for="star4" title="Pretty good - 4 stars"></label>
        <input
          @click="getRank($event)"
          type="radio"
          id="star3half"
          name="rating"
          value="3.5"
        /><label class="half" for="star3half" title="Meh - 3.5 stars"></label>
        <input
          @click="getRank($event)"
          type="radio"
          id="star3"
          name="rating"
          value="3"
        /><label class="full" for="star3" title="Meh - 3 stars"></label>
        <input
          @click="getRank($event)"
          type="radio"
          id="star2half"
          name="rating"
          value="2.5"
        /><label
          class="half"
          for="star2half"
          title="Kinda bad - 2.5 stars"
        ></label>
        <input
          @click="getRank($event)"
          type="radio"
          id="star2"
          name="rating"
          value="2"
        /><label class="full" for="star2" title="Kinda bad - 2 stars"></label>
        <input
          @click="getRank($event)"
          type="radio"
          id="star1half"
          name="rating"
          value="1.5"
        /><label class="half" for="star1half" title="Meh - 1.5 stars"></label>
        <input
          @click="getRank($event)"
          type="radio"
          id="star1"
          name="rating"
          value="1"
        /><label
          class="full"
          for="star1"
          title="Sucks big time - 1 star"
        ></label>
        <input
          @click="getRank($event)"
          type="radio"
          id="starhalf"
          name="rating"
          value="0.5"
        /><label
          class="half"
          for="starhalf"
          title="Sucks big time - 0.5 stars"
        ></label>
      </fieldset>
      {{ currentRating }} Stars
  
    </div></v-col>
    <v-col  cols="1"
        sm="1"
        md="1"><v-btn color="blue" @click="RankDocuemnt()">Rank </v-btn></v-col>
    </v-row>

   
  </div>
</template>
<script>
export default {
  data() {
    return {
      currentRating: 0,
    };
  },
  props: ["name", "rating", "id"],
  methods: {
    getRank(e) {
      this.currentRating = document.getElementById(e.target.id).value;
    },
    async RankDocuemnt() {
      try {
        var url = "http://localhost:8000/course/rate/";
        var data = { document_id: this.id, user_rating: this.currentRating };
        const response = await this.$http.post(url, data);
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>
<style scoped>
@import url(//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css);

fieldset,
label {
  margin: 0;
  padding: 0;
}
body {
  margin: 20px;
}
h1 {
  font-size: 1.5em;
  margin: 10px;
}

/****** Style Star Rating Widget *****/

.rating {
  border: none;
  float: left;
}

.rating > input {
  display: none;
}
.rating > label:before {
  margin: 5px;
  font-size: 1.25em;
  font-family: FontAwesome;
  display: inline-block;
  content: "\f005";
}

.rating > .half:before {
  content: "\f089";
  position: absolute;
}

.rating > label {
  color: #ddd;
  float: right;
}

/***** CSS Magic to Highlight Stars on Hover *****/

.rating > input:checked ~ label, /* show gold star when clicked */
.rating:not(:checked) > label:hover, /* hover current star */
.rating:not(:checked) > label:hover ~ label {
  color: #ffd700;
} /* hover previous stars in list */

.rating > input:checked + label:hover, /* hover current star when changing rating */
.rating > input:checked ~ label:hover,
.rating > label:hover ~ input:checked ~ label, /* lighten current selection */
.rating > input:checked ~ label:hover ~ label {
  color: #ffed85;
}
</style>
