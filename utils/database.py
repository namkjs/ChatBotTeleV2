from sqlalchemy import *
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql+pymysql://root:123456@localhost:3307/Chatbot')


class dtb:
    metadata = MetaData()
    my_table = Table('user3', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('username', String(20)),
                     Column('password', String(255)),
                     Column('balance', Integer, default=0),
                     Column('salt', String(256)),
                     Column('score', Integer, default=0),
                     Column('Language', Integer, default=0)
                     )
    # create table

    def Create_Table(self):
        self.metadata.create_all(engine)

    # insert_user_into_table
    def insert_user(self, usn, passw, salt):
        print("Check salt: ", salt)
        conn = engine.connect()
        conn.execute(self.my_table.insert().values(
            username=usn, password=passw, salt=salt))
        conn.commit()

    # query data
    def query_data(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        result = session.query(self.my_table).all()
        return result

    def query_balance_data(self, usn):
        Session = sessionmaker(bind=engine)
        session = Session()
        result = session.query(self.my_table).filter_by(username=usn).first()
        return result

    def query_language_data(self, usn):
        Session = sessionmaker(bind=engine)
        session = Session()
        result = session.query(self.my_table).filter_by(username=usn).first()
        return result[6]

    def update_data(self, usn, money, bal):
        print(">> check balance truoc", bal)
        money = int(bal) + int(money)
        print(">> check money", money)
    # Create an update statement that increases the salary by 1000 for rows where age > 30
        conn = engine.connect()
        stmt = (
            update(self.my_table)
            .where(self.my_table.c.username == usn)
            .values(balance=money)
        )
        conn.execute(stmt)
        conn.commit()

    def update_pass(self, usn, passw):
        conn = engine.connect()
        stmt = (
            update(self.my_table)
            .where(self.my_table.c.username == usn)
            .values(password=passw)
        )
        conn.execute(stmt)
        conn.commit()

    def update_lan(self, usn, lan):
        conn = engine.connect()
        stmt = (
            update(self.my_table)
            .where(self.my_table.c.username == usn)
            .values(Language=lan)
        )
        conn.execute(stmt)
        conn.commit()

    def send(self, usn, rcv, usn_money, money):
        temp = -int(money)
        print("Check money", money)
        self.update_data(usn, temp, usn_money)

        results = self.query_data()
        for result in results:
            if rcv == result[1]:
                rcv_money = int(result[3])
                break
        self.update_data(rcv, money, rcv_money)


database = dtb()
database.Create_Table()
