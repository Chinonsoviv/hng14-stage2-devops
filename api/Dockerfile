# Stage 1: Build stage
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final stage (Multi-stage)
FROM python:3.11-slim
WORKDIR /app

# Create a non-root user (Required for api_user_creation_cmd)
RUN useradd -m hnguser
USER hnguser

# Copy installed packages from builder
COPY --from=builder /root/.local /home/hnguser/.local
COPY . .

ENV PATH=/home/hnguser/.local/bin:$PATH
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

CMD ["python", "main.py"]