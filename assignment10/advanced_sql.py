import sqlite3


try:
    # Connecting to the database
   

    conn = sqlite3.connect("../db/lesson.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # Task 1: Complex JOINs with Aggregation

    query_1 = """
        SELECT
            orders.order_id,
            SUM(products.price * line_items.quantity) AS total_price
        FROM orders
        JOIN line_items
            ON orders.order_id = line_items.order_id
        JOIN products
            ON line_items.product_id = products.product_id
        GROUP BY orders.order_id
        ORDER BY orders.order_id
        LIMIT 5;
    """

    cursor.execute(query_1)

    results_1 = cursor.fetchall()

    print("Task 1: First 5 Order Totals")

    for order_id, total_price in results_1:
        print(
            f"Order {order_id}: "
            f"${total_price:.2f}"
        )

    # Task 2: Understanding Subqueries

    query_2 = """
        SELECT
            customers.customer_name,
            AVG(order_totals.total_price) AS average_total_price
        FROM customers
        LEFT JOIN (
            SELECT
                orders.customer_id AS customer_id_b,
                orders.order_id,
                SUM(
                    products.price * line_items.quantity
                ) AS total_price
            FROM orders
            JOIN line_items
                ON orders.order_id = line_items.order_id
            JOIN products
                ON line_items.product_id = products.product_id
            GROUP BY
                orders.order_id,
                orders.customer_id
        ) AS order_totals
            ON customers.customer_id =
               order_totals.customer_id_b
        GROUP BY
            customers.customer_id,
            customers.customer_name
        ORDER BY customers.customer_id;
    """

    cursor.execute(query_2)

    results_2 = cursor.fetchall()

    print("\nTask 2: Average Order Price by Customer")

    for customer_name, average_total_price in results_2:
        if average_total_price is None:
            print(
                f"{customer_name}: "
                "No orders"
            )
        else:
            print(
                f"{customer_name}: "
                f"${average_total_price:.2f}"
            )


    # Task 3: Inserting Transactions Based on data

    print("\nTask 3: Creating a New Order")

    #Finding the customer_id for Perez and Sons

    cursor.execute("""
        SELECT customer_id
        FROM customers
        WHERE customer_name = ?;
    """, ("Perez and Sons",))

    customer = cursor.fetchone()

    if customer is None:
        raise ValueError("Customer 'Perez and Sons' not found.")

    customer_id = customer[0]

    # Finding the employee_id for Miranda Harris

    cursor.execute("""
        SELECT employee_id
        FROM employees
        WHERE first_name = ?
            AND last_name = ?;
    """, ("Miranda", "Harris"))

    employee = cursor.fetchone()

    if employee is None:
        raise ValueError("Employee 'Miranda Harris' not found.")

    employee_id = employee[0]

    # Finding the 5 least expensive products

    cursor.execute("""
        SELECT product_id
        FROM products
        ORDER BY price ASC
        LIMIT 5;
    """)

    product_rows = cursor.fetchall()

    product_ids = [row[0] for row in product_rows]

    if len(product_ids) < 5:
        raise ValueError("The Database does not contain enough products.")

    # Create the order and line items in one transaction

    with conn:
        # Create the order and retrieve the new order_id
        cursor.execute("""
            INSERT INTO orders (customer_id, employee_id, date)
            VALUES (?, ?, DATE('now'))
            RETURNING order_id;
        """, (customer_id, employee_id))

        order_id = cursor.fetchone()[0]

        # Add 10 of each of the 5 cheapest products 
        for product_id in product_ids:
            cursor.execute("""
                INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, ?);
            """, (order_id, product_id, 10))

    print(f"New order created with order_id: {order_id}")

    # Display the line items for the new order

    cursor.execute("""
        SELECT
            line_items.line_item_id,
            line_items.quantity,
            products.product_name
        FROM line_items
        JOIN products
            ON line_items.product_id = products.product_id
        WHERE line_items.order_id = ?
        ORDER BY line_items.line_item_id;
    """, (order_id,))

    new_order_items = cursor.fetchall()

    print("\nItems in the new order:")

    for line_item_id, quantity, product_name in new_order_items:
        print(
            f"Line Item {line_item_id}: "
            f"{quantity} x {product_name}"
        )

    # Task 4: Aggregation with HAVING

    query_4 = """
        SELECT
            employees.first_name || ' ' || employees.last_name AS employee_name,
            COUNT(orders.order_id) AS order_count
        FROM employees
        JOIN orders
            ON employees.employee_id = orders.employee_id
        GROUP BY employees.employee_id,
            employees.first_name,
            employees.last_name
        HAVING COUNT(orders.order_id) > 5
        ORDER BY order_count DESC;
    """

    cursor.execute(query_4)

    results_4 = cursor.fetchall()

    print("\nTask 4: Employees Associated with More Than 5 Orders")

    for employee_name, order_count in results_4:
        print(
            f"{employee_name}: "
            f"{order_count} orders"
        )
    
    


except sqlite3.Error as error:
    print(f"SQLite error: {error}")


finally:
    if "conn" in locals():
        conn.close()
        print("\nDatabase connection closed.")