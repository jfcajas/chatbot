"""
    This class recognizes the request for a product list and creates a SQL query
    to pull product data from the store's database and print it for the customer

"""

import mysql.connector
from beautifultable import BeautifulTable as bt
import pandas as pd

mydb = mysql.connector.connect(
    user="root",
    passwd="admin",
    host="localhost",
    database="my_guitar_shop"
)
crsr = mydb.cursor(prepared=True)

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 150)


def findProducts(match):
    sql = 'SELECT product_name, list_price from products'
    crsr.execute(sql)
    matches = crsr.fetchall()
    table = bt()
    for row in matches:
        table.rows.append(row)
    df1 = pd.DataFrame(matches, columns=["Product Name", "Product Price $"])
    df2 = df1.iloc[:, [0, 1]]
    return df2


def final(match):
    print(findProducts(match))
