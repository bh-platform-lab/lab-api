from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_hello_default():
    r = client.get("/api/v1/hello")
    assert r.status_code == 200
    assert r.json() == {"message": "hello, world"}


def test_hello_with_name():
    r = client.get("/api/v1/hello", params={"name": "Brahim"})
    assert r.status_code == 200
    assert r.json() == {"message": "hello, Brahim"}
