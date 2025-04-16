# 🔁 ClickHouse ⇄ Flat File Data Ingestion Web App

A full-stack web application for **bidirectional data ingestion** between **ClickHouse** and **Flat Files (CSV)**.  
This app supports JWT-authenticated ClickHouse access, custom column selection, multi-table joins, data previews, and progress tracking.

---

## 🚀 Features

### ✅ Core Functionality
- Export data from ClickHouse to Flat File (CSV)
- Import data from Flat File to ClickHouse
- JWT-based ClickHouse authentication
- Column selection and ingestion control
- Record count reporting on completion

### 🔄 Bonus Features
- **Multi-Table JOINs** (ClickHouse Source)
  - Select multiple tables
  - Specify JOIN conditions
  - Backend constructs and executes JOIN query

### 💡 Optional Enhancements
- **Progress Bar:** Displays ingestion progress in frontend
- **Data Preview:** Fetch and view first 100 records before ingestion

---

## 📁 Project Structure

project/ │ ├── backend/ │ ├── app.py # Main backend server │ ├── clickhouse_handler.py # Handles ClickHouse auth, SELECT/JOIN, CSV export │ ├── flatfile_handler.py # Reads CSV, validates types, writes to ClickHouse │ ├── test_ingestion.py # Sample test cases and ingestion flows │ ├── frontend/ │ └── src/ │ ├── components/ # React components (Forms, Preview, ProgressBar) │ ├── App.jsx # Root component │ ├── index.js # React entry point │ └── README.md

---
🧪 Testing
Use example datasets provided by ClickHouse:

uk_price_paid

ontime

✅ Recommended Test Cases:
Single ClickHouse table → Flat File (selected columns)

Flat File → New ClickHouse table

(Bonus) Joined ClickHouse tables → Flat File

Connection/authentication failure handling

(Optional) Data preview before ingestion

🖥️ Key UI Features
Source & Target Type Selection (ClickHouse or Flat File)

Dynamic form rendering based on source type

Table & Column selection UI

JOIN conditions input (if multiple tables selected)

CSV Upload (for Flat File)

Ingestion Progress Indicator

Real-time status and final record count

🤝 Contributions
Feel free to fork and enhance the app for:

Drag-and-drop CSV upload

Advanced JOIN builder

Error reporting UI

Upload logs

📄 License
MIT License – Open to use, modify, and share.

✨ Developed By
Yaseen – Full-stack Developer | GitHub | LinkedIn
## ⚙️ Setup & Configuration

### 🧩 Prerequisites
- Python 3.10+
- Node.js 16+ (for React frontend)
- Docker (for running ClickHouse locally) **or** access to a cloud ClickHouse instance

### 🔐 Environment Configuration
ClickHouse connection requires:
- `host`
- `port`
- `database`
- `user`
- `jwtToken` (used as password)

---

## 🛠️ Backend Setup (Python)

```bash
# 1. Navigate to backend
cd backend

# 2. Create virtual environment and activate
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the server
python app.py
# 1. Navigate to frontend
cd frontend

# 2. Install dependencies
npm install

# 3. Run the development server
npm start


Yaseen – Full-stack Developer | GitHub | LinkedIn
