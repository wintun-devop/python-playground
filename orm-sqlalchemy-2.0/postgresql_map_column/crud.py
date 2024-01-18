from models.db import db_session
from models import Product
from sqlalchemy.exc import SQLAlchemyError


def create():
    add_person = Product(name='Mikrotik L009UiGS-RM',model_no='L009UiGS-RM-T1',description='L009 is more than just a router.')
    try:
        db_session.add(add_person)
        db_session.commit()
        result = db_session.query(Product)
        print({"msg":"success"})
    except SQLAlchemyError as e:
        print(e)

create()
    