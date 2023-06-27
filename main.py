from fastapi import FastAPI
import uvicorn
from routes.auth import router

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Heelo"}


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
