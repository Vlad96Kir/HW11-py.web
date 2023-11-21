from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from starlette import status

# Приклад параметрів підключення до PostgreSQL
POSTGRES_HOST = "127.0.0.1"
POSTGRES_USERNAME = "postgres"
POSTGRES_PASSWORD = "784507"
POSTGRES_PORT = "5432"
POSTGRES_DATABASE = "postgres"

# Формування URL для підключення до бази даних
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"

# Створення об'єкта з'єднання
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Функція для отримання сесії бази даних
def get_db():
    db = DBSession()
    try:
        yield db
    except SQLAlchemyError as err:
        print(err)
        db.rollback()
        raise BaseException()
    finally:
        db.close()


# Перевірка підключення (опціонально)
if __name__ == "__main__":
    print(engine)