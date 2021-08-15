import random

from fastapi import APIRouter, Body, Depends, Path, Query


def build_noise_router() -> APIRouter:
    router = APIRouter()

    @router.get("/ping")
    async def ping():
        return "PONG!"


    @router.get("/random")
    async def random(
            mean: float,
            std_dev: float,
        ):

        return random.random()

    return router
