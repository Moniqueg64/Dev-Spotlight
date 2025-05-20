
# DevSpotlight – Developer Blog Platform

**DevSpotlight** is a minimalist blogging platform built with Flask, designed for developers who want to share technical posts, tutorials, and insights. It supports user login, post creation, and a clean reading experience.

---

## Features

- User registration and login (Flask-Login)
- Write and publish blog posts with Markdown support
- View all posts on the homepage
- Secure password hashing and session handling
- Clean UI with Bootstrap

---

## Tech Stack

- **Backend:** Flask, SQLAlchemy
- **Auth:** Flask-Login, Werkzeug security
- **Frontend:** Jinja2 templates, HTML/CSS, Bootstrap
- **Database:** SQLite (can be switched to PostgreSQL)

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/devspotlight.git
cd devspotlight
```

### 2. Set Up the Environment

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file (optional) or use default values in `config.py`.

```env
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///devspotlight.db
```

### 4. Initialize the Database

```bash
from app import create_app, db
app = create_app()
with app.app_context():
    db.create_all()
```

### 5. Run the App

```bash
python run.py
```

App runs at `http://localhost:5000`

---

## Folder Structure

```
devspotlight/
├── app/
│   ├── routes/
│   ├── models/
│   ├── templates/
│   ├── static/
│   └── __init__.py
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

---

## Future Ideas

- Comments system
- Post tags and filtering
- Markdown rendering and syntax highlighting
- Admin dashboard and post drafts

---

## License

MIT License

---

## Author

Created by **Monique64**  
GitHub: [@Monique64](https://github.com/Monique64)
