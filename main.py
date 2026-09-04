from fastapi import FastAPI

app = FastAPI()

@app.get("/health/details")
async def health_details():
    return {
        "status": "ok",
        "service": "backend",
        "version": "1.0.0"
    }
