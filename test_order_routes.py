import pytest
from main import app
from httpx import AsyncClient


@pytest.mark.anyio
async def test_hello():
    async with AsyncClient(app=app, base_url="http://test/orders") as ac:
        response = await ac.get('/orders')
    assert response.status_code == 200
    assert response.json() == {"message":"order"}
