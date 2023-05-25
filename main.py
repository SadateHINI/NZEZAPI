from fastapi import FastAPI
app = FastAPI()

@app.get("/")

async def root():
    return{"Message:" "I'm Front-end developper don't talk about database"}
