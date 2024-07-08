<template>
  <div>
    <h2>How would you rate your satisfaction with our product?</h2>
    <div>
      <span v-for="star in 5" :key="star" @click="rate(star)">
        <i :class="star <= score ? 'fas' : 'far'">★</i>
      </span>
    </div>
    <button @click="submitFeedback">Submit</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      score: 0,
    };
  },
  methods: {
    rate(star) {
      this.score = star;
    },
    async submitFeedback() {
      try {
        await axios.post('http://localhost:8000/feedback/', { score: this.score });
        alert('Feedback submitted successfully!');
      } catch (error) {
        console.error(error);
        alert('Failed to submit feedback.');
      }
    },
  },
};
</script>

<style>
.fas, .far {
  cursor: pointer;
  font-size: 24px;
}
</style>
