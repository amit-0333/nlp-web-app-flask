<div align="center">

```
███╗   ██╗██╗     ██████╗     ██╗    ██╗███████╗██████╗ 
████╗  ██║██║     ██╔══██╗    ██║    ██║██╔════╝██╔══██╗
██╔██╗ ██║██║     ██████╔╝    ██║ █╗ ██║█████╗  ██████╔╝
██║╚██╗██║██║     ██╔═══╝     ██║███╗██║██╔══╝  ██╔══██╗
██║ ╚████║███████╗██║         ╚███╔███╔╝███████╗██████╔╝
╚═╝  ╚═══╝╚══════╝╚═╝          ╚══╝╚══╝ ╚══════╝╚═════╝ 

 █████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔══██╗
███████║██████╔╝██████╔╝
██╔══██║██╔═══╝ ██╔═══╝ 
██║  ██║██║     ██║     
╚═╝  ╚═╝╚═╝     ╚═╝     
```

### 🧠 NLP Web App

> A Flask-based web application that performs **Natural Language Processing** tasks — Named Entity Recognition, Sentiment Analysis & Emotion Detection — with user login and history tracking.

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20App-000000?style=for-the-badge&logo=flask)
![spaCy](https://img.shields.io/badge/NLP-spaCy-09A3D5?style=for-the-badge)
![VADER](https://img.shields.io/badge/Sentiment-VADER-blueviolet?style=for-the-badge)
![JSON](https://img.shields.io/badge/Storage-JSON-lightgrey?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

</div>

---

## 📌 About

This is a **full-stack NLP web application** built with Flask — a step up from the desktop GUI version, now featuring user authentication, multi-task NLP, and per-user history tracking.

Built to master:
- Building full-stack Flask web apps with authentication
- Implementing NER, Sentiment Analysis & Emotion Detection
- Session management and password hashing with `hashlib`
- Storing structured user data with JSON file I/O
- Modularizing a Flask project into separate files (`app.py`, `api.py`, `db.py`)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔐 Register / Login | User auth via JSON file — no database required |
| 🏷️ Named Entity Recognition | Detects persons, places, orgs, dates & more using spaCy |
| 😊 Sentiment Analysis | Positive / Negative / Neutral detection using VADER |
| 😤 Emotion Detection | Detects Happy, Sad, Angry, Fear, Surprise, Disgust |
| 📜 History Tracking | Every past query saved and tracked per user |
| 🔒 Session Management | Flask sessions + SHA-256 password hashing |

---

## 🗂️ Project Structure

```bash
NLP-Web-App/
│
├── 📄 app.py               # Flask routes — wires everything together
├── 📄 api.py               # NLP logic — spaCy NER + VADER + Emotion Detection
├── 📄 db.py                # User data — JSON read & write handler
├── 📄 usersdata.json       # Stores all users and their query history
│
├── 📂 templates/           # Jinja2 HTML templates
│
└── 📄 README.md
```

### 🧠 How It Works

```
User Input
     │
     ▼
app.py (Flask Route)
     │
     ├──→ api.py  (NER / Sentiment / Emotion logic)
     │
     └──→ db.py   (Read & Write usersdata.json)
     │
     ▼
Render Result + Save to History
```

| File | Role |
|------|------|
| `app.py` | Flask routes, session handling, page rendering |
| `api.py` | All NLP functions — spaCy, VADER, emotion keywords |
| `db.py` | Reads & writes user data and history to `usersdata.json` |
| `usersdata.json` | Stores registered users + their full query history |

---

## ⚙️ How to Run

```bash
# 1. Clone the repository
git clone https://github.com/amit-0333/nlp-web-app.git

# 2. Navigate into the folder
cd nlp-web-app

# 3. Install dependencies
pip install flask spacy vaderSentiment

# 4. Download spaCy English model
python -m spacy download en_core_web_sm

# 5. Run the app
python app.py

# 6. Open in browser
# → http://127.0.0.1:5000
```

---

## 🔐 Authentication

User data is stored in `usersdata.json` — no database required.
Passwords hashed with `hashlib` SHA-256. Sessions managed via Flask's built-in `session`.

```json
{
    "username@gmail.com": [
        "username",
        "hashed_password"
    ]
}
```

---

## 🧪 NLP Tasks

### 🏷️ Named Entity Recognition

Uses **spaCy** (`en_core_web_sm`) to detect entities in text.

| Entity | Meaning |
|--------|---------|
| PERSON | People, characters |
| ORG | Companies, agencies |
| GPE | Countries, cities |
| DATE | Dates and times |
| MONEY | Monetary values |

**Input:**
```
Elon Musk founded SpaceX in Hawthorne, California in 2002.
```
**Output:**
```
Elon Musk   → PERSON
SpaceX      → ORG
Hawthorne   → GPE
California  → GPE
2002        → DATE
```

---

### 😊 Sentiment Analysis

Uses **VADER** — best suited for social media and short texts.

**Input:**
```
The movie was absolutely amazing, loved every bit of it!
```
**Output:**
```
Sentiment : Positive
Score     : 0.87
```

---

### 😤 Emotion Detection

Detects emotions using a keyword/lexicon-based approach.

**Input:**
```
I am so frustrated and tired of this situation.
```
**Output:**
```
Emotion : Angry
```

**Detectable emotions:** Happy · Sad · Angry · Fear · Surprise · Disgust

---

## 🧩 My Approach

```
1. 📖 Plan the architecture — app.py / api.py / db.py separation
2. 🔨 Build NLP logic first in api.py
3. 🔒 Add auth — register, login, session, password hashing
4. 💾 Build JSON read/write handler in db.py
5. 🖥️ Wire everything together in app.py with Flask routes
6. ✅ Test all three NLP tasks with different inputs
```

---

## 🎯 Learning Goals

- [x] Build a full-stack Flask web application
- [x] Implement user registration & login with sessions
- [x] Hash passwords with SHA-256
- [x] Store user data with JSON file I/O
- [x] Implement Named Entity Recognition with spaCy
- [x] Implement Sentiment Analysis with VADER
- [x] Implement Emotion Detection
- [x] Track per-user query history
- [x] Modularize Flask project into separate files
- [ ] Deploy to a cloud platform
- [ ] Add a proper database (SQLite / PostgreSQL)
- [ ] Improve emotion detection with an ML model

---

## 🔮 Future Improvements

- [ ] Replace JSON storage with a real database (SQLite / PostgreSQL)
- [ ] Improve emotion detection with a trained ML model
- [ ] Add text summarization feature
- [ ] Visualize NER results with highlighted spans
- [ ] Add multi-language support
- [ ] Deploy to Heroku / Render

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| 🐍 Backend | Python, Flask |
| 🏷️ NLP | spaCy, VADER (vaderSentiment) |
| 🔒 Auth / Storage | JSON file + hashlib SHA-256 |
| 🎨 Frontend | HTML, CSS (Jinja2 templates) |

---

## 👨‍💻 Author

**Amit Kumar**

[![GitHub](https://img.shields.io/badge/GitHub-amit--0333-181717?style=flat&logo=github)](https://github.com/amit-0333)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Amit%20Kumar-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/amit-kumar-a62a3640a/)
[![Kaggle](https://img.shields.io/badge/Kaggle-amitkumar038975-20BEFF?style=flat&logo=kaggle)](https://www.kaggle.com/amitkumar038975)

---

<div align="center">

> 📝 *A step up from the desktop GUI — now a full web app with auth, history & three NLP tasks.*

⭐ **Star this repo if you found it useful!**

</div>
