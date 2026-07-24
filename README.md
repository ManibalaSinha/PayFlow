#  PayFlow — Enterprise Payment Processing Platform | FastAPI + PostgreSQL + Kafka

PayFlow is a production-style payment processing backend built with
FastAPI, PostgreSQL, and event-driven architecture.

The system demonstrates real-world financial engineering concepts:

- Idempotent payment processing
- Transaction consistency and ACID guarantees
- Retry handling for transient failures
- Reconciliation workflows
- Secure authentication
- Event-driven processing with Kafka
- Cloud-native deployment patterns

Built to simulate challenges found in modern banking and fintech platforms.
---

<p align="center">
  <img src="https://raw.githubusercontent.com/ManibalaSinha/ENTERPRISE-TRANSACTION-PLATFORM/main/backend/app/assets/cloudshell.png" width="600" />
  <img src="https://raw.githubusercontent.com/ManibalaSinha/ENTERPRISE-TRANSACTION-PLATFORM/main/backend/app/assets/PaymentFlow.png" width="600" />
  <img src="https://raw.githubusercontent.com/ManibalaSinha/ENTERPRISE-TRANSACTION-PLATFORM/main/backend/app/assets/InitiatePayment.png" width="600" />
  <img src="https://raw.githubusercontent.com/ManibalaSinha/ENTERPRISE-TRANSACTION-PLATFORM/main/backend/app/assets/userDetails.png" width="600" />
  <img src="https://raw.githubusercontent.com/ManibalaSinha/ENTERPRISE-TRANSACTION-PLATFORM/main/backend/app/assets/RetrievedData.png" width="600" />
  <img src="https://raw.githubusercontent.com/ManibalaSinha/ENTERPRISE-TRANSACTION-PLATFORM/main/backend/app/assets/RetrievingUrl.png" width="600" />
</p>
Payment workflow events:

payment.created
payment.validated
payment.processed
payment.settled
payment.failed
payment.reconciled

---

##  Problem Statement

In distributed payment systems:

* Network failures can cause **duplicate charges**
* Partial failures lead to **inconsistent transaction states**
* Systems must guarantee **eventual consistency**

**PayFlow solves this by combining idempotent APIs, retry mechanisms, and reconciliation workflows.**

---

##  Core Features

###  Payment Processing

* `POST /initiate-payment`
  → Idempotent payment creation using unique request keys

* `GET /payment-status/{payment_id}`
  → Real-time tracking of transaction state

---

###  Reliability & Fault Tolerance

* Retry mechanism with **exponential backoff**
* Safe handling of **transient failures**
* Idempotency guarantees to prevent duplicate charges

---

###  Reconciliation Engine

* `POST /reconcile`
  → Batch process to detect and fix inconsistent or failed transactions

---

###  Security

* JWT-based authentication
* Secure password hashing (Passlib)
* RBAC-ready architecture

---

###  Observability

* Structured logging for traceability
* Metrics-ready design for monitoring systems

---

##  System Architecture

## Architecture

Client
 |
 v
FastAPI API Gateway
 |
 v
Payment Service
 |
 +---- PostgreSQL (ACID Transactions)
 |
 +---- Kafka Event Bus
 |
 +---- Redis Cache
 |
 +---- Celery Workers
 |
 +---- Monitoring / Logging

## KAFKA
## Event-Driven Workflow

Payment lifecycle events:

payment.created
        |
        v
payment.validated
        |
        v
payment.processing
        |
        v
payment.completed

Failure scenarios:

payment.failed
payment.retry
payment.reconciled

### Design Principles:

* Clean separation of concerns (API → Service → DB)
* Stateless, scalable API design
* Transaction-safe operations with rollback support
* Fault isolation and recovery mechanisms

---

##  Key Engineering Highlights

* Designed **idempotent APIs** to ensure safe retries
* Implemented **ACID-compliant transactions** for financial consistency
* Built **retry logic with exponential backoff** for resilience
* Modeled domain entities: accounts, payments, audit logs
* Structured backend for **horizontal scalability**

---

##  Tech Stack

* **Backend:** Python, FastAPI
* **Database:** PostgreSQL
* **Auth:** JWT, Passlib
* **Infrastructure:** Docker, Docker Compose
* **Cloud Ready:** AWS (Lambda, SQS, RDS) / GCP (Cloud Run, Pub/Sub)

---

##  Project Structure

```
backend/
├── api/         # Route handlers
├── core/        # Config, security, utilities
├── models/      # SQLAlchemy models
├── schemas/     # Pydantic schemas
├── services/    # Business logic layer
├── db/          # DB session management
└── main.py
```

---

##  Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/ManibalaSinha/enterprise-transaction-platform.git
cd enterprise-transaction-platform
```

### 2. Configure environment

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/transactions
SECRET_KEY=your_secret
```

### 3. Run with Docker

```bash
docker-compose up --build
```

### Access:

* API → [http://localhost:8000](http://localhost:8000)
* Swagger → [http://localhost:8000/docs](http://localhost:8000/docs)

---

##  API Example

### Create Payment

```bash
POST /initiate-payment
```

```json
{
  "amount": 100,
  "currency": "USD",
  "idempotency_key": "abc123"
}
```

### Response

```json
{
  "payment_id": "uuid",
  "status": "pending"
}
```

---

##  Scalability & Performance

* Supports **high-throughput transaction systems**
* Designed for horizontal scaling and high-throughput transaction processing.
* Stateless services enable **horizontal scaling**
* Ready for queue-based async processing (SQS / PubSub)

---

##  Future Enhancements

* Stripe webhook integration (real payment gateway)
* Event-driven architecture (Kafka / PubSub)
* Rate limiting & throttling
* Fraud detection layer
* Admin dashboard & analytics
* CI/CD with automated testing

---

##  Why This Project Stands Out

This project demonstrates:

* Real-world **payment system design**
* Strong understanding of **distributed system challenges**
* Backend expertise in **FastAPI + PostgreSQL**
* Production-ready thinking (reliability, consistency, scaling)

**a system built for real financial workflows**

---

##  Author

**Manibala Sinha**
Senior Backend Engineer | Python | FastAPI

GitHub: [https://github.com/ManibalaSinha](https://github.com/ManibalaSinha)
