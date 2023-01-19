"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json():
    async with aiohttp.ClientSession() as session:
        users = await session.get(USERS_DATA_URL)
        posts = await session.get(POSTS_DATA_URL)
    print('users = ', await users.json(), '/n posts = ', await posts.json())
    return users, posts


asyncio.run(fetch_json())
