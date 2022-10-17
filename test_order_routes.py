import pytest
from main import app
from httpx import AsyncClient


@pytest.mark.anyio
async def test_hello(self):
    async with AsyncClient(app=app, base_url="http://test/orders"):
        response = self.client.get('/orders')
    assert response.status_code == 200
    assert response.json() == {"message":"order"}
