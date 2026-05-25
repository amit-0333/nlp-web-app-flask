# 🧠 NLP Web App

A Flask-based web application that performs **Natural Language Processing** tasks — Named Entity Recognition, Sentiment Analysis, and Emotion Detection — with user login and history tracking.

---

## 📁 Project Structure

```
FLASK WEB/
├── templates/        # HTML templates
├── api.py            # NLP logic (spaCy, VADER)
├── app.py            # Flask routes
├── db.py             # User data read/write (JSON file I/O)
├── usersdata.json    # Stores users and their history
└── README.md
```

---

## ✨ Features

- 🔐 User Register / Login (JSON file based, no database)
- 🏷️ **Named Entity Recognition (NER)** — detects persons, places, organizations, dates etc.
- 😊 **Sentiment Analysis** — positive, negative or neutral using VADER
- 😤 **Emotion Detection** — detects emotions like happy, sad, angry, fear, surprise
- 📜 History — tracks all past queries per user

---

## ⚙️ Installation

**Requirements:** Python 3.7+

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/nlp-web-app.git
   cd nlp-web-app
   ```

2. **Install dependencies**
   ```bash
   pip install flask spacy vaderSentiment
   ```

3. **Download spaCy English model**
   ```bash
   python -m spacy download en_core_web_sm
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

---

## 🔐 Authentication

- User data is stored in `usersdata.json` using Python file I/O — no database required
- Passwords are hashed using `hashlib` (SHA-256)
- Sessions managed with Flask's built-in `session`

**How `usersdata.json` looks:**
```json
{
    "username@gmail.com": [
        "username",
        "password"
]}
```

---

## 🧪 NLP Tasks

### Named Entity Recognition (NER)
Uses **spaCy** (`en_core_web_sm`) to detect entities in text.

| Entity | Meaning               |
|--------|-----------------------|
| PERSON | People, characters    |
| ORG    | Companies, agencies   |
| GPE    | Countries, cities     |
| DATE   | Dates and times       |
| MONEY  | Monetary values       |

**Example input:**
```
Elon Musk founded SpaceX in Hawthorne, California in 2002.
```
**Output:**
```
Elon Musk     → PERSON
SpaceX        → ORG
Hawthorne     → GPE
California    → GPE
2002          → DATE
```

---

### Sentiment Analysis
Uses **VADER** (Valence Aware Dictionary and sEntiment Reasoner) — best suited for social media and short texts.

**Example input:**
```
The movie was absolutely amazing, loved every bit of it!
```
**Output:**
```
Sentiment  : Positive
Score      : 0.87
```

---

### Emotion Detection
Detects emotions like **Happy, Sad, Angry, Fear, Surprise, Disgust** from text using keyword/lexicon-based approach.

**Example input:**
```
I am so frustrated and tired of this situation.
```
**Output:**
```
Emotion : Angry
```

---

## 🛠️ Tech Stack

| Layer        | Technology                     |
|--------------|--------------------------------|
| Backend      | Python, Flask                  |
| NLP          | spaCy, VADER (vaderSentiment)  |
| Auth/Storage | JSON file + Python file I/O    |
| Frontend     | HTML, CSS (Jinja2 templates)   |

---

## 📝 Notes

- No external database used — everything stored in `usersdata.json`
- `db.py` handles all read/write operations for user data
- `api.py` contains all NLP processing functions
- `app.py` wires Flask routes to `api.py` and `db.py`

---

## 📄 License

MIT License — free to use and modify.
