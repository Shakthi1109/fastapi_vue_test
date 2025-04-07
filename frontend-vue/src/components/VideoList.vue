<template>
  
    <div v-if="hasSearched && videos.length === 0" class="video-info">
      No videos found for this game.
    </div>

    <div class="video-info">{{ videos.length }} videos found</div>
    
    <div class="video-list">
    <div v-for="video in videos" :key="video.id" class="video-item">
      <img :src="video.thumbnail_url" :alt="video.title" class="thumbnail" />
      <div class="video-details">
        <h3>{{ video.title }}</h3>
        <p>Views: {{ video.view_count }}</p>
        <p>{{ video.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    videos: Array, // Receive list of videos from parent component
    hasSearched: Boolean, // Track if a search has been made
  },
};
</script>

<style scoped>
.video-list {
  justify-content: center;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.video-item {
  width: 250px;
  background-color: #3c3c3c;
  border-radius: 8px;
  padding: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.thumbnail {
  width: 100%;
  border-radius: 8px;
}
.video-details {
  padding: 10px 0;
}

.video-info {
  padding: 20px;
  text-align: center;
  margin-bottom: 20px;
  font-size: 18px;
}

</style>
