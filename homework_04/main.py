"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from homework_04.jsonplaceholder_requests import fetch_users, fetch_posts
from homework_04.models import Engine, Base, User, Post, Session


async def create_tables():
    async with Engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_users(session: AsyncSession, a):
    a = await fetch_users()
    for obj in a:
        user = User(name=obj.get('name'), username=obj.get('username'), email=obj.get('email'))
        session.add(user)
    await session.commit()


async def create_posts(session: AsyncSession, a):
    a = await fetch_posts()
    for obj in a:
        post = Post(title=obj.get('title'), body=obj.get('body'), user_id=obj.get('userId'))
        session.add(post)
    await session.commit()


async def async_main():
    users, posts = await asyncio.gather(fetch_users(), fetch_posts())
    async with Session() as session:
        await create_tables()
        await create_users(session, users)
        await create_posts(session, posts)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
