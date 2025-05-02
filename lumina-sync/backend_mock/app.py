from fastapi import FastAPI, Body
app = FastAPI()
store = {}

@app.post("/profile")
def upsert_profile(profile: dict = Body(...)):
    store[profile["id"]] = profile
    return {"status": "ok", "count": len(store)}
