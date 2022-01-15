import os

import berbix
from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException, status

load_dotenv()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
    
@app.post("/hook", 
        responses={
            200: {"description": "Validated Berbix signature."},
            400: {"description": "Could not validate Berbix signature"},
            }
        )
async def hook(info : Request):
    cl = berbix.Client(api_secret=os.getenv('BERBIX_API_SECRET'))
    # this secret key can be found in the webhook section of the dashboard
    webhook_secret = os.getenv('BERBIX_WEBHOOK_SECRET')
    # this is the body of the webhook request from Berbix
    req_json = await info.json()
    req_body = await info.body()
    # the berbix validate_signature method expects the request body as a string
    json_str = req_body.decode("utf-8")
    # content in the x-berbix-signature header, in the form v0,timestamp,signature
    signature = info.headers.get('x-berbix-signature')
    if not (cl.validate_signature(webhook_secret, json_str, signature)):
        raise HTTPException(
            status_code=400, 
            detail="Could not validate Berbix webhook signature"
            )
    return_dict = {
        "status" : "SUCCESS",
        "data" : req_json
    }
    return return_dict
