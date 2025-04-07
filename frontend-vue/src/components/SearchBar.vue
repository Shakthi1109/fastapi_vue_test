<template>
  <div>
    <!-- Input field -->
    <input
      v-model="gameName"
      type="text"
      placeholder="Search for a game..."
      @keyup.enter="onSearch"     
      class="search-input"
    /> <!-- Triggers search on Enter key -->

    <!-- Search button -->
    <button @click="onSearch" class="search-button">
      Search
    </button>
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
  padding: 10px;
  font-size: 16px;
  width: 100%;
  max-width: 400px;
  margin: 10px 0;
  box-sizing: border-box;
}

.search-button {
  padding: 10px 20px;
  font-size: 16px;
  margin-left: 10px;
  cursor: pointer;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
}

.search-button:hover {
  background-color: #45a049;
}
</style>
