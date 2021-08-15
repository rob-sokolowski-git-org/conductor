import logging

from conductor.routes.noise import build_noise_router
from fastapi import APIRouter



def build_all_routers() -> APIRouter:
    logging.info(f"Building all routers..")
    router = APIRouter()
    router.include_router(build_noise_router())
    return router