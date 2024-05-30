from app import session
from models import brand_tbl
brand_name=input("Enter brand name:   ")
specification=input("Enter specification:   ")
type=input("Enter the type:     ")
price=float(input("Enter the price:  "))
new_input=brand_tbl(
    brand_name=brand_name,
    specification=specification,
    type=type,
    price=price
)
session.add(new_input)
session.commit()