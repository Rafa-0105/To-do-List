import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def conn():
    try:
        user = os.getenv("USER")
        password = os.getenv("PASSWORD")
        host = os.getenv("HOST")
        port = os.getenv("PORT")
        database = os.getenv("DATABASE")
        url = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
        engine = create_engine(url)

        if engine:
            print("Conection Sucess!")
        else:
            print("Erro to conection")
    except ValueError as error:
        print(error)

    return engine