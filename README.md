# 🏥 Hospital Management System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=for-the-badge)

A comprehensive **Desktop Application** built with **Python (Tkinter)** and **MySQL** to manage hospital records, patient prescriptions, and medical history efficiently.

---

## 📸 Interface Screenshots

| **Dashboard View**
![Dashboard View](screenshots/HMS.PNG)

---

## ✨ Key Features

* ✅ **Patient Registration:** Store patient details like Name, Address, DOB, and NHS Number.
* ✅ **Prescription Management:** Assign medicines, dosage, and side effects.
* ✅ **Database Integration:** All records are securely stored in a MySQL database.
* ✅ **CRUD Operations:**
    * **C**reate (Add new records)
    * **R**ead (View records in a Treeview table)
    * **U**pdate (Modify existing patient details)
    * **D**elete (Remove records)
* ✅ **Search & Filter:** Easily find patients by Reference No.

---

## 🛠️ Tech Stack

* **Frontend:** Python Tkinter (Standard GUI Library)
* **Backend:** MySQL Database (XAMPP / WAMP / MySQL Workbench)
* **Connector:** `mysql-connector-python`

---

## ⚙️ Prerequisites

Before running the project, make sure you have the following installed:

1.  **Python 3.10+** ([Download Here](https://www.python.org/downloads/))
2.  **MySQL Server** (via [XAMPP](https://www.apachefriends.org/) or [MySQL Workbench](https://dev.mysql.com/downloads/workbench/))
3.  **Git** (Optional, for cloning)

---

## 🚀 Installation & Setup

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository
Open your terminal (Command Prompt / Git Bash) and run:

```bash
git clone [https://github.com/your-username/hospital-management-system.git](https://github.com/your-username/hospital-management-system.git)
cd hospital-management-system
```

### 2. Install Dependencies
You need to install the MySQL connector for Python to allow the application to communicate with the database.

```bash
pip install mysql-connector-python 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
```

### 3. Database Configuration 🗄️
Open **MySQL Workbench** or **XAMPP (phpMyAdmin)**. Create a new database and table by running the following SQL script:

```sql
CREATE DATABASE mydata;
USE mydata;

CREATE TABLE hospital (
    Name_of_Tablets VARCHAR(100),
    Reference_No VARCHAR(100) NOT NULL PRIMARY KEY,
    Dose VARCHAR(100),
    No_of_Tablets VARCHAR(100),
    Lot VARCHAR(100),
    Issue_Date VARCHAR(100),
    Exp_Date VARCHAR(100),
    Daily_Dose VARCHAR(100),
    Side_Effect VARCHAR(100),
    Further_Information VARCHAR(100),
    Blood_Pressure VARCHAR(100),
    Storage_Advice VARCHAR(100),
    Medication VARCHAR(100),
    Patient_Id VARCHAR(100),
    NHS_Number VARCHAR(100),
    Patient_Name VARCHAR(100),
    Date_of_Birth VARCHAR(100),
    Patient_Address VARCHAR(100)
);
```
### 4. Update Credentials 🔑
Open `main.py` in your code editor (VS Code) and find the database connection lines. Update the `password` to match your local MySQL password.

```python
conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="YOUR_MYSQL_PASSWORD",  # <--- Change this
    database="mydata"
)
```
## ▶️ How to Run
Once everything is set up, run the application using your terminal:

```bash
python main.py
```
## 🤝 Contributing
Contributions are welcome! If you'd like to improve this project:

1.  **Fork** the project.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  **Commit** your changes (`git commit -m 'Add some AmazingFeature'`).
4.  **Push** to the branch (`git push origin feature/AmazingFeature`).
5.  Open a **Pull Request**.

## 📞 Contact
**Zia ul islam Mughal**

📧 Email: [ziaulislam0@gmail.com](mailto:ziaulislam0@gmail.com)  
🔗 LinkedIn: [https://www.linkedin.com/in/ziaulislammughal/](https://linkedin.com/in/yourprofile)

<br>

<p align="center">
  Made with ❤️ by <a href="https://github.com/ziaulislam-mughal">Zia ul Islam MUGHAL</a>
</p>