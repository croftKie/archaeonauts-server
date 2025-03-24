# Archaeonauts Server

Welcome to the **Archaeonauts Server** — the backend system for the Archaeonauts game, handling user authentication, progress tracking, and the global leaderboard.

## 🌐 About the Server

The Archaeonauts Server powers the multiplayer and progression aspects of the game. It manages player accounts, tracks game state, and updates the public leaderboard.

The server handles:

- **User Authentication** – Secure login with password hashing
- **Game State Management** – Saves player progress and statistics
- **Leaderboard** – Global ranking for reputation, knowledge, and ruins explored

## 🛠️ Tech Stack

- **Python** – Core programming language
- **FastAPI** – For building the RESTful API
- **MongoDB** – For storing user data and game state
- **bcrypt** – For password hashing and secure authentication

## 📥 Installation

### Prerequisites

- Python 3.10+
- MongoDB instance running locally or in the cloud

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a `.env` file with the following:

```env
MONGO_URI=mongodb://localhost:27017/archaeonauts
SECRET_KEY=your-secret-key
```

### Run the Server

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## 🚀 API Endpoints

### User Authentication

- `POST /register` – Register a new user
- `POST /login` – Log in and receive a JWT token
- `GET /profile` – Retrieve player profile

### Game State

- `POST /progress` – Update game progress
- `GET /progress` – Get current game state

### Leaderboard

- `GET /leaderboard` – Get top players ranked by reputation and knowledge

## 🌍 Contributing

We welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

### Code Guidelines

- Follow PEP 8 for Python styling.
- Keep commits clean and well-documented.
- Write unit tests for any new functionality.

## 🤝 License

This project is open-source under the MIT License.

## 📧 Contact

For questions or feedback, please open an issue or contact the development team.

---

Thank you for helping build the Archaeonauts universe!
