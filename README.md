# 🎮 Twitch Video Search Web App

![Screenshot (32)](https://github.com/user-attachments/assets/64e197d1-01bb-4020-81ac-f53d67c4ec38)


This full-stack web app lets users search for Twitch game videos and view trending search terms using:

- ⚙️ **FastAPI** (Python backend)
- 🌐 **Vue.js** (Frontend)
- ☁️ **MongoDB Atlas** (Cloud database)

---

## ✨ Features

- 🔍 Search for Twitch videos by game name
- 📈 Trending search terms (stored and ranked using MongoDB)
- 🔥 Cool UI showing top searched games
- ☁️ No local DB setup needed — uses MongoDB Atlas

## 🚀 Quick Start

### 📦 Prerequisites

- **Python 3.9+**
- **Node.js 16+** and **npm** or **yarn**
- A free **MongoDB Atlas** account (to get your connection URI)
- A free **Twitch Developer account** (to get your `client_id` and `client_secret`)

---

## 🖥️ Backend Setup (FastAPI)

**1. Clone the repository:**

   ```bash
   git clone https://github.com/Shakthi1109/fastapi_vue_test.git
   cd fastapi_vue_test/backend-fastapi
   ```


**2. Create and activate a virtual environment:**

On Windows:
```
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

**3. Install backend dependencies:**

``` pip install -r requirements.txt ```


**4. Create a .env file:**
Create a file called .env in backend-fastapi/ with the following:
```
TWITCH_CLIENT_ID=your-client-id
TWITCH_CLIENT_SECRET=your-client-secret
MONGO_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority&appName=<Cluster>
```


**5. Run the FastAPI server:**
```
uvicorn main:app --reload
```

The backend API will be available at:

- 📍 http://localhost:8000
- Serving at: http://127.0.0.1:8000
- API docs: http://127.0.0.1:8000/docs 


---

## 🌐 Frontend Setup (Vue.js)
Navigate to frontend directory


```cd ../frontend-vue```


Install dependencies

```
npm install
# or
yarn install
```

Run the frontend dev server

```
npm run dev
# or
yarn dev
```

The frontend will be available at:

- 📍 http://localhost:5173


**❣️Have fun coding with Shakthivel Murugavel❣️**
