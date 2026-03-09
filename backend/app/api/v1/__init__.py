"""API v1 路由聚合。"""

from fastapi import APIRouter

from app.api.v1.routes import health, example

router = APIRouter()

router.include_router(health.router, tags=["health"])
router.include_router(example.router, prefix="/example", tags=["example"])
