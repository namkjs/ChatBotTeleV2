from sqlalchemy import *
from passlib.hash import bcrypt
from sqlalchemy.orm import sessionmaker
engine = create_engine(
    'mysql://bb786fcaa29898:931ea44f@us-cdbr-east-06.cleardb.net/heroku_a5cf45e366fd580?reconnect=true')


class dtb1:

    def __init__(self, username):
        self.usern = str(username)
        self.metadata = MetaData()
        self.my_table = Table(f'{self.usern}', self.metadata,
                              Column('id', Integer, primary_key=True),
                              Column('Hash', String(256)),
                              )

    def create_table(self):
        self.metadata.create_all(engine)
    # create table

    def insert_user(self, trans):
        print(">>> check in transaction: ", trans)
        conn = engine.connect()
        conn.execute(self.my_table.insert().values(
            Hash=trans))
        conn.commit()

    def query_data(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        results = session.query(self.my_table).all()
        return results
