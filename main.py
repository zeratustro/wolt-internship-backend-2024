import uvicorn
from fastapi import FastAPI
from modules.Order import Order

app = FastAPI()

@app.post("/")
def fee(item: Order):
    return {"delivery_fee": item.fee}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)