<template>
  <div class="video-search">
    <SearchBar @search="searchVideos" />  <!-- Pass the search method to the SearchBar component -->
    <VideoList :videos="videos" />       <!-- Pass the video list to the VideoList component -->
  </div>
</template>

<script>
import { searchVideos } from '../services/TwitchApi.js';  // Import the search function
import SearchBar from './SearchBar.vue';
import VideoList from './VideoList.vue';

export default {
  components: {
    SearchBar,
    VideoList,
  },
  data() {
    return {
      videos: [],
    };
  },
  methods: {
    async searchVideos(gameName) {
      this.videos = await searchVideos(gameName);  // Call the API and update videos
    },
  },
};
</script>

<style scoped>
.video-search {
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
}
</style>
