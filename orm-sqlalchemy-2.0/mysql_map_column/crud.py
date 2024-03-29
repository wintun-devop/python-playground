from models import Product
from models.db import db_session
from sqlalchemy.exc import SQLAlchemyError

# data format
""" 
name='Mikrotik L009UiGS-RM'
model_no='L009UiGS-RM-T2'
description='L009 is more than just a router.' 
"""

def create(name:str,model_no:str,description:str) -> dict:
    n = name
    m = model_no
    d = description
    add_person = Product(name=n,model_no=m,description=d)
    try:
        db_session.add(add_person)
        db_session.commit()
        result = db_session.query(Product).filter_by(model_no=m).first()
        res = {"id":str(result.id),"name":n,"model_no":m,"description":d}
        print(res)
        return res
    except SQLAlchemyError as e:
        print("error",e)
        raise e

def get_one(id:str)->dict:
    id = id
    try:
        result = db_session.query(Product).filter_by(id=id).first()
        res = {"id":str(result.id),"name":result.name,"model_no":result.model_no,"description":result.description}
        print(res)
        return res
    except SQLAlchemyError as e:
        # print("error",e)
        raise e

def get_all()->list:
    try:
        result = db_session.query(Product).all()
        res = []
        for row in result:
            row_result = {"id":str(row.id), "name":row.name,"model_no":row.model_no,"description":row.description}
            res.append(row_result)
        print(res)
        return res
    except SQLAlchemyError as e:
        # print("error",e)
        raise e

def delete(id)->None:
    id=id
    try:
        result=db_session.query(Product).filter_by(id=id).delete(synchronize_session=False)
        print(result)
        db_session.commit()
        return None
    except SQLAlchemyError as e:
        # print("error",e)
        raise e

def update(id:str,name:str,model_no:str,description:str)->dict:
    id=id
    try:
        result=db_session.query(Product).filter_by(id=id).first()
        if result:
            result.name=name
            result.model_no=model_no
            result.description=description
            db_session.add(result)
            db_session.commit()
            res = {"id":str(result.id),"name":result.name,"model_no":result.model_no,"description":result.description}
            print(res)
            return res
    except SQLAlchemyError as e:
        # print("error",e)
        raise e

# create("CCR CCR2004-16G-2S+PC","CCR2004-16G-2S-t25","Approximately 200'000 hours at 25C")
# get_one("d28a3597-acfd-461c-bdaa-27f57c302e58")
# get_all()
# delete("d28a3597-acfd-461c-bdaa-27f57c302e58")
""" update   """
# update("abd4ecc2-ed07-4e94-8a23-72fa1f66155b","CCR CCR2004-16G-2S+PC","CCR2004-16G-2-5","Update")