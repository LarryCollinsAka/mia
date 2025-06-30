from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import os


app = FastAPI()

VERIFY_TOKEN = os.getenv("WHATSAPP_VERIFY_TOKEN", "super-mia-token")

@app.get("/webhook")
def verify(request: Request):
    params = dict(request.query_params)
    if params.get("hub.mode") == "subscribe" and params.get("hub.verify_token") == VERIFY_TOKEN:
        return PlainTextResponse(params["hub.challenge"])
    return PlainTextResponse("Verification failed", status_code=403)

