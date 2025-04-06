<template>
    <div class="search-bar-container">
      <input v-model="query" @keyup.enter="handleSearch" placeholder="Search for a game" />
      <button @click="handleSearch">Search</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        query: ""  // Store the search query
      };
    },
    methods: {
      handleSearch() {
        this.$emit("search", this.query);  // Emit the search query to the parent
      }
    }
  };
  </script>
  
  <style scoped>
  .search-bar-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
  }
  
  input {
    padding: 8px;
    font-size: 1rem;
  }
  
  button {
    padding: 8px 16px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #45a049;
  }
  </style>
  