from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import declarative_base
import psycopg2
import os

user= os.environ.get('user', 'root')
passw = os.environ.get('passwd', 'admin')
host= os.environ.get('host', 'localhost')
port = os.environ.get('port', '5432')
db = os.environ.get('dbs', 'test')


engine = create_engine(f'postgresql://{user}:{passw}@{host}:{port}/{db}')
db_session = scoped_session(sessionmaker(engine))

Database = declarative_base()

