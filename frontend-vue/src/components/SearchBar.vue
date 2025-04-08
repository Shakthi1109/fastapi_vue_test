<template>
  <div>
    <input v-model="gameName" placeholder="Search for a game..."  @keyup.enter="onSearch" type="text" class="search-input"/>
    <button @click="onSearch" class="search-button"> Search </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      gameName: '', // Stores user input
    };
  },
  methods: {
    // Emit search event to the parent component
    onSearch() {
      if (this.gameName.trim()) {
        this.$emit('search', this.gameName);
      }
    },
  },
};
</script>

<style scoped>
.search-input {
  min-height: 40px;
  font-size: 16px;
  font-weight: bold;
  max-width: 400px;
  padding-left: 10px;
  margin-right: 20px;
}

.search-button {
  font-size: 16px;
  background-color: #4CAF50;
  color: white;
}

.search-button:hover {
  background-color: #45a049;
}
</style>
