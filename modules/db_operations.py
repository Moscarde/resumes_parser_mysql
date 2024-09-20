from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Classe que define a tabela 'resumes'
class Resume(Base):
    __tablename__ = 'resumes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_text = Column(Text, nullable=False)
    url = Column(String(255), nullable=False)

def create_db_session(db_type):
    if db_type == "mysql":
        engine = create_engine('mysql+mysqlconnector://usertest:Senha123!@localhost/tech_recruiter')
    elif db_type == "sqlite":
        engine = create_engine('sqlite:///tech_recruiter.db')
    else:
        raise ValueError("Tipo de banco de dados inválido. Use 'mysql' ou 'sqlite'.")

    Session = sessionmaker(bind=engine)
    return Session(), engine

def create_table(engine):
    Base.metadata.create_all(engine)

def url_exists(session, url):
    return session.query(Resume).filter(Resume.url == url).count() > 0

def add_resume(session, full_text, url):
    new_resume = Resume(full_text=full_text, url=url)
    session.add(new_resume)
