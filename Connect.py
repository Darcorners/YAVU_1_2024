import pymysql
from Config import host, user, password, database


try:
    connection = pymysql.connections.Connection(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = database,
        cursorclass = pymysql.cursors.DictCursor
    )
    print('Соединение успешно')
    print('\n')

except Exception as ex:
    print("\nПрограмма выполнена с ошибками")
    print(ex)