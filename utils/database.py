from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql+pymysql://root:123456@localhost:3307/Chatbot')


class dtb:
    metadata = MetaData()
    my_table = Table('user3', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('username', String(20)),
                     Column('password', String(20)),
                     Column('balance', Integer, default=0)
                     )
    # create table

    def Create_Table(self):
        self.metadata.create_all(engine)

    # insert_user_into_table
    def insert_user(self, usn, passw):
        conn = engine.connect()
        conn.execute(self.my_table.insert().values(
            username=usn, password=passw))
        conn.commit()

    # query data
    def query_data(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        result = session.query(self.my_table).all()
        return result

    def update_data(self, usn, money, bal):
        money = int(bal) + int(money)
        print(">>>", money)
        print(">>>>", usn)

    # Create an update statement that increases the salary by 1000 for rows where age > 30
        conn = engine.connect()
        stmt = (
            update(self.my_table)
            .where(self.my_table.c.username == usn)
            .values(balance=money)
        )
        with engine.connect() as conn:
            conn.execute(stmt)


database = dtb()
