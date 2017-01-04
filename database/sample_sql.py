from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

engine = create_engine('mysql://root:password@localhost:5432/testdb')
#connection = engine.connect()
#result = connection.execute("select * from numbers")

from sqlalchemy import Column, String, Integer, ForeignKey
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(10))


# Construct a sessionmaker object
session = sessionmaker()
# Bind the sessionmaker to engine
session.configure(bind=engine)
# Create all the tables in the database which are
# defined by Base's subclasses such as User
Base.metadata.create_all(engine)

# Make a new Session object
s = session()
john = User(name='John')
 
# Add User john to the Session object
s.add(john)
 
# Commit the new User John to the database
s.commit()

