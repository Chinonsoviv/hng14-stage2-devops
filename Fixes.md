# FIXES LOG

## Bug 1: uvicorn not found
- Issue: uvicorn command not recognized
- Fix: used `python -m uvicorn main:app --reload`

## Bug 2: Redis connection refused
- Issue: worker could not connect to Redis
- Fix: started Redis using Docker

## Bug 3: Missing Python module
- Issue: ModuleNotFoundError (requests)
- Fix: installed requests using pip