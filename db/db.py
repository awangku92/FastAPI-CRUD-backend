import sys, os 

# Bring packages onto the path
sys.path.append(os.path.abspath('..'))
import config as conf

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# CONNECTION TO DB
#'dialect+driver://username:password@host:port/database'
conn_string = 'sqlite://'+conf.DB['URL']
engine = create_engine(conn_string, echo=True, pool_pre_ping=True)
Session = sessionmaker(bind=engine,expire_on_commit=False)
s = Session()

# FOR DB
Base = declarative_base()