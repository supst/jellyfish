# Frontend Dockerfile
FROM node:20-alpine AS builder

WORKDIR /app

# Install pnpm
RUN npm install -g pnpm

# Copy package files (context is root, so use front/)
COPY front/package.json front/pnpm-lock.yaml ./

# Install dependencies  
RUN pnpm install

# Copy source
COPY front/ .

# Build
RUN pnpm run build

# Production
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY front/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
