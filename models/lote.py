from typing import List
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.orm import Mapped
from datetime import datetime

from models.model_base import ModelBase
from models.tipo_picole import TipoPicole

class Lote(ModelBase):
    __tablename__: str = 'lotes'
    
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    quantidade: int = sa.Column(sa.Integer, nullable=False)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    id_tipo_picole: int = sa.Column(sa.Integer, sa.ForeignKey('tipos_picole.id')) # tabela.campo #
    tipo_picole: Mapped[TipoPicole] = orm.relationship('TipoPicole', lazy='joined') # Conf interna so SQL Alchemy #

    def __repr__(self) -> int:
        return f'<Lote: {self.id}>'