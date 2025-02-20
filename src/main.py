from fastapi import FastAPI
from routes import base,data
#from dotenv import load_dotenv
#load_dotenv(".env")

app = FastAPI()
app.include_router(base.base_router)
app.include_router(data.data_router)

#@app.get("/w")
#def read_root():
#    return {"Hello": "World"}