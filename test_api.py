import pytest
from httpx import AsyncClient
from random import randint

from main import app, posts_db

baseUrl = "http://localhost:8000/"

@pytest.mark.anyio
async def test_root():
    async with AsyncClient(app=app, base_url=baseUrl) as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}

@pytest.mark.anyio
async def test_posts_get():
    async with AsyncClient(app=app, base_url=baseUrl) as ac:
        response = await ac.get("/posts/")
    assert response.status_code == 200
    assert response.json() == posts_db

@pytest.mark.anyio
async def test_posts_id():
    num = randint(1, len(posts_db))
    async with AsyncClient(app=app, base_url=baseUrl) as ac:
        response = await ac.get(f"/posts/get/{num}/")
    assert response.status_code == 200
    assert response.json() == posts_db[num-1]