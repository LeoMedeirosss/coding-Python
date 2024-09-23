import argparse
import psycopg2
from psycopg2 import sql
from datetime import datetime

def connect():
    conn = psycopg2.connect(
        dbname="restaurante",
        user="user",
        password="password",
        host="db",
        port="5432"
    )
    return conn

def create_customer(conn, customer_name):
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO customers (customer_name)
            VALUES (%s)
            """,
            (customer_name,)
        )
    conn.commit()
    print(f"Customer {customer_name} created")

def create_dish(conn, dish_name, price):
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO dishes (dish_name, price)
            VALUES (%s, %s)
            """,
            (dish_name, price)
        )
    conn.commit()
    print(f"Dish {dish_name} with price {price} created")

def create_order(conn, customer_name, dish_name, quantity):
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO orders (customer_id, dish_id, quantity)
            VALUES (
                (SELECT customer_id FROM customers WHERE customer_name = %s),
                (SELECT dish_id FROM dishes WHERE dish_name = %s),
                %s
            )
            """,
            (customer_name, dish_name, quantity)
        )
    conn.commit()
    print(f"Order created for {customer_name}, {dish_name}, {quantity}")

def update_order(conn, order_id, dish_name, quantity):
    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE orders
            SET dish_id = (SELECT dish_id FROM dishes WHERE dish_name = %s),
                quantity = %s
            WHERE order_id = %s
            """,
            (dish_name, quantity, order_id)
        )
    conn.commit()
    print(f"Order {order_id} updated to {dish_name}, {quantity}")

def update_order_status(conn, order_id, status):
    with conn.cursor() as cur:
        cur.execute(
            """
            UPDATE orders
            SET status = %s
            WHERE order_id = %s
            """,
            (status, order_id)
        )
    conn.commit()
    print(f"Order {order_id} status updated to {status}")

def retrieve_orders(conn):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT o.order_id, c.customer_name, d.dish_name, o.quantity, o.order_date, o.status
            FROM orders o
            JOIN customers c ON o.customer_id = c.customer_id
            JOIN dishes d ON o.dish_id = d.dish_id
            ORDER BY o.order_id
            """
        )
        rows = cur.fetchall()
        if rows:
            for row in rows:
                order_id, customer_name, dish_name, quantity, order_date, status = row
                formatted_date = order_date.strftime("%d/%m/%Y %H:%M:%S")
                print(f"Order ID: {order_id}, Customer: {customer_name}, Dish: {dish_name}, Quantity: {quantity}, Date: {formatted_date}, Status: {status}")
        else:
            print("No orders found")

def list_orders_by_status(conn, status):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT o.order_id, c.customer_name, d.dish_name, o.quantity, o.order_date, o.status
            FROM orders o
            JOIN customers c ON o.customer_id = c.customer_id
            JOIN dishes d ON o.dish_id = d.dish_id
            WHERE o.status = %s
            """,
            (status,)
        )
        rows = cur.fetchall()
        if rows:
            for row in rows:
                order_id, customer_name, dish_name, quantity, order_date, status = row
                formatted_date = order_date.strftime("%d/%m/%Y %H:%M:%S")
                print(f"Order ID: {order_id}, Customer: {customer_name}, Dish: {dish_name}, Quantity: {quantity}, Date: {formatted_date}, Status: {status}")
        else:
            print(f"No {status} orders found")

def list_customers(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM customers")
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No customers found")

def list_dishes(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM dishes")
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No dishes found")

def delete_order(conn, order_id):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM orders WHERE order_id = %s", (order_id,))
    conn.commit()
    print(f"Order {order_id} deleted")

def delete_customer(conn, customer_id):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM customers WHERE customer_id = %s", (customer_id,))
    conn.commit()
    print(f"Customer {customer_id} deleted")

def delete_dish(conn, dish_id):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM dishes WHERE dish_id = %s", (dish_id,))
    conn.commit()
    print(f"Dish {dish_id} deleted")

def main():
    parser = argparse.ArgumentParser(description='Restaurant Order Management')
    subparsers = parser.add_subparsers(dest='command')

    parser_create_customer = subparsers.add_parser('create_customer')
    parser_create_customer.add_argument('customer_name')

    parser_create_dish = subparsers.add_parser('create_dish')
    parser_create_dish.add_argument('dish_name')
    parser_create_dish.add_argument('price', type=float)

    parser_create_order = subparsers.add_parser('create_order')
    parser_create_order.add_argument('customer_name')
    parser_create_order.add_argument('dish_name')
    parser_create_order.add_argument('quantity', type=int)

    parser_update = subparsers.add_parser('update')
    parser_update.add_argument('order_id', type=int)
    parser_update.add_argument('dish_name')
    parser_update.add_argument('quantity', type=int)

    parser_update_status = subparsers.add_parser('update_status')
    parser_update_status.add_argument('order_id', type=int)
    parser_update_status.add_argument('status')

    parser_retrieve = subparsers.add_parser('retrieve')

    parser_list_pending = subparsers.add_parser('list_pending')

    parser_list_completed = subparsers.add_parser('list_completed')

    parser_list_customers = subparsers.add_parser('list_customers')

    parser_list_dishes = subparsers.add_parser('list_dishes')

    parser_delete = subparsers.add_parser('delete')
    parser_delete.add_argument('order_id', type=int)

    parser_delete_customer = subparsers.add_parser('delete_customer')
    parser_delete_customer.add_argument('customer_id', type=int)

    parser_delete_dish = subparsers.add_parser('delete_dish')
    parser_delete_dish.add_argument('dish_id', type=int)

    args = parser.parse_args()
    conn = connect()

    if args.command == 'create_customer':
        create_customer(conn, args.customer_name)
    elif args.command == 'create_dish':
        create_dish(conn, args.dish_name, args.price)
    elif args.command == 'create_order':
        create_order(conn, args.customer_name, args.dish_name, args.quantity)
    elif args.command == 'update':
        update_order(conn, args.order_id, args.dish_name, args.quantity)
    elif args.command == 'update_status':
        update_order_status(conn, args.order_id, args.status)
    elif args.command == 'retrieve':
        retrieve_orders(conn)
    elif args.command == 'list_pending':
        list_orders_by_status(conn, 'Pendente')
    elif args.command == 'list_completed':
        list_orders_by_status(conn, 'Concluido')
    elif args.command == 'list_customers':
        list_customers(conn)
    elif args.command == 'list_dishes':
        list_dishes(conn)
    elif args.command == 'delete':
        delete_order(conn, args.order_id)
    elif args.command == 'delete_customer':
        delete_customer(conn, args.customer_id)
    elif args.command == 'delete_dish':
        delete_dish(conn, args.dish_id)

    conn.close()

if __name__ == "__main__":
    main()
