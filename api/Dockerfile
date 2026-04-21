# Stage 1: Build stage
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final stage
FROM python:3.11-slim
WORKDIR /app

# Install curl (Required for the healthcheck to work)
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Create a non-root user (Required for api_user_creation_cmd)
RUN useradd -m hnguser
USER hnguser

# Copy installed packages from builder
COPY --from=builder /root/.local /home/hnguser/.local
COPY . .

# Set paths and healthcheck
ENV PATH=/home/hnguser/.local/bin:$PATH
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

CMD ["python", "main.py"]