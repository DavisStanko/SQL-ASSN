import sqlite3
import sys

################## DB SQL Functionality ####################

# UPDATE #
def update_product(data):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        sql = "update Product set Name=?, Price=? where ProductID=?"
        cursor.execute(sql, data)
        db.commit()


def update_UI():
    # user input is requested
    product_ID = input("Please enter product ID to edit.\n")
    product_name = input("Please enter the new name: \n")
    print("Please enter price of %s: " % product_name)
    product_price = input()
    data = (product_name, product_price, product_ID)
    update_product(data)


# FIND #
def select_all_products():
    global productsAll
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Product")
        productsAll = cursor.fetchall()
        return productsAll


def select_product(id):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute(
            "select Name,Price from Product where ProductID=?", (id,))
        product = cursor.fetchone()
        return product


def select_products_UI():
    # user input is requested
    choice = input(
        "Enter \'one' for a specific product ID and \'all' for all products in the DB.\n")
    choice = choice.lower()
    choice = choice.strip()
    if choice == 'one':
        product_ID = int(input("Please enter product ID to find.\n"))

        print(select_product(product_ID))
    elif choice == 'all':

        print(select_all_products())
    else:
        print("Please select again.\n")


def select_products_UI():
    product_ID = int(input("Please enter product ID to find.\n"))
    print(select_product(product_ID))


# DELETE #
def delete_product(data):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        sql = "delete from product where Name=?"
        cursor.execute(sql, data)
        db.commit()


def delete_UI():
    # user input is requested
    product_ID = int(input("Please enter product ID to delete.\n"))
    data = (product_ID,)
    delete_product(data)
    print("Deleted product ID number %s" % product_ID)


# LIST sort/order products
def list_products_UI():
    print("\nAdd DB SQL code here to list and sort products by name or price.")
    # user input is requested
    choice = input(
        "Enter \'one' for a specific product ID and \'all' for all products in the DB.\n")
    choice = choice.lower()
    choice = choice.strip()
    if choice == 'one':
        product_ID = int(input("Please enter product ID to find.\n"))
        print(select_product(product_ID))
    elif choice == 'all':

        print(select_all_products())
    else:
        print("Please select again.\n")

    input("\nPress enter to continue.")


def list_product():
    print("filler")
