from fastapi import FastAPI

app = FastAPI()

@app.post("/")
def fee():
    return {"delivery_fee": 0}