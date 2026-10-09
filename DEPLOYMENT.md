# Deployment and Operational Packaging

This document describes how to run Sash for evaluation and production use.

## Quick start (demo)

From a fresh clone:

```bash
# Option A: Docker Compose (recommended for evaluators)
docker compose up --build
# Then open http://localhost:8501

# Option B: Local Python environment
pip install -r requirements.txt
streamlit run app.py
```

No secrets are required for the demo; mock providers are used by default.

## Environment configuration

Key environment variables (all optional in demo mode):

- `ENVIRONMENT`: `dev`, `staging`, or `prod` (default: `dev`).
- `ENABLE_MOCK_PROVIDER`: `true` or `false` (default: `true` in demo).
- `PROVIDER_API_KEY`: API key for real provider (only in production).
- `WEBHOOK_SECRET`: Shared secret for webhook verification (production).
- `DATABASE_URL`: Database connection string (production).

Never commit real secrets to version control. Use Docker secrets, Kubernetes secrets, or your cloud secret manager.

## Health check

- Streamlit UI: `GET http://<host>:8501/health` (if configured) or simply check UI availability.
- API service (optional): `GET http://<host>:8000/health` returns `{"status": "ok", "version": "..."}`.

In Docker Compose, the Streamlit service includes a basic HTTP health check.

## Demo reset

To reset demo state to a known baseline:

```bash
# Remove local SQLite and cached data
rm -rf data/*.db data/*.sqlite
# Optionally clear Python caches
find . -type d -name __pycache__ -prune -exec rm -rf {} +
```

Then restart the app or containers. The next run will recreate a clean demo database.

## Durable storage guidance

- For evaluation: the default SQLite-backed storage in `data/` is sufficient.
- For production: replace SQLite with a managed database (Postgres, etc.) and configure `DATABASE_URL`.
- Persist the `sash-data` Docker volume or mount a host directory to `/app/data` to survive container restarts.

## Deployment notes

- Use the provided `Dockerfile` and `docker-compose.yml` as a starting point.
- For production, disable the mock provider, configure secrets, and set `ENVIRONMENT=prod`.
- Integrate with your CI/CD pipeline to build and deploy the Docker image.
- Monitor the health endpoint and application logs for operational visibility.

## Startup instructions (summary)

1. Ensure Docker or Python 3.11+ is installed.
2. Clone the repository and navigate to the project root.
3. For demo: run `docker compose up` or `streamlit run app.py`.
4. Open the UI at `http://localhost:8501` and run a sample workflow.
5. Use the **Deployment** page in the UI for health status and reset actions.
