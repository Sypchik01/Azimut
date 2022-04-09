from data.db import db_connect
from data.sql import get_sql


def text_len(sql_input):
    sql_output = ''
    for i in sql_input:
        sql_output += i + '\n--\n'
    return sql_output
