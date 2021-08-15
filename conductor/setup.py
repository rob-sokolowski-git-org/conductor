import asyncio
import json
import logging
import sys
import uvicorn
import time
import random

from conductor.routes.setup import build_all_routers
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional


app = FastAPI(title="conductor_api")
app.include_router(router=build_all_routers())

# set global random seed
now_seed = int(time.time())
random.seed(now_seed)
logging.info(f"random seed set random system clock: {now_seed}")

# Cors stuff: currently this is only needed for local demos that hit this from the browser
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.info(f"Running uvicorn..")
uvicorn.run(app, host="0.0.0.0", port=8000)
