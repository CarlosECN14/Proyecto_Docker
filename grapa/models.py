from database import Database

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String



class Peliculas(Database):
    __tablename__ = 'peliculas'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    descripcion = Column(String(250))
    imagen = Column(String(100))

