from passlib.context import CryptContext


# SQLALCHEMY_DATABASE_URL = "mariadb+pymysql://root:Snex2022@127.0.0.1:3306/fast"

SQLALCHEMY_DATABASE_URL = "postgresql://myuser:1234@fastapi_postgres_1:5432/fastapi_database"
hasher= CryptContext(schemes=['bcrypt'])
SECRET = hasher.hash('hsenixuglcsgnjbkfbdgcevicpo5hwoierhcvoidmxsoy3m77nc47grfbcdunzskkk4747xnygoaumu0t7imcxgb')