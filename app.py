from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
username='root'
password='2215a2216k'
database='pixie_db'
database=f"mysql+mysqldb://{username}:{password}@localhost/{database}"
engine=create_engine(database)
session=sessionmaker(bind=engine)
session=session()