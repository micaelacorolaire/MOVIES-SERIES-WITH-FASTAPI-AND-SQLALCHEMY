from sqlalchemy import Column, Integer, String,Date
from database import BaseModel

class series(BaseModel):
    __tablename__='series'
    __args__={'schema':'public'}
    id_series=Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    title=Column(String,nullable=False)
    serie_director=Column(String,nullable=False)
    actors=Column(String,nullable=False)
    kind_of_serie=Column(String,nullable=False)
    qualification=Column(Integer,nullable=False)
    seasons=Column(Integer,nullable=False)
    episodes=Column(Integer,nullable=False)
    release_year=Column(Date,nullable=False)
class movies(BaseModel):
    __tablename__='movies'
    __args__={'schema':'public'}
    id_movies=Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    title=Column(String,nullable=False)
    movies_director=Column(String,nullable=False)
    actors=Column(String,nullable=False)
    kind_of_movies=Column(String,nullable=False)
    qualification=Column(Integer,nullable=False)
    release_year=Column(Date,nullable=False)
    
    