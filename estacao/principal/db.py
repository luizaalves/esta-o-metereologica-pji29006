#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from settings import SQLALCHEMY_DATABASE_URI as DB_URI

Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=create_engine(DB_URI,connect_args={'check_same_thread':False}))
session = scoped_session(Session)