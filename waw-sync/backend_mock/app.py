from typing import Dict

from fastapi import FastAPI, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# ─── CORS (attach *after* app creation) ───────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── In‑memory store (not thread‑safe: fine for a mock) ───────────────────
store: Dict[str, dict] = {}

# ─── Request / response schema ────────────────────────────────────────────
class Profile(BaseModel):
    id: str
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    updated_at: int

class UpsertResponse(BaseModel):
    status: str
    count: int

# ─── Endpoint ─────────────────────────────────────────────────────────────
@app.post("/profile", response_model=UpsertResponse)
def upsert_profile(profile: Profile = Body(...)):
    store[profile.id] = profile.model_dump()
    return {"status": "ok", "count": len(store)}
