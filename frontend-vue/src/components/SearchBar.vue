<template>
  <div class="search-container">
    <div class="search-box">
      <input
        v-model="gameName"
        placeholder="Search for a game..."
        @keyup.enter="onSearch"
        @focus="fetchTrending"
        @blur="hideDropdown"
        @input="handleInput"
        type="text"
        class="search-input"
      />
      <button @click="onSearch" class="search-button">Search</button>
    </div>

    <ul v-if="showDropdown && trending.length" class="dropdown">
      <li
        v-for="(item, index) in trending"
        :key="index"
        @mousedown.prevent="selectTrending(item.game_name)"
        class="dropdown-item"
      >
        <span>
          {{ item.emoji }} <strong>{{ item.game_name }}</strong>
        </span>
        <span class="frequency">
          trending {{ item.rank }} {{ item.flames }}
        </span>
      </li>
    </ul>
  </div>
</template>



<script>
export default {
  data() {
    return {
      gameName: '',
      trending: [],
      showDropdown: false,
      emojiMap: {
        fifa: '⚽',
        gta: '🚗',
        mario: '🍄',
        valorant: '🎯',
        nfs: '🏎️',
        minecraft: '⛏️',
      },
    };
  },
  methods: {
    onSearch() {
      if (this.gameName.trim()) {
        this.$emit('search', this.gameName);
        this.showDropdown = false;
      }
    },
    async fetchTrending() {
      try {
        const response = await fetch('http://localhost:8000/trending-searches');
        let data = await response.json();

        // Most searched = rank 1 at top
        data.sort((a, b) => b.frequency - a.frequency);

        this.trending = data.map((item, index) => {
          const emoji = this.emojiMap[item.game_name.toLowerCase()] || '🎮';
          const rank = index + 1;
          const flames = rank === 1 ? '🔥' : '';

          return {
            ...item,
            emoji,
            rank,
            flames,
          };
        });

        this.showDropdown = true;
      } catch (err) {
        console.error('Error fetching trending searches:', err);
      }
    },
    selectTrending(game) {
      this.gameName = game;
      this.onSearch();
    },
    handleInput() {
      this.showDropdown = false;
    },
    hideDropdown() {
      setTimeout(() => (this.showDropdown = false), 200);
    },
  },
};
</script>



<style scoped>

.search-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 40px;
}

.search-box {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
}

.search-input {
  min-height: 40px;
  font-size: 16px;
  font-weight: bold;
  width: 300px;
  padding-left: 10px;
  margin-right: 20px;
  background-color: #000;
  color: #fff;
  box-shadow: -2px 0 #fff, 0 1px #fff, 1px 0 #fff, 0 -1px #fff;
  font-weight: bold;
  
}

.search-button {
  font-size: 16px;
  background-color: #4caf50;
  color: white;
  padding: 10px 15px;
  font-weight: 900;
  box-shadow: -2px 0 black, 0 2px black, 2px 0 black, 0 -2px black;
}

.search-button:hover {
  background-color: #45a049;
}

.dropdown {
  background: #f3d6f6;
  border: 1px solid #ccc;
  width: 450px;
  z-index: 100;
  margin-top: 5px;
  padding: 0;
  list-style: none;
  border-radius: 6px;
  box-shadow: -2px 0 black, 0 2px black, 2px 0 black, 0 -2px black;
  color: #000;
}

.dropdown-item {
  padding: 10px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  font-size: 15px;
  align-items: center;
}

.dropdown-item:hover {
  background-color: #f5f5f5;
}

.frequency {
  color: #000000;
  font-size: 14px;
  white-space: nowrap;
}
</style>

