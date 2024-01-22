## installing alembic and sqlalchemy
```
pip install alembic sqlalchemy
```
## alembic initialization
```
alembic init migrations
```
## alembic db-source configuration-postgresql
```
[app]
sqlalchemy.url = mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}
```
## config env.py
```
import model to env.py as Admin setup
```
## migration
```
alembic revision --autogenerate -m "your migration name"
```
```
alembic upgrade heads
```
