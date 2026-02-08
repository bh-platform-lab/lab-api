from fastapi import APIRouter

from app.api.v1.features import router as features_router

router = APIRouter()


@router.get("/hello")
def hello(name: str = "world"):
    return {"message": f"hello, {name}"}


router.include_router(features_router)
