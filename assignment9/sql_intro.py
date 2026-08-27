import sqlite3

# Functions for adding data

def add_publisher(conn, name):
    try:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id FROM publishers WHERE name = ?",
            (name,)
        )

        existing = cursor.fetchone()

        if existing:
            return existing[0]

        cursor.execute(
            "INSERT INTO publishers (name) VALUES (?)",
            (name,)
        )

        return cursor.lastrowid

    except sqlite3.Error as error:
        print(f"Error adding publisher: {error}")
        return None


def add_magazine(conn, name, publisher_id):
    try:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id FROM magazines WHERE name = ?",
            (name,)
        )

        existing = cursor.fetchone()

        if existing:
            return existing[0]

        cursor.execute(
            """
            INSERT INTO magazines (name, publisher_id)
            VALUES (?, ?)
            """,
            (name, publisher_id)
        )

        return cursor.lastrowid

    except sqlite3.Error as error:
        print(f"Error adding magazine: {error}")
        return None


def add_subscriber(conn, name, address):
    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id
            FROM subscribers
            WHERE name = ? AND address = ?
            """,
            (name, address)
        )

        existing = cursor.fetchone()

        if existing:
            return existing[0]

        cursor.execute(
            """
            INSERT INTO subscribers (name, address)
            VALUES (?, ?)
            """,
            (name, address)
        )

        return cursor.lastrowid

    except sqlite3.Error as error:
        print(f"Error adding subscriber: {error}")
        return None


def add_subscription(
    conn,
    subscriber_id,
    magazine_id,
    expiration_date
):
    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id
            FROM subscriptions
            WHERE subscriber_id = ?
              AND magazine_id = ?
              AND expiration_date = ?
            """,
            (
                subscriber_id,
                magazine_id,
                expiration_date
            )
        )

        existing = cursor.fetchone()

        if existing:
            return existing[0]

        cursor.execute(
            """
            INSERT INTO subscriptions
            (
                subscriber_id,
                magazine_id,
                expiration_date
            )
            VALUES (?, ?, ?)
            """,
            (
                subscriber_id,
                magazine_id,
                expiration_date
            )
        )

        return cursor.lastrowid

    except sqlite3.Error as error:
        print(f"Error adding subscription: {error}")
        return None


# Main program

try:
    with sqlite3.connect("../db/magazines.db") as conn:

        conn.execute("PRAGMA foreign_keys = 1")

        cursor = conn.cursor()

        # Create publishers table

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS publishers (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE
            );
        """)

        # Create magazines table

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS magazines (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                publisher_id INTEGER NOT NULL,
                FOREIGN KEY (publisher_id)
                    REFERENCES publishers(id)
            );
        """)


        # Create subscribers table

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                address TEXT NOT NULL
            );
        """)


        # Create subscriptions table

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                id INTEGER PRIMARY KEY,
                subscriber_id INTEGER NOT NULL,
                magazine_id INTEGER NOT NULL,
                expiration_date TEXT NOT NULL,
                FOREIGN KEY (subscriber_id)
                    REFERENCES subscribers(id),
                FOREIGN KEY (magazine_id)
                    REFERENCES magazines(id)
            );
        """)


        # Add publishers

        publisher1_id = add_publisher(
            conn,
            "National Geographic Society"
        )

        publisher2_id = add_publisher(
            conn,
            "Condé Nast"
        )

        publisher3_id = add_publisher(
            conn,
            "Time USA"
        )

        # Add magazines

        magazine1_id = add_magazine(
            conn,
            "National Geographic",
            publisher1_id
        )

        magazine2_id = add_magazine(
            conn,
            "The New Yorker",
            publisher2_id
        )

        magazine3_id = add_magazine(
            conn,
            "TIME",
            publisher3_id
        )


        # Add subscribers

        subscriber1_id = add_subscriber(
            conn,
            "Alice Johnson",
            "100 Main Street"
        )

        subscriber2_id = add_subscriber(
            conn,
            "Bella Smith",
            "225 Oak Avenue"
        )

        subscriber3_id = add_subscriber(
            conn,
            "Charlie Davis",
            "40 Pine Road"
        )


        # Add subscriptions

        add_subscription(
            conn,
            subscriber1_id,
            magazine1_id,
            "2027-01-31"
        )

        add_subscription(
            conn,
            subscriber2_id,
            magazine2_id,
            "2027-05-15"
        )

        add_subscription(
            conn,
            subscriber3_id,
            magazine3_id,
            "2027-09-30"
        )


        # Saving all changes
        conn.commit()

        print("Database populated successfully.")

        # query 1: Retrieve all subscribers
        print("\nAll Subscribers:")
        cursor.execute("""
            SELECT * 
            FROM subscribers;
        """)

        subscribers = cursor.fetchall()

        for subscriber in subscribers:
            print(subscriber)

        # Query 2: Retrieve magazines sorted by name
        print("\nMagazines sorted by name:")

        cursor.execute("""
            SELECT *
            FROM magazines
            ORDER BY name;
        """)

        magazines = cursor.fetchall()

        for magazine in magazines:
            print(magazine)

        # Query 3: Find magazines for a particular publisher

        publisher_name = "Condé Nast"

        print(f"\nMagazines published by {publisher_name}:")

        cursor.execute("""
            SELECT m.name
            FROM magazines m
            JOIN publishers p ON m.publisher_id = p.id
            WHERE p.name = ?;
        """, (publisher_name,))

        magazines = cursor.fetchall()

        for magazine in magazines:
            print(magazine)


except sqlite3.Error as error:
    print(f"SQLite error: {error}")


finally:
    if "conn" in locals():
        conn.close()
        print("Database connection closed.")