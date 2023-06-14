from dotenv import load_dotenv
import os

load_dotenv()

from sqlalchemy import create_engine, text

host = os.getenv("HOST")
database = os.getenv("DATABASE")
user = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
connection_string = (
    "mysql+mysqlconnector://"
    + user
    + ":"
    + password
    + "@"
    + host
    + ":"
    + "3306/"
    + database
)
engine = create_engine(connection_string, echo=True)


def mysqlconnect():
    with engine.connect() as connection:
        result = connection.execute(text("select * from book_masters"))
        # column_names = connection.execute(text("show columns from book_masters"))

        # result_dicts_column = []
        # for row in column_names.all():
        #     result_dicts_column.append(row.Field)

        result_dicts = []
        for row in result.all():
            result_dicts.append(
                {
                    "serial_no": row.s_no,
                    "title": row.title,
                    "author": row.author,
                    "genre": row.genre,
                }
            )

    return result_dicts
