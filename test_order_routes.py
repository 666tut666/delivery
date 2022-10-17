import pytest
from main import app
from httpx import AsyncClient


@pytest.mark.anyio
async def test_hello():
    async with AsyncClient(app=app, base_url="/orders") as ac:
        response = await ac.get('/')
    assert response.status_code == 200
    assert response.json() == {"message":"order"}
