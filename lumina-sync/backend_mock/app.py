from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

app = FastAPI()
store = {}

@app.post("/profile")
def upsert_profile(profile: dict = Body(...)):
    store[profile["id"]] = profile
    return {"status": "ok", "count": len(store)}
