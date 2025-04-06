<template>
    <div class="video-search-container">
      <h1>Twitch Video Search</h1>
      <SearchBar @search="onSearch" />
      <VideoList :videos="videos" />
    </div>
  </template>
  
  <script>
  import SearchBar from './SearchBar.vue';
  import VideoList from './VideoList.vue';
  import { searchVideos } from '../services/twitchApi.js';  // Import the function to search Twitch API
  
  export default {
    components: {
      SearchBar,
      VideoList
    },
    data() {
      return {
        videos: [],  // Store the list of videos
        searchQuery: ""  // Store the search query
      };
    },
    methods: {
      async onSearch(query) {
        this.searchQuery = query;
        await this.fetchVideos(query);
      },
      async fetchVideos(query) {
        this.videos = await searchVideos(query);  // Fetch videos from API
      }
    },
    mounted() {
      setInterval(() => {
        if (this.searchQuery) {
          this.fetchVideos(this.searchQuery);  // Refresh the videos every 2 minutes
        }
      }, 120000);  // 120000 ms = 2 minutes
    }
  };
  </script>
  
  <style scoped>
  .video-search-container {
    padding: 20px;
    text-align: center;
  }
  
  h1 {
    color: #4CAF50;
  }
  
  .video-list {
    margin-top: 20px;
  }
  </style>
  