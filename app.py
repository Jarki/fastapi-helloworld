import os

import fastapi
from fastapi.staticfiles import StaticFiles 
import uvicorn


app = fastapi.FastAPI()

@app.get("/api")
def api_example():
    return {"ok": True}

app.mount("/", StaticFiles(directory="./static", html=True), name="html")

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("HOST", "0.0.0.0"), port=int(os.getenv("PORT", 8080)))


