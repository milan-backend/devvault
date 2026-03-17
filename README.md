# 🚀 DevVault — Secure Environment Manager for Developers

DevVault is a developer-focused tool that simplifies how environment variables (`.env` files) are managed across projects and machines.

Instead of manually creating and sharing `.env` files, DevVault allows you to securely store secrets and generate `.env` files instantly using a CLI.

---

## ❗ Problem

Managing environment variables is messy and error-prone:

* Rewriting `.env` files for every project
* Sharing secrets insecurely (WhatsApp, email, etc.)
* Missing keys when switching devices
* Manual copy-paste every time

---

## ✅ Solution

DevVault provides:

* 🔐 Secure storage for secrets
* 📦 Project-based environment management
* ⚡ CLI tool to instantly generate `.env` files
* 🧩 Centralized system for developers

---

## ⚙️ How It Works

### 🔹 Step 1 — Setup (One-Time)

Using API (Swagger UI):

1. Signup
2. Create a project
3. Add secrets (key-value pairs)

---

### 🔹 Step 2 — Daily Usage

Using CLI:

```bash
devvault login <email> <password>
devvault pull <project_name>
```

👉 This automatically generates a `.env` file.

---

## 🧠 Example

Instead of writing:

```env
DATABASE_URL=...
SECRET_KEY=...
API_KEY=...
```

You just run:

```bash
devvault pull backend_project
```

👉 `.env` is generated instantly.

---

## 🏗️ Tech Stack

* FastAPI (Backend API)
* PostgreSQL (Database)
* SQLAlchemy (ORM)
* JWT Authentication
* Fernet Encryption (Secrets)
* Python CLI (Typer + Requests)

---

## 🔐 Security

* Secrets are encrypted before storage
* No secrets stored in plaintext
* `.env` file ignored via `.gitignore`
* JWT-based authentication
* Project-level access control

---

## 📁 Project Structure

```text
devvault/
│
├── routes/
│   ├── auth/
│   └── secret/
│
├── models/
├── schemas/
├── dependencies/
├── cli/
│   └── devvault_cli.py
│
├── database.py
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## 🚀 Running the Project

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Setup environment variables

Create `.env` file:

```env
DATABASE_URL=your_database_url
SECRET_KEY=SECRET_KEY
DEVVAULT_SECRET_KEY=your_fernet_key
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### 3️⃣ Run server

```bash
uvicorn main:app --reload
```

### 4️⃣ Open API docs

```
http://127.0.0.1:8000/docs
```

---

## 💻 CLI Usage

```bash
python cli/devvault_cli.py login <email> <password>
python cli/devvault_cli.py pull <project_name>
```

---

## 🎯 Key Features

* 🔐 Secure secret management
* ⚡ Instant `.env` generation
* 🧩 Project-based organization
* 🛠 CLI + API integration
* 🧱 Clean backend architecture

---

## 🚧 Future Improvements

* Web dashboard (UI)
* Team collaboration
* Secret versioning
* Secret rotation

---

## 💡 Why DevVault?

This project demonstrates:

* Real-world backend system design
* Authentication & security
* Encryption handling
* CLI + API integration
* Problem-solving beyond CRUD

---

## 👨‍💻 Author

Built by Milan — Backend Developer focused on building scalable systems and developer tools.

---

## ⭐ Final Note

DevVault is not just a project — it's a step toward building real developer infrastructure tools.
