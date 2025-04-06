<template>
    <div class="video-list">
      <div v-for="video in videos" :key="video.id" class="video-card">
        <img :src="video.thumbnail_url" :alt="video.title" />
        <h3>{{ video.title }}</h3>
        <p>{{ video.description }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      videos: Array  // List of videos passed as a prop
    }
  };
  </script>
  
  <style scoped>
  .video-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
  }
  
  .video-card {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    text-align: center;
  }
  
  .video-card img {
    width: 100%;
    border-radius: 5px;
  }
  
  .video-card h3 {
    font-size: 1.2rem;
    margin-top: 10px;
  }
  
  .video-card p {
    font-size: 0.9rem;
    color: #555;
  }
  </style>
  