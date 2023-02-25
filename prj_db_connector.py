import pymysql


def get_user(user_id):
    try:
        schema_name = 'freedb_DevOpsDB202212'
        # Establishing a connection to DB
        conn = pymysql.connect(
            host='sql.freedb.tech',
            port=3306,
            user='freedb_devuser',
            passwd='Xr2&HQ3nX#gX2#E',
            db=schema_name)
        conn.autocommit(True)

        # Getting a cursor from Database
        cursor = conn.cursor()

        # Get data from table
        cursor.execute(f"SELECT user_name FROM {schema_name}.users WHERE user_id='{user_id}';")
        row = cursor.fetchone()
        username = row[0]

        cursor.close()
        conn.close()

        return username

    except Exception as e:
        return f'somthing went wrong, error {e}'

    # finally:


def add_user(user_id, user_name):

    try:
        schema_name = 'freedb_DevOpsDB202212'
        # Establishing a connection to DB
        conn = pymysql.connect(
            host='sql.freedb.tech',
            port=3306,
            user='freedb_devuser',
            passwd='Xr2&HQ3nX#gX2#E',
            db=schema_name)
        conn.autocommit(True)

        # Getting a cursor from Database
        cursor = conn.cursor()

        # Inserting data into table
        cursor.execute(f"INSERT into {schema_name}.users (user_id, user_name) VALUES ('{user_id}', '{user_name}');")

        cursor.close()
        conn.close()
        return cursor

    except Exception as e:
        f = f'somthing went wrong, error {e}'
    return f


def validate_user(user_id, user_name):

    try:
        schema_name = 'freedb_DevOpsDB202212'
        # Establishing a connection to DB
        conn = pymysql.connect(
            host='sql.freedb.tech',
            port=3306,
            user='freedb_devuser',
            passwd='Xr2&HQ3nX#gX2#E',
            db=schema_name)
        conn.autocommit(True)

        # Getting a cursor from Database
        cursor = conn.cursor()

        # Inserting data into table
        cursor.execute(f"SELECT * FROM {schema_name}.users WHERE user_id='{user_id}' AND user_name='{user_name}';")

        cursor.close()
        conn.close()
        return cursor

    except Exception as e:
        f = f'somthing went wrong, error {e}'
    return f


def put_user(user_id, user_name):
    try:
        schema_name = 'freedb_DevOpsDB202212'
        # Establishing a connection to DB
        conn = pymysql.connect(
            host='sql.freedb.tech',
            port=3306,
            user='freedb_devuser',
            passwd='Xr2&HQ3nX#gX2#E',
            db=schema_name)
        conn.autocommit(True)

        # Getting a cursor from Database
        cursor = conn.cursor()

        # Inserting data into table
        cursor.execute(f"UPDATE {schema_name}.users SET user_id = '{user_id}' WHERE user_name = '{user_name}';")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f'somthing went wrong, error {e}')

    # finally:
    #     if conn.open():
    #         cursor.close()
    #         conn.close()
    #         print("MySQL connection is closed")


def delete_user(user_id):
    try:
        schema_name = 'freedb_DevOpsDB202212'
        # Establishing a connection to DB
        conn = pymysql.connect(
            host='sql.freedb.tech',
            port=3306,
            user='freedb_devuser',
            passwd='Xr2&HQ3nX#gX2#E',
            db=schema_name)
        conn.autocommit(True)

        # Getting a cursor from Database
        cursor = conn.cursor()

        # Inserting data into table
        cursor.execute(f"DELETE FROM {schema_name}.users WHERE user_id = '{user_id}';")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f'somthing went wrong, error {e}')


