from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(prefix="/features", tags=["features"])

# In-memory store for now (later you can replace with DB/Redis)
_FEATURES: dict[str, bool] = {
    "dark_mode": False,
    "beta_banner": True,
}


class FeatureFlag(BaseModel):
    name: str = Field(min_length=2, max_length=50, pattern=r"^[a-z0-9_]+$")
    enabled: bool


@router.get("/", response_model=dict[str, bool])
def list_features():
    return _FEATURES


@router.get("/{name}", response_model=FeatureFlag)
def get_feature(name: str):
    if name not in _FEATURES:
        raise HTTPException(status_code=404, detail="feature_not_found")
    return {"name": name, "enabled": _FEATURES[name]}


@router.put("/{name}", response_model=FeatureFlag)
def set_feature(name: str, payload: FeatureFlag):
    # keep URL and body consistent
    if payload.name != name:
        raise HTTPException(status_code=400, detail="name_mismatch")
    _FEATURES[name] = payload.enabled
    return payload
