import re
import mysql.connector

global connection

# Establish the connection with the database
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "eathub_db"
)

# Extract session_id from the name
def get_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_id = match.group(1)
        return extracted_id

# Convert food list into string
def get_str_from_food_list(food_list: list):
    string = ", ".join([item for item in food_list])
    return string

# Convert food dictionary into string
def get_str_from_food_dict(food_dict: dict):
    string = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return string

# Function to get the next available order_id
def get_next_order_id():
    cursor = connection.cursor()

    query = "SELECT MAX(order_id) FROM orders"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    cursor.close()

    if result is None:
        return 1
    else:
        return result + 1

# Function to update the database
def insert_to_database(order: dict):
    next_order_id = get_next_order_id()

    for food_item, quantity in order.items():
        rcode = insert_order_item(
            food_item,
            quantity,
            next_order_id
        )

        if rcode == -1:
            return -1
        
    order_total = get_order_price(next_order_id)

    insert_tracking(next_order_id, "Preparing", order_total)

    return next_order_id

# Function to call the MySQL procedure and insert items to orders
def insert_order_item(food_item, quantity, next_order_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('insert_order_item', (food_item, quantity, next_order_id))
        connection.commit()
        cursor.close()

        print("Order item added successfully!")
        return 1

    except Exception as e:
        print(f"Error occurred: {e}")
        connection.rollback()
        return -1

# Function to insert order into the order_tracking
def insert_tracking(order_id, status, order_total):
    cursor = connection.cursor()

    insert_query = "INSERT INTO order_tracking(order_id, status, order_total) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (order_id, status, order_total))
    connection.commit()
    cursor.close()

# Function to get the total price for order
def get_order_price(order_id):
    cursor = connection.cursor()
    query = "SELECT quantity, total_price FROM orders WHERE order_id = %s"
    cursor.execute(query, (order_id,))
    rows = cursor.fetchall()
    cursor.close()

    total_order_price = sum(total_price for _, total_price in rows)

    return total_order_price

# Function to track order
def get_order_status(order_id):
    cursor = connection.cursor()

    query = f"SELECT status FROM order_tracking WHERE order_id = {order_id}"
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()

    if result:
        return result[0]
    else:
        return None
    