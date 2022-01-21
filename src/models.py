from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, create_engine


# Create the session maker which will generate a context manager for us
session_maker = sessionmaker(bind=create_engine('sqlite:///database.sqlite3'))


# Main class to wrap all the classes
Base = declarative_base()


class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
