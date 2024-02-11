from sqlalchemy import create_engine, MetaData, Table

from sqlalchemy.orm import sessionmaker



engine = create_engine("sqlite:///books.db")

conn = engine.connect()

metadata = MetaData()

book = Table("book", metadata, autoload=True, autoload_with=engine)



Session = sessionmaker(bind=engine)

session = Session()



query = session.query(book.columns.title).order_by(book.columns.title)



for title in query:

    print(title)



session.close()

