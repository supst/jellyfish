"""健康检查（v1 内）。"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def v1_health():
    return {"status": "ok", "version": "v1"}
