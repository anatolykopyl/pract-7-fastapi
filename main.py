from fastapi import FastAPI, HTTPException
from typing import List
from models import Term

app = FastAPI()

glossary = {}

@app.get("/terms/", response_model=List[Term])
async def get_terms():
    return list(glossary.values())

@app.get("/terms/{keyword}", response_model=Term)
async def get_term(keyword: str):
    if keyword not in glossary:
        raise HTTPException(status_code=404, detail="Term not found")
    return glossary[keyword]

@app.post("/terms/", response_model=Term)
async def add_term(term: Term):
    if term.keyword in glossary:
        raise HTTPException(status_code=400, detail="Term already exists")
    glossary[term.keyword] = term
    return term

@app.put("/terms/{keyword}", response_model=Term)
async def update_term(keyword: str, term: Term):
    if keyword not in glossary:
        raise HTTPException(status_code=404, detail="Term not found")
    glossary[keyword] = term
    return term

@app.delete("/terms/{keyword}", response_model=dict)
async def delete_term(keyword: str):
    if keyword not in glossary:
        raise HTTPException(status_code=404, detail="Term not found")
    del glossary[keyword]
    return {"detail": "Term deleted"}