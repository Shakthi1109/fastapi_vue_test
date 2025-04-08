<template>
  <div class="app">
    <h1>Twitch Video Search</h1>

    <!-- Search bar -->
    <SearchBar @search="onSearch" />

    <!-- Loading message -->
    <div v-if="isLoading" class="info"> Loading videos... </div>

    <!-- No videos message (only after a search was made and not loading) -->
    <div v-if="hasSearched && !isLoading && videos.length === 0" class="info"> No videos found for this game. </div>

    <VideoList v-if="videos.length > 0" :videos="videos" :hasSearched="hasSearched" />
    
  </div>
</template>

<script>
import { searchVideos } from './services/TwitchApi';
import SearchBar from './components/SearchBar.vue';
import VideoList from './components/VideoList.vue';

export default {
  components: {
    SearchBar,
    VideoList,
  },
  data() {
    return {
      game: '',          // Game name from search
      videos: [],        // Fetched videos
      isLoading: false,  // Show loading spinner
      hasSearched: false // Track if search has occurred
    };
  },
  methods: {
    async onSearch(game) {
      this.game = game;
      await this.fetchVideos(); // Trigger fetch when user searches
    },

    async fetchVideos() {
      if (this.game) {
        this.isLoading = true;
        this.hasSearched = true;

        try {
          const videoResults = await searchVideos(this.game);
          this.videos = Array.isArray(videoResults) ? videoResults : [];
        } catch (error) {
          console.error("Error fetching videos:", error);
          this.videos = []; // fallback if API fails
        } finally {
          this.isLoading = false;
        }
      }
    },
  },
  
  mounted() {
    // Refresh videos every 2 minutes
    setInterval(() => {
      if (this.game) {
        this.fetchVideos();
      }
    }, 120000);
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
  margin-top: 20px;
}

.info {
  padding-top: 20px;
  font-size: 16px;
}
</style>
