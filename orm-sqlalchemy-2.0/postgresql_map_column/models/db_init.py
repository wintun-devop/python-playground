from db import engine
from __init__ import Base

Base.metadata.create_all(bind=engine)