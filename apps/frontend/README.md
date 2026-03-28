# CreditRisk — Frontend

Angular single-page application providing the user interface for credit risk analysis. Users submit loan application data through a form and receive ML-scored decisions with LLM-generated analyst insights.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Local Setup](#local-setup)
- [Environment Configuration](#environment-configuration)
- [Running the Development Server](#running-the-development-server)
- [Building for Production](#building-for-production)
- [Code Quality](#code-quality)
- [Docker Setup](#docker-setup)

---

## Prerequisites

- **Node.js 20+**
- **npm** (included with Node.js)
- **Angular CLI** — installed globally or used via npx

```bash
npm install -g @angular/cli
```

---

## Local Setup

1. Navigate to the frontend directory:

```bash
cd apps/frontend
```

2. Install dependencies:

```bash
npm install
```

3. Make sure the backend is running at `http://localhost:8000` (see [`apps/backend/README.md`](../backend/README.md) for backend setup).

---

## Environment Configuration

API URL configuration is located in the `src/environments/` directory:

| File                     | `apiUrl`                | Usage          |
|--------------------------|-------------------------|----------------|
| `environment.ts`         | `http://localhost:8000` | Development    |
| `environment.prod.ts`    | *(empty — set at build)*| Production     |

For local development, the default configuration points to the backend running on port `8000`. No changes are needed unless the backend runs on a different host or port.

---

## Running the Development Server

Start the Angular development server:

```bash
ng serve
```

Or using npm:

```bash
npm start
```

The application will be available at `http://localhost:4200`. It will automatically reload when source files are modified.

---

## Building for Production

To create an optimized production build:

```bash
ng build
```

Build artifacts will be written to the `dist/` directory. Set the `apiUrl` in `environment.prod.ts` to the production backend URL before building.

---

## Code Quality

The project uses Prettier for code formatting:

```bash
npx prettier --check .
npx prettier --write .
```

To run unit tests:

```bash
ng test
```

---

## Docker Setup

> **Planned** — Docker configuration will be added in a future update.
