# CQRS + Event Sourcing with Django & FastAPI (SQLite + Service Discovery)

This project demonstrates a **Command Query Responsibility Segregation
(CQRS)** architecture combined with **Event Sourcing**, implemented
using:

-   **Django** → Write side (commands + event store)
-   **FastAPI** → Read side (queries + projections)
-   **SQLite** → Persistence for both sides
-   **Service Discovery** → Dynamic service lookup (without load
    balancing)

The goal is to provide a **clear, educational, but realistic** reference
architecture for distributed systems.

------------------------------------------------------------------------

## Architecture Overview

The system is split into **two independent services**, each with a
single responsibility.

-   **Write Side (Django)**\
    Handles commands, enforces business rules, and stores events.

-   **Read Side (FastAPI)**\
    Serves queries using denormalized read models built from events.

Each side owns its own database and can be scaled or replaced
independently.

------------------------------------------------------------------------

## Core Concepts

### CQRS (Command Query Responsibility Segregation)

CQRS separates **writes** from **reads**.

-   Commands change state
-   Queries return state
-   Write and read models are different
-   Databases are independent

Commands never return domain data, only success or failure.\
Queries never modify state.

------------------------------------------------------------------------

### Event Sourcing

Instead of persisting current state, the system persists **events**.

Examples: - AccountCreated - MoneyDeposited - MoneyWithdrawn

Current state is rebuilt by replaying events.

Benefits: - Full audit trail - Time travel and replay - Easier
debugging - Strong business invariants

------------------------------------------------------------------------

## Write Side (Django)

### Responsibilities

-   Accept commands
-   Load aggregates by replaying events
-   Validate business rules
-   Emit and persist new events

### Event Store

-   Implemented as a Django model
-   Append-only
-   Stored in `write_db.sqlite3`
-   Source of truth for the system

### Aggregates

Aggregates: - Represent business concepts - Apply events to rebuild
state - Decide whether commands are valid - Emit new events

They do not directly interact with the database.

------------------------------------------------------------------------

## Read Side (FastAPI)

### Responsibilities

-   Serve read-only queries
-   Use denormalized projections
-   Never enforce business rules
-   Never write events

### Read Models (Projections)

-   Built from events
-   Optimized for reads
-   Can be rebuilt at any time
-   Stored in `read_db.sqlite3`

### API Layer

FastAPI exposes read-only endpoints such as:

GET /accounts/{account_id}

These endpoints are safe to scale independently.

------------------------------------------------------------------------

## Event Projection Flow

1.  Events are written to the Django event store
2.  A projector consumes events
3.  Read models are updated
4.  FastAPI serves queries from projections

The system is **eventually consistent**.

------------------------------------------------------------------------

## Service Discovery

Service discovery removes hardcoded service URLs.

### Service Registry

A lightweight FastAPI-based registry provides: - Service registration -
Heartbeats - Service discovery

### Registration

Each service registers itself on startup with: - Service name - Host -
Port

### Heartbeats

Services periodically send heartbeats to indicate liveness.\
Stale services are removed automatically.

### Discovery

Clients query the registry to dynamically locate services.

------------------------------------------------------------------------

## SQLite Usage

SQLite is used for simplicity and clarity.

Advantages: - Zero configuration - Easy debugging - Ideal for learning
and demos

Limitations: - Single writer - No horizontal scaling

The architecture can be migrated to PostgreSQL or MySQL without
structural changes.

------------------------------------------------------------------------

## How to Run the Project

### Prerequisites

-   Python 3.10+
-   pip
-   virtualenv (recommended)

------------------------------------------------------------------------

### 1. Clone the Repository

``` bash
git clone https://github.com/samueladole/cqrs-event-sourcing-django-fastapi.git
cd cqrs-event-sourcing-django-fastapi
```

------------------------------------------------------------------------

### 2. Create and Activate Virtual Environment

``` bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate    # Windows
```

------------------------------------------------------------------------

### 3. Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

### 4. Start the Service Registry

``` bash
cd registry
fastapi dev main.py --port 9000
```

------------------------------------------------------------------------

### 5. Start the Write Side (Django)

``` bash
cd write_side
python manage.py migrate
python manage.py runserver 8000
```

This creates `write_db.sqlite3` and starts the command API.

------------------------------------------------------------------------

### 6. Initialize the Read Side Database

``` bash
cd read_side
python -c "from database.init_db import init_db; init_db()"
```

This creates `read_db.sqlite3`.

------------------------------------------------------------------------

### 7. Start the Read Side (FastAPI)

``` bash
cd read_side
fastapi dev main.py --port 8001
```

The read service will register itself with the service registry on
startup.

------------------------------------------------------------------------

### 8. Using the System

-   Send **commands** to the Django write API
-   Project events into the read database
-   Query **read models** via FastAPI

------------------------------------------------------------------------

## What This Architecture Demonstrates

-   True CQRS separation
-   Event sourcing fundamentals
-   Independent read/write scaling
-   Service discovery without tight coupling
-   Rebuildable read models
-   Clean domain boundaries

------------------------------------------------------------------------

## Intentionally Excluded

To keep the example focused: - No load balancing - No message brokers -
No async processing - No authentication

These can be added later without changing core concepts.

------------------------------------------------------------------------

## Key Takeaway

CQRS separates responsibility.\
Event sourcing preserves truth.\
Service discovery removes coupling.

Together, they form a scalable and evolvable system architecture.
