# Yub-AiName (AI 起名系统)

An **AI-powered** Chinese name generation system with full user authentication, email verification, and DeepSeek LLM integration.

> Built with FastAPI, SQLAlchemy (async), MySQL, JWT, and LangChain.

## Features

- **AI Name Generation** — Generate 5 semantically rich Chinese names based on surname, gender, style preferences, and exclusions
- **DeepSeek Integration** — Powered by DeepSeek Chat (qwen3-max compatible) with structured JSON output
- **Email Verification** — QQ SMTP-based email code registration flow
- **JWT Authentication** — Dual token (access + refresh) with singleton-managed AuthHandler
- **Alembic Migrations** — Database schema versioning
- **Repository Pattern** — Clean separation of business logic and data access
- **Pydantic Validation** — All inputs/outputs validated

## Architecture

```
yub-ainame/
├── main.py                  # FastAPI entry point
├── dependencies.py          # FastAPI dependency injection
├── alembic/                 # Database migrations
├── core/
│   ├── auth.py              # JWT token handling (access + refresh)
│   ├── agent.py             # DeepSeek LLM integration for name generation
│   └── mail.py              # QQ SMTP email service
├── models/
│   ├── user.py              # User & EmailCode SQLAlchemy models
│   └── __init__.py          # Async engine & session factory
├── repository/
│   ├── user_repo.py         # User + EmailCode DB operations
│   └── __init__.py
├── routers/
│   ├── auth_router.py       # Register, login, email code endpoints
│   └── name_router.py       # AI name generation endpoint
├── schemas/
│   ├── user_schemas.py      # Auth request/response schemas
│   ├── agent.py             # Name generation result schemas
│   └── name.py              # Name input schema
└── settings/
    └── __init__.py          # Configuration (DB, email, JWT)
```

## Quick Start

```bash
# Install dependencies
pip install fastapi uvicorn sqlalchemy aiomysql pydantic python-jose fastapi-mail langchain-deepseek

# Set up MySQL database
# Update DB credentials in settings/__init__.py

# Run migrations
alembic upgrade head

# Start the server
uvicorn main:app --reload --port 8000
```

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/auth/code?email=` | Send email verification code |
| POST | `/auth/register` | Register with email + code |
| POST | `/auth/login` | Login with email + password |
| POST | `/names/generate` | Generate 5 Chinese names |
| GET | `/mail/test?email=` | Test email delivery |

## Tech Stack

- **FastAPI** — Async web framework
- **SQLAlchemy (async)** — MySQL ORM
- **JWT** — Access + Refresh token authentication
- **DeepSeek Chat** — LLM for name generation
- **QQ SMTP** — Email verification
- **Alembic** — Migration management
- **Pydantic** — Schema validation
