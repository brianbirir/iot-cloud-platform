import psycopg2
from config import DatabaseInitializationConfig


db_config = DatabaseInitializationConfig()


def check_database():
    """Checks for specified database existence"""
    try:
        conn = psycopg2.connect(dbname=db_config.POSTGRES_DATABASE_NAME,
                                user=db_config.POSTGRES_DATABASE_USER,
                                password=db_config.POSTGRES_DATABASE_PASSWORD,
                                host=db_config.POSTGRES_DATABASE_HOST,
                                port=db_config.POSTGRES_DATABASE_PORT)

        print(conn)
    except psycopg2.DatabaseError as e:
        print(e)

def create_user():
    try:
        conn = psycopg2.connect(dbname=db_config.POSTGRES_DATABASE_NAME,
                                user=db_config.POSTGRES_DATABASE_USER,
                                password=db_config.POSTGRES_DATABASE_PASSWORD,
                                host=db_config.POSTGRES_DATABASE_HOST,
                                port=db_config.POSTGRES_DATABASE_PORT)
        cur = conn.cursor()
        sql_statement = ""

        cur.execute()
    except psycopg2.DatabaseError as e:
        print(e)
# def create_database():
#     """Creates PostgreSQL database"""
#     try:
#         conn = psycopg2.connect(dbname=db_config.POSTGRES_DATABASE_NAME,
#                                 user=db_config.POSTGRES_DATABASE_USER,
#                                 password=db_config.POSTGRES_DATABASE_PASSWORD,
#                                 host=db_config.POSTGRES_DATABASE_HOST,
#                                 port=db_config.POSTGRES_DATABASE_PORT)
#
#     except psycopg2.DatabaseError as e:
#         print(e)


if __name__ == "__main__":
    check_database()
