from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from api.src import routers

app = FastAPI()
for router in routers:
    app.include_router(router)

@app.get('/ping')
async def ping_pong():
    return {'ping': 'pong!'}