# Simple Frontend Dockerfile
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y nodejs npm curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g pnpm && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy package files
COPY front/package.json front/pnpm-lock.yaml ./

# Install dependencies  
RUN pnpm install

# Copy source
COPY front/ .

# Build
RUN pnpm run build

EXPOSE 3000
CMD ["ls", "dist"]
