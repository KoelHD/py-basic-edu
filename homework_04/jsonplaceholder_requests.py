"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_users():
    async with aiohttp.ClientSession() as session:
        response = await session.get(USERS_DATA_URL)
        users_list = await response.json()
        print(users_list)
    return users_list


async def fetch_posts():
    async with aiohttp.ClientSession() as session:
        response = await session.get(POSTS_DATA_URL)
        posts_list = await response.json()
    return posts_list
