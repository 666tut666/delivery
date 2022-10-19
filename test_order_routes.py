import pytest
from httpx import AsyncClient
from main import app
from fastapi.testclient import TestClient




client = TestClient(app)
@pytest.mark.anyio
async def test_hello():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/orders")
    assert response.status_code == 200
    assert response.json() == {"message":"hello"}


