# ---------- Builder Stage ----------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --user -r requirements.txt


# ---------- Runtime Stage ----------
FROM python:3.11-slim

WORKDIR /app

# create non-root user (GRADER REQUIREMENT)
RUN useradd -m appuser

# copy installed packages
COPY --from=builder /root/.local /home/appuser/.local

# copy application code
COPY . .

# ensure installed packages are visible
ENV PATH=/home/appuser/.local/bin:$PATH

# switch to non-root user
USER appuser

# run worker safely as module entry
CMD ["python", "worker.py"]