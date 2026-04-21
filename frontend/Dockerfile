# Stage 1: Build
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# Stage 2: Production
FROM node:18-alpine
WORKDIR /app
# Create non-root user
RUN addgroup -S hnggroup && adduser -S hnguser -G hnggroup
USER hnguser
COPY --from=builder /app .
EXPOSE 3000
CMD ["npm", "start"]