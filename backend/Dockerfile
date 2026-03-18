# Backend Dockerfile
FROM python:3.11-slim

# Install uv
RUN pip install uv

WORKDIR /app

# Copy dependency files
COPY backend/pyproject.toml backend/uv.lock ./

# Install dependencies using uv
RUN uv sync --frozen --no-dev

# Copy source code
COPY backend/ .

# Create storage directory
RUN mkdir -p /app/storage

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
