FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends ripgrep && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml .
COPY agent/ agent/
COPY api.py .
COPY service.py .
COPY schemas.py .

RUN pip install --no-cache-dir -e .

RUN mkdir -p /workspace
WORKDIR /workspace

ENTRYPOINT ["sh", "-c", "uvicorn api:app --host 0.0.0.0 --port ${PORT}"]