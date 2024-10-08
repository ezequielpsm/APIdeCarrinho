from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

#configurações
engine = create_engine('mysql+mysqlconnector://root:731015@localhost:3306/cinema')
# conn  = engine.connect()
# response = conn.execute(text('SELECT * FROM filmes;'))
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# #entidades

class Filmes(Base):
    __tablename__ = "filmes"

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Filme [titulo={self.titulo}, ano={self.ano}]"


# #SQL

# #Insert
data_insert = Filmes(titulo="adada", genero="Ação", ano=2022)
session.add(data_insert)
session.commit()

# #delete
session.query(Filmes).filter(Filmes.titulo=="Batman").delete()
session.commit()

#Update
session.query(Filmes).filter(Filmes.genero == "Drama").update({"ano": 2000})
session.commit()

#Select
data = session.query(Filmes).all()
print(data)
print(data[0].titulo)

session.close()