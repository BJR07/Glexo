# 🚀 Glexo - Django Mini Search Engine

## 📖 Overview

Glexo is a Django-based mini search engine that enables users to search documents efficiently using keyword-based retrieval. The application implements an inverted index for faster searching, ranks results based on term frequency, and provides user authentication along with search history tracking.

---

## ✨ Features

* 🔍 Keyword-based document search
* ⚡ Inverted Index implementation for faster retrieval
* 📊 Search result ranking based on term frequency
* 👤 User Registration and Login System
* 🕒 Search History Management
* 📄 Document Detail Page
* 🛠️ Django Admin Panel for document management
* 🎨 Responsive UI with Bootstrap
* ☁️ Deployed on Render

---

## 🛠️ Tech Stack

* Python
* Django
* MySQL / SQLite
* HTML5
* CSS3
* Bootstrap 5
* Django ORM
* Git & GitHub
* Render
* Gunicorn
* WhiteNoise

---

## 📂 Project Structure

```text
Glexo/
│
├── search/
├── templates/
├── static/
├── media/
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/glexo.git
cd glexo
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 🔍 How Search Works

Glexo uses an **Inverted Index** data structure.

Example:

```python
{
    "python": [1, 2, 3],
    "django": [2, 5]
}
```

When a user searches for a keyword:

1. The keyword is matched in the inverted index.
2. Relevant documents are retrieved.
3. Results are ranked based on keyword frequency.
4. Matching documents are displayed to the user.

---

## 📸 Screenshots

### Home Page

<img width="1896" height="827" alt="Screenshot 2026-06-21 111947" src="https://github.com/user-attachments/assets/420fd8fe-c6ef-432b-8b07-6123d240af53" />


### Search Results

<img width="1817" height="823" alt="Screenshot 2026-06-21 111547" src="https://github.com/user-attachments/assets/ce317836-f44e-481d-bbab-78cd0c4cd509" />


### Document Details Page

<img width="1802" height="781" alt="Screenshot 2026-06-21 111604" src="https://github.com/user-attachments/assets/3e8bb418-a0ea-4e4f-bc36-d0488068a69b" />


### Login Page

<img width="1827" height="773" alt="Screenshot 2026-06-21 111710" src="https://github.com/user-attachments/assets/1a835616-ccd1-4237-80b1-424fb78d33c9" />

### History page
<img width="1853" height="647" alt="Screenshot 2026-06-21 111731" src="https://github.com/user-attachments/assets/a3257683-1486-4b05-8fa9-e3ca5bc3cee8" />

---

## 🎯 Key Learning Outcomes

* Django Models & ORM
* Authentication System
* Search Algorithms
* Inverted Indexing
* Information Retrieval Concepts
* Database Design
* Deployment using Render
* Git & GitHub Workflow

---

## 📈 Future Enhancements

* Fuzzy Search
* Auto Suggestions
* TF-IDF Ranking
* Search Analytics Dashboard
* REST API Integration
* Elasticsearch Integration

---

## 👨‍💻 Author

**Biswajit Rout**

📧 Email: [work.bjr07@gmail.com](mailto:work.bjr07@gmail.com)

💼 LinkedIn: linkedin.com/in/bjr07

🌐 GitHub: github.com/bjr07

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
