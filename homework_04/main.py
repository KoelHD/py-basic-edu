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
from homework_04.models import engine, Base, User, Post, Session


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_users(session):
    a = await fetch_users()
    for usr in a:
        user = User(name=usr.get('name'), username=usr.get('username'), email=usr.get('email'))
        session.add(user)
    await session.commit()


async def create_posts(session):
    b = await fetch_posts()
    for post in b:
        pst = Post(title=post.get('title'), body=post.get('body'), user_id=post.get('userId'))
        session.add(pst)
    await session.commit()


async def async_main():
    await create_tables()
    await asyncio.gather(create_users(Session), create_posts(Session))


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
