# Stage 1: Build stage
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# Stage 2: Final stage
FROM node:18-alpine
WORKDIR /app

# Create non-root user (Required for fe_user_creation_cmd)
RUN addgroup -S hnggroup && adduser -S hnguser -G hnggroup
USER hnguser

COPY --from=builder /app .
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000 || exit 1

EXPOSE 3000
CMD ["npm", "start"]