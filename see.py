from app import session
from models import brand_tbl
all_record=session.query(brand_tbl).all()
for record in all_record:
    print(f"isbn_no:{record.isbn_no},brand_name:{record.brand_name},specification:{record.specification},type:{record.type},price:{record.price}")