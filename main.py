from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
   return { "details": "Test-test, check-check" }