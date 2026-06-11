from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def getroute():
    return {"message":"Hello World"}