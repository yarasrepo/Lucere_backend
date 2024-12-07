from fastapi import FastAPI
from app.api import product
from utils.import_products import import_csv_data

app = FastAPI()

import_csv_data()

app.include_router(product.router)

@app.get("/")
def read_root():
    return {"message": "FastAPI app is running!"}

