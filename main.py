from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()


@app.get("/health")
def health_check():
    """Basic readiness endpoint."""
    return {"status": "ok"}


@app.get("/sum")
def sum_values(x: float | None = None, y: float | None = None):
    """Return the sum of query params x and y."""
    if x is None or y is None:
        raise HTTPException(status_code=400, detail="Both x and y query params are required.")
    return {"result": x + y}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

