import psycopg


def get_connection():
    return psycopg.connect(
        host="localhost",
        dbname="bank_system",
        user="postgres",
        password="12345678",
        port=5432
    )


def get_customer(name, password):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT customer_id, name, password
        FROM customers
        WHERE name = %s AND password = %s
        """,
        (name, password)
    )

    customer = cursor.fetchone()

    cursor.close()
    connection.close()

    return customer


def get_account(customer_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT account_id, customer_id, balance, account_type
        FROM accounts
        WHERE customer_id = %s
        """,
        (customer_id,)
    )

    account = cursor.fetchone()

    cursor.close()
    connection.close()

    return account


def get_account_by_id(account_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT account_id, customer_id, balance, account_type
        FROM accounts
        WHERE account_id = %s
        """,
        (account_id,)
    )

    account = cursor.fetchone()

    cursor.close()
    connection.close()

    return account


def update_balance(account_id, balance):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE accounts
        SET balance = %s
        WHERE account_id = %s
        """,
        (balance, account_id)
    )

    connection.commit()

    cursor.close()
    connection.close()


def transfer_money(sender_id, receiver_id, amount):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE accounts
        SET balance = balance - %s
        WHERE account_id = %s
        """,
        (amount, sender_id)
    )

    cursor.execute(
        """
        UPDATE accounts
        SET balance = balance + %s
        WHERE account_id = %s
        """,
        (amount, receiver_id)
    )

    connection.commit()

    cursor.close()
    connection.close()


def change_password(customer_id, new_password):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE customers
        SET password = %s
        WHERE customer_id = %s
        """,
        (new_password, customer_id)
    )

    connection.commit()

    cursor.close()
    connection.close()