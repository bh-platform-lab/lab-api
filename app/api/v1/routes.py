from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
def hello(name: str = "world"):
    return {"message": f"hello, {name}"}
