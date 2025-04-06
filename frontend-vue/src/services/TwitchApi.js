import axios from 'axios';

export const searchVideos = async (game) => {
  try {
    const response = await axios.get('http://localhost:8000/api/search-videos', {
      params: { game_id: game },  // Pass the game ID as a query parameter

    });

    // Return the list of videos from the backend
    return response.data.videos;
  } catch (error) {
    console.error("Error fetching videos from backend", error);
    return [];
  }
};
