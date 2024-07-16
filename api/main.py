from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from api.src import routers

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

for router in routers:
    app.include_router(router, prefix='/api')

@app.get('/ping')
async def ping_pong():
    return {'ping': 'pong!'}