

# 🐍 Python Dance with Nanah
> **MIVA-CSC312 Final Project Submission**  
> *A Secure, Database-Driven Developer Portal for the Nigerian Tech Ecosystem.*

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511fa.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

---

##  Project Overview
**Python Dance with Nanah** is a comprehensive web implementation designed for the **MIVA-CSC312 (Web Application Development)** assessment. Transitioning from a simple static site to a secure, enterprise-grade portal, this application allows Nigerian student developers to register, secure their accounts, and publish their technical "stories" to a centralized directory.

### The Technical Workflow:
1. **Initialize:** User signs up via a secure interface.
2. **Document:** Redirected to the internal Technical Journey documentation.
3. **Enroll:** User signs in to a private Dashboard to fill in their "Dance Line" (Bio) and skills.
4. **Publish:** Data persists in SQLite and appears instantly on the **Dance Roster** (Directory).

---

##  Key Features

| Feature | Technical Implementation |
|:---|:---|
| **Secure Authentication** | Session-based login/logout management. |
| **Zero-Knowledge Security** | PBKDF2-SHA256 password hashing via `Werkzeug`. |
| **Data Persistence** | Relational mapping using `SQLAlchemy` ORM. |
| **Dynamic Routing** | Flexible endpoint handling for individual portfolios. |
| **Modern UI** | Enterprise Gray/White theme using `Bootstrap 5`. |
| **Modular Design** | `Jinja2` template inheritance for a DRY codebase. |

---

##  Project Architecture

```text
python-dance-with-nanah/
├── App.py                 # Backend Core (Routes, Models, & Auth Logic)
├── miva_nexus.db          # SQLite Persistence Layer
├── requirements.txt       # Environment Dependencies
├── templates/             # UI Layer (Jinja2 Templates)
│   ├── layout.html        # Master Boilerplate (Bootstrap/Nav/Footer)
│   ├── index.html         # High-Conversion Landing Page
│   ├── signup.html        # User Registration (with Password Toggle)
│   ├── signin.html        # Secure Login (with Password Toggle)
│   ├── home.html          # Data Collection Dashboard
│   ├── profile.html       # Unified Student Directory (The Roster)
│   ├── student.html       # Individual Portfolio Rendering
│   ├── services.html      # Technical Documentation & Assignment Readme
│   ├── about.html         # Project Background
│   └── contact.html       # Support Interface
└── static/                # Custom CSS & Branding Assets
```

---

##  Tech Stack
* **Language:** Python 3.x
* **Framework:** Flask (Micro-framework)
* **ORM:** SQLAlchemy
* **Database:** SQLite3
* **Security:** Werkzeug Security (Hashing)
* **Frontend:** Bootstrap 5, Font Awesome 6, Animate.css

---

##  Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Access2Christian/python-dance-with-nanah.git
   cd python-dance-with-nanah
   ```

2. **Install the environment:**
   ```bash
   pip install flask flask-sqlalchemy werkzeug
   ```

3. **Ignite the application:**
   ```bash
   python App.py
   ```

4. **Access the portal:**
   Open your browser and navigate to `http://127.0.0.1:5000`

---

##  Security Implementation
The project satisfies Requirement 5 of the assignment by ensuring that **plain-text passwords are never stored**. 

```python
# Security Snippet from App.py
from werkzeug.security import generate_password_hash

# Hash before Database Commit
hashed = generate_password_hash(user_password, method='pbkdf2:sha256')
```

---

##  Author
**Christian Nnaji**  
- **Matric No:** 2024/B/SENG/0246  
- **Student ID:** 30037606  
- **Institution:** Miva Open University  
- **Course:** MIVA-CSC312 — Web Application Development  

---

##  License
This project is an academic submission for **Miva Open University**. All rights reserved. Powered by Nnaji Christian's Creative Logic.
