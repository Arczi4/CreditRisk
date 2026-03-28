# CreditRisk — Backend

FastAPI application providing credit risk scoring via a scikit-learn ML pipeline and LLM-generated analyst insights via LangChain and RAG.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Local Setup](#local-setup)
- [Environment Variables](#environment-variables)
- [Model Artifact](#model-artifact)
- [Running the Server](#running-the-server)
- [Code Quality](#code-quality)
- [Docker Setup](#docker-setup)

---

## Prerequisites

- **Python 3.12+**
- **Poetry** — [installation guide](https://python-poetry.org/docs/#installation)
- **OpenAI API key** — required for LLM inference and embeddings

---

## Local Setup

1. Navigate to the backend directory:

```bash
cd apps/backend
```

2. Install dependencies via Poetry:

```bash
poetry install
```

3. Create a `.env` file in the `apps/backend/` directory (see [Environment Variables](#environment-variables)).

4. Place the trained model artifact in the correct location (see [Model Artifact](#model-artifact)).

---

## Environment Variables

Create a `.env` file in `apps/backend/` with the following:

```env
OPENAI_API_KEY=your-openai-api-key
```

The OpenAI key is used by LangChain for both the LLM (`gpt-5.4-mini`) and the embedding model (`text-embedding-3-large`).

Additional settings can be overridden via environment variables (see `app/core/settings.py`):

| Variable       | Default                | Description                     |
|----------------|------------------------|---------------------------------|
| `HOST`         | `0.0.0.0`             | Server bind address             |
| `PORT`         | `8000`                 | Server port                     |
| `DEBUG`        | `True`                 | Enable debug mode               |
| `CORS_ORIGINS` | `http://localhost:4200`| Allowed CORS origins            |
| `LOG_DIR`      | `logs`                 | Directory for log files         |

---

## Model Artifact

The ML pipeline requires a trained model file to be present at:

```
apps/backend/app/ml/models/log_reg_pipeline_without_outliers_v2.pkl
```

This file is not included in the repository. The full training pipeline (feature engineering, calibration, evaluation) is available at:

[predicting_loan_payback](https://github.com/Arczi4/kaggle-competitions/tree/master/predicting_loan_payback)

---

## Running the Server

Start the development server from the `apps/backend/` directory:

```bash
poetry run uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

Useful endpoints:

| Endpoint                | Method | Description                          |
|-------------------------|--------|--------------------------------------|
| `/`                     | GET    | Project info and version             |
| `/health`               | GET    | Health check                         |
| `/api/payback/single`   | POST   | Credit risk scoring + LLM analysis   |

Interactive API documentation is available at `http://localhost:8000/docs` (Swagger UI).

**Note on first startup**: If the Chroma vector store does not exist yet (`rag/chrome_db/`), the application will automatically load and embed the policy documents from `rag/docs/` on first run. This requires a valid OpenAI API key and may take a moment.

---

## Code Quality

The project uses the following tools for code quality:

```bash
# Format code
poetry run black .

# Lint
poetry run ruff check .

# Type checking
poetry run mypy .

# Run tests
poetry run pytest
```

Pre-commit hooks are configured via `.pre-commit-config.yaml`. To set up:

```bash
poetry run pre-commit install
```

---

## Docker Setup

> **Planned** — Docker configuration will be added in a future update.
