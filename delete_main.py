from typing import Optional

from conf.db_session import create_session

from models.revendedor import Revendedor
from models.picole import Picole


def deletar_picole(id_picole: int) -> None:
    with create_session() as session:
        picole: Optional[Picole] = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

        if picole:
            session.delete(picole)
            session.commit()
        else:
            print(f'Não encontrei picole com id {id_picole}')


def deletar_revendedor(id_revendedor: int) -> None:
    with create_session() as session:
        revendedor: Optional[Revendedor] = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()

        if revendedor:
            session.delete(revendedor)
            session.commit()
        else:
            print(f'Não encontrei nenhum revendedor com id {id_revendedor}')


def select_filtro_revendedor(id_revendedor: int) -> None:
    with create_session() as session:
        revendedor: Optional[Revendedor] = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none() 

        if revendedor:
            print(f'ID: {revendedor.id}')
            print(f'Razão Social: {revendedor.razao_social}')
        else:
            print(f'Não encontrei nenhum revendedor com id {id_revendedor}')



if __name__ == '__main__':
    from update_main import select_filtro_picole

    # id_picole = 21

    # # antes
    # select_filtro_picole(id_picole=id_picole)

    # # Deletar
    # deletar_picole(id_picole=id_picole)

    # # Depois
    # select_filtro_picole(id_picole=id_picole)

    
    id_revendedor_nv = 2
    id_revendedor_v = 5

     # antes
    select_filtro_revendedor(id_revendedor=id_revendedor_v)

    # Deletar
    deletar_revendedor(id_revendedor=id_revendedor_v)

    # Depois
    select_filtro_revendedor(id_revendedor=id_revendedor_v)



