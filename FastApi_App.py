from fastapi import FastAPI
import uvicorn

app=FastAPI()

@app.get("/")
def root():
    return {"Hey Buddy"}


@app.get("/status")
def status():
    return {"status": "running"}  


@app.get("/health")
def health():
    return {"health": "good"} 


@app.get("/info")
def info():
    return {"app": "Web App", "version": "1.0.0"}

if __name__ == "__main__":
   uvicorn.run(app, host="127.0.0.1", port=8000)
