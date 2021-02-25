import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# the secret configuration specific things
from var import Var

DB_URI = "postgres://fpcjlwlbvvetuj:40f669c5566855d9c7ac10a79814fcc35d2e04e0026503f07158f766ab42537b@ec2-54-144-251-233.compute-1.amazonaws.com:5432/d2hl9k01vg99sr"


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
