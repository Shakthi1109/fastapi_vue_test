# visibrain_test

Frontend:

npm create vite@latest frontend-vue -- --template vue
cd frontend-vue
npm install
npm run dev

Open http://localhost:5173



Backend:

Create virtual env and activate it :
$ python -m venv venv
$ venv\Scripts\activate (Windows)


Create main.py and run the server with:
$ uvicorn main:app --reload

        



![Screenshot (30)](https://github.com/user-attachments/assets/4934d9cd-c727-4d3d-9592-647e8d10d99f)


# 🎮 Twitch Video Search Web App

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
   git clone https://github.com/<your-username>/visibrain_test.git
   cd visibrain_test/backend-fastapi
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
MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/test?retryWrites=true&w=majority
TWITCH_CLIENT_ID=your_twitch_client_id
TWITCH_CLIENT_SECRET=your_twitch_client_secret
```


**5. Run the FastAPI server:**
```
uvicorn main:app --reload
```

The backend API will be available at:

📍 http://localhost:8000
   Serving at: http://127.0.0.1:8000                                                              
   API docs: http://127.0.0.1:8000/docs 




*🌐 Frontend Setup (Vue.js)*
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
📍 http://localhost:5173


**Have fun coding with Shakthivel Murugavel**