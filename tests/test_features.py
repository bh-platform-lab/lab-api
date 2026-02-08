from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_features():
    r = client.get("/api/v1/features")
    assert r.status_code == 200
    data = r.json()
    assert "dark_mode" in data
    assert isinstance(data["dark_mode"], bool)


def test_get_feature_ok():
    r = client.get("/api/v1/features/dark_mode")
    assert r.status_code == 200
    assert r.json()["name"] == "dark_mode"


def test_get_feature_404():
    r = client.get("/api/v1/features/does_not_exist")
    assert r.status_code == 404
    assert r.json()["detail"] == "feature_not_found"


def test_put_feature_ok():
    r = client.put("/api/v1/features/dark_mode", json={"name": "dark_mode", "enabled": True})
    assert r.status_code == 200
    assert r.json() == {"name": "dark_mode", "enabled": True}


def test_put_feature_name_mismatch():
    r = client.put("/api/v1/features/dark_mode", json={"name": "other", "enabled": True})
    assert r.status_code == 400
    assert r.json()["detail"] == "name_mismatch"
