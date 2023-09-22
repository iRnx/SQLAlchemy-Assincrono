import asyncio

from conf.db_session import create_session

# Insert parte 1
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor

# Inserte parte 2
from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole

from typing import List


async def insert_aditivo_nutritivo() -> AditivoNutritivo:
    print('Cadastrando Aditivo Nutritivo')

    nome : str = input('Informe o nome do Aditivo Nutritivo: ')
    formula_quimica: str = input('Informe a fórmula química do aditivo: ')

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    async with create_session() as session:
        # session = create_session()
        session.add(an)
        await session.commit()
        await session.refresh(an)

        # print('Aditivo Nutritivo cadastrado com sucesso')
        # print(f'ID: {an.id}')
        # print(f'Nome: {an.nome}')
        # print(f'Formula Química: {an.formula_quimica}')
        # print(f'Data Criação: {an.data_criacao}')

        return an
        
    

async def insert_sabor() -> None:
    print('Cadastrando Sabor')

    nome: str = input('Informe o Sabor: ')

    sabor: Sabor = Sabor(nome=nome)

    async with create_session() as session:
        session.add(sabor)
        await session.commit()
        await session.refresh(sabor)

        print('Sabor cadastrado com sucesso')
        print(f'ID: {sabor.id}')
        print(f'Nome: {sabor.nome}')
        print(f'Data Criação: {sabor.data_criacao}')


async def insert_tipos_embalagem() -> None:
    print('Cadastre os tipos de embalagem')

    nome: str = input('Cadastre o nome da embalagem: ')
    nome_embalagem: TipoEmbalagem = TipoEmbalagem(nome=nome)


    async with create_session() as session:
        session.add(nome_embalagem)
        await session.commit()
        await session.refresh(nome_embalagem)

        print('Tipo de embalagem cadastrado com sucesso')
        print(f'ID: {nome_embalagem.id}')
        print(f'Nome: {nome_embalagem.nome}')
        print(f'Data Criação: {nome_embalagem.data_criacao}')
    

async def insert_tipos_picole() -> None:
    print('Cadastre tipos de picolé')

    nome: str = input('Cadastre o tipo de picolé: ')
    tipos_picole: TipoPicole = TipoPicole(nome=nome) 

    async with create_session() as session:
        session.add(tipos_picole)
        await session.commit()
        await session.refresh(tipos_picole)


        print('Tipo de picolé cadastrado com sucesso')
        print(f'ID: {tipos_picole.id}')
        print(f'Nome: {tipos_picole.nome}')
        print(f'Data Criação: {tipos_picole.data_criacao}')


async def insert_ingrediente() -> Ingrediente:
    print('Cadastre os ingredientes')

    nome: str = input('Cadastre os ingredientes: ') 
    ingrediente: Ingrediente = Ingrediente(nome=nome)

    async with create_session() as session:
        session.add(ingrediente)
        await session.commit()
        await session.refresh(ingrediente)

        return ingrediente
    
        # print('Ingrediente cadastrado com sucesso')
        # print(f'ID: {ingrediente.id}')
        # print(f'Nome: {ingrediente.nome}')
        # print(f'Data Criação: {ingrediente.data_criacao}')


async def insert_conservante() -> Conservante:

    nome: str = input('Cadastre o nome do conservante: ')
    descricao: str = input('Cadastre a descrição do conservante: ')

    conservante: Conservante = Conservante(nome=nome, descricao=descricao)
    
    async with create_session() as session:
        session.add(conservante)
        await session.commit()
        await session.refresh(conservante)

        return conservante

        # print(f'ID: {conservante.id}')
        # print(f'Nome: {conservante.nome}')
        # print(f'Conservante: {conservante.descricao}')
        # print(f'Data Criação: {conservante.data_criacao}')


async def insert_revendedor() -> Revendedor:
    print('Cadastre Revendedor')

    cnpj: str = input('Informe o CNPJ do revendedor: ')
    razao_social: str = input('Informe a razão social do reendedor: ')
    contato: str = input('Informe o contato do revendedor: ')

    revendedor: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)
    
    async with create_session() as session:
        session.add(revendedor)
        await session.commit()
        await session.refresh(revendedor)

        return revendedor
    

async def insert_lote() -> Lote:
    print('Cadastre Lote')

    id_tipo_picole: int = int(input('Informe o id do tipo do picole: '))
    quantidade: int = int(input('Informe a Quantidade de picolé: '))

    lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)
    
    async with create_session() as session:
        session.add(lote)
        await session.commit()
        await session.refresh(lote)

        return lote


# Foreinkey e manytomany
async def insert_nota_fiscal() -> None:
    print('Cadastre Nota Fiscal')

    valor: float = float(input('Informe o valor da nota fiscal: '))
    numero_serie: str = input('Informe o número de série: ')
    descricao: str = input('Informe a descrição: ')
    id_revendedor: int = int(input('Informe o ID do revendedor: '))

    nf: NotaFiscal = NotaFiscal(valor=valor, numero_serie=numero_serie, descricao=descricao, id_revendedor=id_revendedor)

    lote1 = await insert_lote()
    nf.lotes.append(lote1)

    lote2 = await insert_lote()
    nf.lotes.append(lote2)
    
    async with create_session() as session:
        session.add(nf)
        await session.commit()
        await session.refresh(nf)

        print('Nota fiscal cadastrada com sucesso')
        print(f'ID: {nf.id}')
        print(f'Data: {nf.data_criacao}')
        print(f'Valor: {nf.valor}')
        print(f'Número de serie: {nf.numero_serie}')
        print(f'Descrição: {nf.descricao}')
        print(f'ID Revendedor: {nf.id_revendedor}')
        print(f'Revendedor razao social: {nf.revendedor.razao_social}')
   

# Foreinkey e manytomany
async def insert_picole() -> None:
    print('Cadastrando Picole')

    preco: float = float(input('Informe o preço do picole: '))
    id_sabor: int = int(input('Informe o ID do sabor: '))
    id_tipo_picole: int = int(input('Informe o ID do tipo de picole: '))
    id_tipo_embalagem: int = int(input('Informe o ID do tipo de embalagem: '))


    picole: Picole = Picole(id_sabor=id_sabor, id_tipo_picole=id_tipo_picole, id_tipo_embalagem=id_tipo_embalagem, preco=preco)

    ingrediente1 = await insert_ingrediente()
    picole.ingredientes.append(ingrediente1)

    ingrediente2 = await insert_ingrediente()
    picole.ingredientes.append(ingrediente2)

    # Tem conservante?
    conservante = await insert_conservante()
    picole.conservantes.append(conservante)

    # Tem Aditivos Nutritivos?
    aditivo_nutritivo = await insert_aditivo_nutritivo()
    picole.aditivos_nutritivos.append(aditivo_nutritivo)

    async with create_session() as session:
        session.add(picole)
        await session.commit()
        await session.refresh(picole)

        print('Picolé cadastrado com sucesso')
        print(f'ID: {picole.id}')
        print(f'Data: {picole.data_criacao}')
        print(f'Preço: {picole.preco}')
        print(f'Sabor: {picole.sabor.nome}') # Foreinkey
        print(f'Tipo Picole: {picole.tipo_picole.nome}') # Foreinkey
        print(f'Tipo Embalagem: {picole.tipo_embalagem.nome}') # Foreinkey
        print(f'Ingredientes: {picole.ingredientes}') # manytomany
        print(f'Conservantes: {picole.conservantes}') # manytomany
        print(f'Aditivos Nutritivos: {picole.aditivos_nutritivos}') # manytomany




if __name__ == '__main__':
    # an = asyncio.run(insert_aditivo_nutritivo())
    # print('Aditivo Nutritivo cadastrado com sucesso')
    # print(f'ID: {an.id}')
    # print(f'Nome: {an.nome}')
    # print(f'Formula Química: {an.formula_quimica}')
    # print(f'Data Criação: {an.data_criacao}')

    # asyncio.run(insert_sabor())

    # asyncio.run(insert_tipos_embalagem())

    # ingrediente = asyncio.run(insert_ingrediente())

    # print(f'ID: {ingrediente.id}')
    # print(f'Nome: {ingrediente.nome}')
    # print(f'Data Criação: {ingrediente.data_criacao}')

    # conservante = asyncio.run(insert_conservante())

    # print(f'ID: {conservante.id}')
    # print(f'Nome: {conservante.nome}')
    # print(f'Conservante: {conservante.descricao}')
    # print(f'Data Criação: {conservante.data_criacao}')

    # insert_tipos_picole()

    # rev = asyncio.run(insert_revendedor())
    # print('Conservante cadastrado com sucesso')
    # print(f'ID: {rev.id}')
    # print(f'CNPJ: {rev.cnpj}')
    # print(f'Contato: {rev.contato}')
    # print(f'Data Criação: {rev.data_criacao}')

    
    # lote = asyncio.run(insert_lote())
    # print('Lote cadastrado com sucesso')
    # print(f'ID: {lote.id}')
    # print(f'Quantidade: {lote.quantidade}')
    # print(f'ID Tipo Picole: {lote.id_tipo_picole}')
    # print(f'Data Criação: {lote.data_criacao}')

    # asyncio.run(insert_nota_fiscal())

    asyncio.run(insert_picole())
