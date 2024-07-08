<template>
  <div id="app">
    <FeedbackForm />
  </div>
</template>

<script>
import FeedbackForm from './components/FeedbackForm.vue';

export default {
  name: 'App',
  components: {
    FeedbackForm
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
