# 🚀 Two-Tier DevOps Web Application

A **Two-Tier Web Application** built using **Flask** and **MySQL**, fully containerized with **Docker**, orchestrated using **Docker Compose**, and deployed automatically using a **Jenkins CI/CD pipeline**.

This project demonstrates **end-to-end DevOps practices** on a local machine without any cloud dependency.

---

## 📌 Project Overview

This application follows a **two-tier architecture**:

- **Tier 1 – Application Layer**
  - Flask-based web application
  - Welcome page with project details
  - User input form
  - Displays user data from database

- **Tier 2 – Database Layer**
  - MySQL database
  - Runs in a separate Docker container
  - Persists user information

All components are containerized and managed using Docker Compose, with CI/CD automation handled by Jenkins.

---

## 🛠️ Tech Stack

| Category           |      Technology |
|--------------------|-----------------|
| Frontend & Backend |  Flask (Python) |
| Database           |       MySQL     |
| Containerization   |      Docker     |
| Orchestration      |  Docker Compose |
| CI/CD              |      Jenkins    |
| Version Control    |   Git & GitHub  |
| OS                 |      Linux      |

---

## ✨ Features

- 📄 Welcome page with project overview
- ➕ User registration form (Name, Email, Role)
- 🗄️ Data persistence using MySQL
- 🔄 Dynamic data fetch and display
- 🐳 Fully Dockerized application
- ⚙️ Automated CI/CD using Jenkins
- 🧪 Database health checks

---


## 🚀 Getting Started (Run Locally)

### ✅ Prerequisites

Ensure the following are installed:

- Docker
- Docker Compose (v2)
- Git
- Jenkins

---

### ▶️ Run the Application

From the project root directory:

```bash
docker compose up -d --build
```

## 🧪 Future Enhancements

- Full CRUD operations (Update/Delete users)
- Nginx reverse proxy
- GitHub Webhooks for auto builds
- Cloud deployment (AWS EC2)
- Kubernetes migration
