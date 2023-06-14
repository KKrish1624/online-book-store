<template>
  <div class="about">
    <h3 v-text="render"></h3>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      render: "",
    };
  },
  methods: {
    getResponse() {
      const path = "http://127.0.0.1:5000/second";
      axios.get(path).then((res) => {
        console.log(res.data);
        this.render = res.data;
      });
    },
  },
  created() {
    this.getResponse();
  },
};
</script>
