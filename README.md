

# 🧑‍💼 Employee Management System

A simple web-based application built using **Flask** and **SQLite**, designed to manage employee records through a clean and user-friendly interface.

---

## 📌 Features

* 🔍 View a list of all employees in a dashboard
* ➕ Add new employees with:

  * Name
  * Post
  * Email
  * Phone number
* 📝 Edit existing employee information
* ❌ Delete employee records
* 💡 Clean UI styled with custom CSS or Bootstrap

---

## 🚀 Getting Started

Follow these steps to set up and run the project locally:

1. **Clone the repository**

   ```bash
   git clone https://github.com/BhartiSinghal16/EmployeeManagementSystem.git
   cd EmployeeManagementSystem
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   venv\Scripts\activate      # On Windows  
   source venv/bin/activate   # On Linux/Mac  
   ```

3. **Install dependencies**

   ```bash
   pip install flask
   ```

4. **Set up the database**

   * Run this Python script once to initialize the SQLite database:

     ```python
     import sqlite3

     conn = sqlite3.connect('employees.db')
     conn.execute('''
     CREATE TABLE employees (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         post TEXT NOT NULL,
         email TEXT NOT NULL,
         phone TEXT NOT NULL
     )
     ''')
     conn.close()
     ```
   * Alternatively, save the code above in `init_db.py` and run:

     ```bash
     python init_db.py
     ```

5. **Run the application**

   ```bash
   python app.py
   ```

   * Then open your browser and go to:

     ```
     http://127.0.0.1:5000/
     ```

---

## 📂 Project Structure

```
EmployeeManagementSystem/
├── app.py
├── employees.db
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add.html
│   └── edit.html
├── static/
│   └── style.css
├── .gitignore
└── README.md
```

---

## 📌 Future Improvements

* Add login/authentication (admin panel)
* Add search/filter functionality
* Upload employee profile pictures
* Export data to Excel or PDF
* Use MySQL or PostgreSQL in production

