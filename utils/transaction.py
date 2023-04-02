from sqlalchemy import *
from passlib.hash import bcrypt
from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql+pymysql://root:123456@localhost:3307/Chatbot')


class dtb1:

    def __init__(self, username):
        self.usern = str(username)
        self.metadata = MetaData()
        self.my_table = Table(f'{self.usern}', self.metadata,
                              Column('id', Integer, primary_key=True),
                              Column('Day', String(256)),
                              Column('Time', String(256)),
                              Column('Money', String(256)),
                              Column('From', String(256))
                              )

    def create_table(self):
        self.metadata.create_all(engine)
    # create table

    def insert_user(self, day, time, money, fr):
        print(">>> check in transaction: ", day,
              "-", time, "-", money, "-", fr)
        conn = engine.connect()
        conn.execute(self.my_table.insert().values(
            Day=day, Time=time, Money=money, From=fr))
        conn.commit()

    def query_data(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        results = session.query(self.my_table).all()
        return results
