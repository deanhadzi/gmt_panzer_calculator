from sqlalchemy import create_engine
from sqlalchemy.orm import (
    as_declarative,
    declared_attr,
    sessionmaker
)

SQLALCHEMY_URI = "postgresql://localhost/postgres"

engine = create_engine(SQLALCHEMY_URI, echo=True, future=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@as_declarative()
class Base(object):
    """Declarative Base with table name and repr."""

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def __repr__(self):
        args_dict = {k: v for k, v in vars(self).items() if k[0] != "_"}
        values = ", ".join("{}={!r}".format(k, v) for k, v in args_dict.items())
        return f"{type(self).__name__}({values})"

