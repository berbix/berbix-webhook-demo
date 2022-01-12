import os

import berbix
from dotenv import load_dotenv
from fastapi import FastAPI, Request

load_dotenv()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
    
@app.post("/hook")
async def hook(info : Request):
    cl = berbix.Client(api_secret=os.getenv('BERBIX_API_SECRET'))
    # this secret key can be found in the webhook section of the dashboard
    webhook_secret = os.getenv('BERBIX_WEBHOOK_SECRET')
    # this is the body of the webhook request from Berbix
    req_json = await info.json()
    # content in the x-berbix-signature header, in the form v0,timestamp,signature
    signature = info.headers.get('x-berbix-signature')
    is_valid = cl.validate_signature(webhook_secret, req_json, signature)
    return_dict = {
        "status" : "SUCCESS",
        "data" : req_json
    }
    return return_dict
