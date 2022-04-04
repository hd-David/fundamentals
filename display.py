from app import User, Address, dbconnect
from sqlalchemy import create_engine, insert, update, delete, select

session = dbconnect()
stmt = select(User).where(User.name.in_(["spongebob", "sandy", "patrick"]))

for user in session.scalars(stmt):
    print(user)