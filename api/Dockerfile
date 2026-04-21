# Stage 1: Build (Multi-stage)
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final
FROM python:3.11-slim
WORKDIR /app

# Create a non-root user (Required for points)
RUN useradd -m hnguser
USER hnguser

# Copy only the installed packages and code
COPY --from=builder /root/.local /home/hnguser/.local
COPY . .

# Set paths and healthcheck
ENV PATH=/home/hnguser/.local/bin:$PATH
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

CMD ["python", "main.py"]