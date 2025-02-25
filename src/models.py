import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    seguidores = Column(Integer, nullable=False)                   
    posts = Column(Integer, nullable=False)

class Publicacion(Base):
    __tablename__ = 'publicacion'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, nullable=False)
    descripcion = Column(String(250), nullable=False)                   
    likes= Column(Integer, nullable=False)
    url_imagen= Column(String(250), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)



class Comentarios(Base):
    __tablename__ = 'comentarios'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_usuario= Column(Integer)
    id_publicacion = Column(Integer)
    comentarios = Column(String(250), nullable=False)
    publicacion_id = Column(Integer, ForeignKey('publicacion.id'))
    publicacion = relationship(Publicacion)

class Seguidores(Base):
    __tablename__ = 'seguidores'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)
    id_seguir= Column(Integer)

    
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
