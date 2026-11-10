from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from app.analytics import initialize,run_query
app=FastAPI(title="Multi-Agent Analytics",version="0.1.0")
initialize()
class Query(BaseModel): question:str=Field(min_length=1); business_unit:str|None=None
@app.get("/health")
def health(): return {"status":"ok"}
@app.post("/query")
def query(req:Query):
    try: return run_query(req.question,req.business_unit)
    except ValueError as e: raise HTTPException(400,str(e)) from e
