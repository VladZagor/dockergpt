import uvicorn
from fastapi import FastAPI
from private_gpt import PrivateGPT
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/update_db")
async def update_db():
    pgpt = PrivateGPT()
    await pgpt.update_documents()


@app.post("/ask")
async def ask(question: str):
    pgpt = PrivateGPT()
    answer, docs = pgpt.ask(question)
    resp = {
        "question": question,
        "answer": answer,
        "sources": [d.__dict__ for d in docs]
    }
    return json.dumps(resp)

if __name__ == "__main__":
    # Initially update documents
    pgpt = PrivateGPT()
    pgpt.update_documents()
    # Start the server
    uvicorn.run(app, host="0.0.0.0", port=8000)
