import pymysql

def connect(
    host: str = 'localhost',
    port: int = 3306,
    user: str = 'root',
    password: str = '',
    database: str = '',
) -> pymysql.connections.Connection:
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
    )
    return conn

def connection_test(
    host: str = 'localhost',
    port: int = 3306,
    user: str = 'root',
    password: str = '',
    database: str = '',
) -> bool:
    try:
        conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
        )
        conn.close()
        return True
    
    except pymysql.MySQLError as e:
        print(f"Conenction failed: {e}")
        return False
