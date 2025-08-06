from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return JSONResponse(
        content={"message": "Luma działa ❤️"},
        media_type="application/json; charset=utf-8"
    )
