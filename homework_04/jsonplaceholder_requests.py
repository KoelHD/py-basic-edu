"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio

import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_users():
    async with aiohttp.ClientSession() as session:
        response = await session.get(USERS_DATA_URL)
        data = await response.json()
        users = data.get('name', 'username', 'email')
    return users


async def fetch_posts():
    async with aiohttp.ClientSession() as session:
        posts = await session.get(POSTS_DATA_URL)
    return posts.json()

