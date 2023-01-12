import psycopg2


def create_table(db_connect):
    query = """
        CREATE TABLE IF NOT EXISTS "iris_data" (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP,
            sepal_length float8,
            sepal_width float8,
            petal_length float8,
            petal_width float8,
            target int
        );"""

    with db_connect.cursor() as cur:
        cur.execute(query)
        db_connect.commit()


if __name__ == "__main__":
    # Connect to db
    db_connect = psycopg2.connect(
        user="myuser",
        password="mypassword",
        host="localhost",
        port=5432,
        database="mydatabase",
    )

    # Create table
    create_table(db_connect)
