from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Numeric,Float
Base=declarative_base()
class brand_tbl (Base):
    __tablename__='brand_tbl'
    isbn_no=Column(Integer,primarykey=True,autoincrement=True,nullable=False)
    brand_name=Column(String(100),nullable=False)
    specification=Column(String(100),nullable=False)
    type=Column(String(100),nullable=False)
    price=Column(Float,nullable=False)

    def __init__(self,brand_name,specification,type,price):
        self.brand_name=brand_name
        self.specification=specification
        self.type=type
        self.price=price