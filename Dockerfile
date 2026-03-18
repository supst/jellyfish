# Combined Dockerfile (Frontend + Backend in one container)
# Note: For production, it's recommended to use separate containers with docker-compose

# ============ Frontend Build Stage ============
FROM node:20-alpine AS frontend-builder

RUN corepack enable && corepack prepare pnpm@latest --activate

WORKDIR /app/front

COPY front/package.json front/pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile

COPY front/ .
RUN pnpm run build

# ============ Backend Build Stage ============
FROM python:3.11-slim AS backend-builder

RUN pip install uv

WORKDIR /app/backend

COPY backend/pyproject.toml backend/uv.lock ./
RUN uv sync --frozen --no-dev

COPY backend/ .
RUN mkdir -p /app/storage

# ============ Production Stage ============
FROM python:3.11-slim

# Install nginx and supervisor
RUN apt-get update && apt-get install -y nginx supervisor && rm -rf /var/lib/apt/lists/*

# Create directories
RUN mkdir -p /app/storage /var/log/supervisor

# Copy backend
COPY --from=backend-builder /app /app

# Copy frontend build
COPY --from=frontend-builder /app/front/dist /app/front/dist

# Copy configs
COPY combined/nginx.conf /etc/nginx/sites-available/default
COPY combined/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

WORKDIR /app

EXPOSE 80 8000

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
