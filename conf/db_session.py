from typing import Optional

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine

from models.model_base import ModelBase


__async_engine: Optional[AsyncEngine] = None


def criar_engine() -> AsyncEngine:
    """
    Função para configurar a conexão ao banco de dados
    """

    global __async_engine

    if __async_engine:
        return

    conn: str =  f'postgresql+asyncpg://renan:1533@localhost:5432/picoles'
    __async_engine = create_async_engine(url=conn, echo=False)

    return __async_engine


def create_session() -> AsyncSession:
    """
    Função para criar a sessão de conexão ao banco de dados
    """
    
    global __async_engine

    if not __async_engine:
        criar_engine()

    __async_session = sessionmaker(bind=__async_engine, expire_on_commit=False, class_=AsyncSession)
    session: AsyncSession = __async_session()

    return session



async def create_tables() -> None:
    global __async_engine

    if not __async_engine:
        criar_engine()
    
    import models.__all_models
    async with __async_engine.begin() as conn:
        await conn.run_sync(ModelBase.metadata.drop_all)
        await conn.run_sync(ModelBase.metadata.create_all)





