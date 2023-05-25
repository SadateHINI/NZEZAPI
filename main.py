from fastapi import FastApi
app = FastApi()

@app.get("/")

async def root():
    return{"Message:" "I'm Front-end developper don't talk about database"}