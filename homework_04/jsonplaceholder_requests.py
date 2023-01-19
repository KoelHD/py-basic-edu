"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_users():
    async with aiohttp.ClientSession() as session:
        users = await session.get(USERS_DATA_URL)
    return users.json()


async def fetch_posts():
    async with aiohttp.ClientSession() as session:
        posts = await session.get(POSTS_DATA_URL)
    return posts.json()
