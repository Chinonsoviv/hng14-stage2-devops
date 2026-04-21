from fastapi import FastAPI, HTTPException
import redis
import uuid

app = FastAPI()

r = redis.Redis(host="redis", port=6379, decode_responses=True)


@app.post("/jobs")
def create_job():
    job_id = str(uuid.uuid4())

    r.hset(f"job:{job_id}", mapping={"status": "queued"})
    r.lpush("job", job_id)

    return {"job_id": job_id}


@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    job_data = r.hgetall(f"job:{job_id}")

    if not job_data:
        raise HTTPException(status_code=404, detail="Job not found")

    return {
        "job_id": job_id,
        "status": job_data.get("status")
    }
