import axios from 'axios';

export const searchVideos = async (game) => {
  try {
    const response = await axios.get('http://localhost:8000/search', {
      params: { game },  // Pass the game name to the backend API
    });

    console.log(response.data); // Log the entire response to check if the structure is correct

    // Ensure the data has the `data` property and it's an array
    if (response.data && Array.isArray(response.data)) {
      return response.data.map((video) => ({
        id: video.id,
        title: video.title,
        duration: video.duration,
        view_count: video.view_count,
        url: video.url,
        thumbnail_url: video.thumbnail_url.replace('%{width}', '320').replace('%{height}', '180'), // Replace width and height
      }));
    } else {
      return 0;
    }
  } catch (error) {
    console.error('Error fetching videos:', error);
    return 0;
  }
};
