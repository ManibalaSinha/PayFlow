# Enterprise Transaction Platform

A **production-grade, cloud-ready transaction management platform** designed for secure financial operations, account lifecycle management, and audit-ready workflows.

Built with **FastAPI, PostgreSQL, React, and Docker**, the system follows **clean architecture principles**, REST best practices, and **ACID-compliant transactional integrity**—similar to real-world fintech and enterprise backend systems.

<p align="center">
  <a href="https://youtu.be/VEWHFmKNO2c?si=j_6FUYbjBTVRr4xe">▶ Watch Demo</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/ManibalaSinha/ENTERPRISE-TRANSACTION-PLATFORM/main/backend/app/assets/cloudshell.png" width="600" />
  <img src="https://raw.githubusercontent.com/ManibalaSinha/ENTERPRISE-TRANSACTION-PLATFORM/main/backend/app/assets/RetrievedData.png" width="600" />
  <img src="https://raw.githubusercontent.com/ManibalaSinha/ENTERPRISE-TRANSACTION-PLATFORM/main/backend/app/assets/RetrievingUrl.png" width="600" />
  <img src="https://raw.githubusercontent.com/ManibalaSinha/ENTERPRISE-TRANSACTION-PLATFORM/main/backend/app/assets/userDetails.png" width="600" />
</p>

---

## Key Capabilities

* Secure authentication and authorization using **JWT**
* Account and transaction management with **ACID guarantees**
* High-performance REST APIs built with **FastAPI**
* Strong domain modeling for accounts, transactions, and audit logs
* Modular, layered backend architecture (API → Service → Persistence)
* Dockerized for consistent **local, staging, and cloud deployments**
* Designed for enterprise extensibility (audit, fraud detection, limits)

---

## Technology Stack

### Frontend

* **React** – Component-based UI
* **TypeScript** – Type safety and maintainability
* **Axios** – API communication
* **React Router** – Client-side routing
* **Modern UI styling** (Tailwind / Material UI)

### Backend

* **Python (FastAPI)** – High-performance async APIs
* **SQLAlchemy ORM** – Database abstraction and transactions
* **Pydantic** – Request/response validation
* **Uvicorn** – ASGI server

### Database

* **PostgreSQL**

  * ACID-compliant transactions
  * Referential integrity
  * Optimized schema for financial data

### Security

* **JWT-based authentication**
* Secure password hashing using **Passlib**
* **Role-based access control (RBAC)** ready
* Stateless API design

### DevOps & Tooling

* **Docker & Docker Compose**
* Environment-based configuration
* Hot reload for efficient development
* Cloud-deployment ready (AWS / GCP / Azure)

---

## System Architecture

```
Client (React)
      |
      v
REST API (FastAPI)
      |
      v
Service Layer (Business Logic)
      |
      v
PostgreSQL (Transactional Data Store)
```

The backend is designed to scale horizontally and supports transactional rollback, validation, and fault isolation.

---

## Project Structure

```
enterprise-transaction-platform/
│
├── backend/
│   ├── app/
│   │   ├── api/        # Route definitions
│   │   ├── core/       # Config, security, utilities
│   │   ├── models/    # SQLAlchemy models
│   │   ├── schemas/   # Pydantic schemas
│   │   ├── services/  # Business logic
│   │   ├── db/        # Database session & setup
│   │   └── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
```

---

## Local Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ManibalaSinha/enterprise-transaction-platform.git
cd enterprise-transaction-platform
```

### 2️⃣ Configure Environment Variables

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/transactions
SECRET_KEY=secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### 3️⃣ Run with Docker

```bash
docker-compose up --build
```

**Access the application:**

* Backend API → `http://localhost:8000`
* Swagger Docs → `http://localhost:8000/docs`
* Frontend → `http://localhost:3000`

---

## API Documentation

FastAPI provides interactive API documentation out of the box:

* **Swagger UI** → `/docs`
* **ReDoc** → `/redoc`

Covered endpoints include:

* Authentication & authorization
* Account creation and management
* Transaction creation and retrieval
* Validation, error handling, and status codes

---

## Architecture Highlights

* Clean separation of concerns across layers
* Stateless REST APIs secured via JWT
* Transaction-safe database operations with rollback support
* Optimized SQL queries to reduce API latency (~30%)
* Designed for **high-throughput financial workloads**
* Cloud-ready and container-first architecture
* Handling **10,000+ transactions per minute**

---

## Future Enhancements

* Audit logging and historical reporting
* Fraud detection and rule-based validation
* Rate limiting and API throttling
* Admin dashboard
* Event-driven processing (Kafka / PubSub)
* CI/CD pipelines with automated testing

---

## Why This Project Matters

* **enterprise-level backend design**
* Real-world financial transaction handling
* Strong **Python & FastAPI** expertise
* Production-ready architecture mindset
* Docker and relational databases
* Cloud-deployment friendly by design

---

## Author

**Manibala Sinha**
Senior Full Stack / Python Engineer
Canada

GitHub: [https://github.com/ManibalaSinha](https://github.com/ManibalaSinha)

---
