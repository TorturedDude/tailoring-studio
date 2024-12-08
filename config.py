from os import getenv

from dotenv import load_dotenv


load_dotenv()

#Database
DB_USER = getenv('DB_USER')
DB_PASSWORD = getenv('DB_PASSWORD')
DB_HOST = getenv('DB_HOST')
DB_PORT = getenv('DB_PORT')
DB_NAME = getenv('DB_NAME')

#JWT
SECRET_KEY=getenv('SECRET_KEY')
ALGORITHM=getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES=getenv('ACCESS_TOKEN_EXPIRE_MINUTES')