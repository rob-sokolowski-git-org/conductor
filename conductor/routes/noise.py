import numpy as np

from fastapi import APIRouter, Body, Depends, Path, Query
from pydantic import BaseModel
import time
import typing as t
import logging


class _RandomResponse(BaseModel):
    query: t.Dict[str, t.Any]
    result: float


def build_noise_router() -> APIRouter:
    router = APIRouter()


    @router.get("/ping")
    async def ping():
        return "PONG!"


    @router.get("/random")
    async def random(
            mean: float,
            std_dev: float,
        ) -> _RandomResponse:

        # logging.info(f"sleeping for 10 secs...")
        # time.sleep(10)

        return _RandomResponse(
            query={
                "mean": mean,
                "std_dev": std_dev,
            },
            result=np.random.normal(mean, std_dev, 1)[0],
        )

    return router
