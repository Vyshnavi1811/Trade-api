
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils import analyze_sector

app = FastAPI()
security = HTTPBearer()

FAKE_TOKEN = "mysecrettoken"

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != FAKE_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")

@app.get("/analyze/{sector}")
async def analyze(sector: str, token: str = Depends(verify_token)):
    return analyze_sector(sector)
