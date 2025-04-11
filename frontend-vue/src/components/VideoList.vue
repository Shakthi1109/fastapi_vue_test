<template>

    <div class="video-info">{{ videos.length }} videos found</div>
    
    <div class="video-list">
    <div v-for="video in videos" :key="video.id" class="video-item">
      <a :href="video.url" target="_blank" class="video-link">
      <img :src="video.thumbnail_url" :alt="video.title" class="thumbnail" />
      <div class="video-details">
        <h3>{{ video.title }}</h3>
        <p>Views: {{ video.view_count }}</p>
        <p>Duration: {{ video.duration }}</p>
      </div>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    videos: Array, // Receive list of videos passed directly from parent component
    hasSearched: Boolean, // Track if a search has been made
  }
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
  background-color: #f7b9ff;
  border-radius: 8px;
  padding: 10px;
  box-shadow: -5px 0 black, 0 5px black, 5px 0 black, 0 -5px black;
}
.thumbnail {
  width: 100%;
  border-radius: 8px;
}
.video-details {
  padding: 10px 0;
  color: #000000;
}

.video-info {
  padding-top: 30px;
  padding-bottom: 10px;
  text-align: center;
  margin-bottom: 20px;
  font-size: 17px;
  font-weight: bold;
  text-shadow: -2px 0 black, 0 2px black, 2px 0 black, 0 -2px black;
}

</style>
