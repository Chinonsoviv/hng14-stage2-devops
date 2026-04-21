from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis
import uuid
import os

app = FastAPI()

# FIX: Use environment variable for Redis host (defaults to 'localhost' for local dev)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

# FIX: Define a schema so Swagger gives you an input box
class JobRequest(BaseModel):
    title: str
    description: str = ""

@app.post("/jobs", status_code=201)
def create_job(job: JobRequest): # Now Swagger will let you type!
    job_id = str(uuid.uuid4())
    
    # Store job data and status
    r.hset(f"job:{job_id}", mapping={
        "title": job.title,
        "status": "queued"
    })
    
    # Push ID to queue for the worker
    r.lpush("job", job_id)
    
    return {"job_id": job_id}

@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    job_data = r.hgetall(f"job:{job_id}")
    if not job_data:
        raise HTTPException(status_code=404, detail="Job not found")
    
    return {"job_id": job_id, "status": job_data.get("status")}