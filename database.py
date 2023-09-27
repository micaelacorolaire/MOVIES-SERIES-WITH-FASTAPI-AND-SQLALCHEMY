from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector

# Configuración de la base de datos MySQL
db_config = {
    'user': 'root',                  # Tu nombre de usuario de MySQL
    'password': 'micaelacorolaire',  # Tu contraseña de MySQL
    'host': 'localhost',             # El host de tu servidor MySQL
    'database': 'moviesandseries'    # El nombre de tu base de datos MySQL
}

# Crea una conexión a la base de datos MySQL utilizando mysql.connector
conn = mysql.connector.connect(**db_config)

# URL de conexión para SQLAlchemy
DATABASE_URL = "mysql+mysqlconnector://root:micaelacorolaire@localhost/moviesandseries"

# Crea el motor SQLAlchemy y la sesión
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BaseModel = declarative_base()




