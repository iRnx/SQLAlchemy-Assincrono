import asyncio

from typing import List

from sqlalchemy import func # Funções de agregação
from sqlalchemy.future import select

from conf.helpers import formata_data
from conf.db_session import create_session

# Select Simples
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.revendedor import Revendedor

# Select Compostos/Complexos
from models.picole import Picole

# Select simples -> SELECT * FROM aditivos_nutritivos;
async def select_todos_aditivos_nutritivos() -> None:

    async with create_session() as session:

        # query = select(AditivoNutritivo)
        # aditivos_nutritivos: List[AditivoNutritivo] = await session.execute(query)
        # aditivos_nutritivos = aditivos_nutritivos.scalars().all()

        aditivos_nutritivos: List[AditivoNutritivo] = (await session.execute(select(AditivoNutritivo))).scalars().all()

        for an in aditivos_nutritivos:
            print(f'ID: {an.id}')
            print(f'Data: {an.data_criacao}')
            print(f'Nome: {an.nome}')
            print(f'Formula Quimica: {an.formula_quimica}')
            print('=-=' * 15)


# Filtrando dados
async def select_filtro_sabor(id_sabor: int) -> None:
    async with create_session() as session:
        
        query = select(Sabor).filter(Sabor.id == id_sabor) # query = select(Sabor).where(Sabor.id == id_sabor)

        resultado = await session.execute(query)

        # Forma 1 # Retorna None caso não encontre
        # sabor: Sabor = resultado.scalars().first()

        # Forma 2 # Retorna None caso não encontre
        # sabor: Sabor = resultado.scalars().one_or_none()

        # Forma 3 # exec.NoResultFound caso não encontre
        # sabor: Sabor = resultado.scalars().one()

        # # Forma 4 # None caso não encontre
        sabor: Sabor = resultado.scalar_one_or_none() # Recomendado
        

        print(f'ID: {sabor.id}')
        print(f'Data: {formata_data(sabor.data_criacao)}')
        print(f'Nome: {sabor.nome}')
        print('=-=' * 15)


async def select_complexo_picole() -> None:
    async with create_session() as session:
        
        query = select(Picole)
        resultado = await session.execute(query)
        picoles: List[Picole] = resultado.scalars().unique().all()

        for picole in picoles:
            print(f'ID: {picole.id}')
            print(f'Data: {formata_data(picole.data_criacao)}')
            print(f'Preço: {picole.preco}')

            print(f'ID Sabor: {picole.id_sabor}')
            print(f'Sabor: {picole.sabor.nome}')

            print(f'ID Embalagem: {picole.id_tipo_embalagem}')
            print(f'Embalagem: {picole.tipo_embalagem.nome}')

            print(f'ID Tipo Picole: {picole.id_tipo_picole}')
            print(f'Tipo Picole: {picole.tipo_picole.nome}')

            print(f'Ingredientes: {picole.ingredientes}')
            print(f'Aditivos Nutritivos: {picole.aditivos_nutritivos}')
            print(f'Conservantes: {picole.conservantes}')

            print('=-=' * 15)


async def select_order_by_sabor() -> None:
    async with create_session() as session:

        query = select(Sabor).order_by(Sabor.data_criacao.desc())
        resultado = await session.execute(query)
        sabores: Sabor = resultado.scalars().all()

        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f'Nome: {sabor.nome}')
            print('=-=' * 15)


# Agrupamento de dados, group_by()
async def select_group_by_picole() -> None:
    async with create_session() as session:

        query = select(Picole).group_by(Picole.id, Picole.id_tipo_picole)
        resultado = await session.execute(query)
        picoles: List[Picole] = resultado.scalars().unique().all() 

        for picole in picoles:
            print(f'ID: {picole.id}')
            print(f'Tipo Picole: {picole.tipo_picole.nome}')
            print(f'Sabor: {picole.sabor.nome}')
            print(f'Preço: {picole.preco}')
            print('=-=' * 15)


# Limitando quantidade de dados
async def select_limit() -> None:
    async with create_session() as session:
        query = select(Sabor).limit(25)
        resultado = await session.execute(query)
        sabores: List[Sabor] = resultado.scalars()
    
        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f'Sabor: {sabor.nome}')
            print('=-=' * 15)


# count()
async def select_count_revendedor() -> None:
    async with create_session() as session:
        query = select(func.count(Revendedor.id))
        resultado = await session.execute(query)
        qtd: int = resultado.scalar()
        print(f'Quantidade de revendedores: {qtd}')


async def select_agregacao() -> None:
    async with create_session() as session:
        query = select(
            func.sum(Picole.preco).label('Soma'),
            func.avg(Picole.preco).label('Media'),
            func.min(Picole.preco).label('Minimo'),
            func.max(Picole.preco).label('Maximo'),
        )
        resultado = await session.execute(query)
        resultado = resultado.all()

        print(f'A soma de todos os picoles é: {resultado[0][0]}')
        print(f'A Média de todos os picoles é: {resultado[0][1]}')
        print(f'Picolé mais barato: {resultado[0][2]}')
        print(f'Picolé mais caro: {resultado[0][3]}')


if __name__ == '__main__':
    # asyncio.run(select_todos_aditivos_nutritivos())
    asyncio.run(select_filtro_sabor(95))
    # asyncio.run(select_complexo_picole())
    # asyncio.run(select_order_by_sabor())
    # asyncio.run(select_group_by_picole())
    # asyncio.run(select_limit())
    # asyncio.run(select_count_revendedor())
    # asyncio.run(select_agregacao())