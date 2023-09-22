from sqlalchemy import Table, create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Crear la instancia de SQLAlchemy
engine = create_engine('sqlite:///mydatabase.db', echo=True)
Base = declarative_base()

# Definir la tabla intermedia
user_group_association = Table('user_group_association', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('group_id', Integer, ForeignKey('groups.id'))
)

# Definir el modelo User
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    groups = relationship("Group", secondary=user_group_association, back_populates="users")

# Definir el modelo Group
class Group(Base):
    __tablename__ = 'groups'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    users = relationship("User", secondary=user_group_association, back_populates="groups")

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión de SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# Crear instancias de User y Group
user1 = User(name="Usuario 1")
user2 = User(name="Usuario 2")
group1 = Group(name="Grupo 1")
group2 = Group(name="Grupo 2")

# Establecer la relación ManyToMany
user1.groups.append(group1)
user1.groups.append(group2)
user2.groups.append(group1)

# Agregar las instancias a la sesión y confirmar la transacción
session.add_all([user1, user2, group1, group2])
session.commit()

# Consultar la relación
user = session.query(User).filter_by(name="Usuario 1").first()
print("Grupos del Usuario 1:", [group.name for group in user.groups])

group = session.query(Group).filter_by(name="Grupo 1").first()
print("Usuarios en el Grupo 1:", [user.name for user in group.users])

# Cerrar la sesión
session.close()
