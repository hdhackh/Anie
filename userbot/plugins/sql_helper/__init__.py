import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# the secret configuration specific things
from var import Var

DB_URI = "postgres://bxvcsmczwdafcq:4e34203d52388a9494e1bb6bd1fb97dcff20fe8ef9872ca47a894d099380fa45@ec2-54-164-241-193.compute-1.amazonaws.com:5432/d91t9oe2tcqppn"


def start() -> scoped_session:
    engine = create_engine(DB_URI)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    # this is a dirty way for the work-around required for #23
    print(
        "DB_URI is not configured. Features depending on the database might have issues."
    )
    print(str(e))
