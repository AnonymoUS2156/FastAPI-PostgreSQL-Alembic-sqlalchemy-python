from fastapi import FastAPI

app = FastAPI()

@app.get("/get_synonyms/")
async def get_synonyms(synonyms: str):
    return synonyms
