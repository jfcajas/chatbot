"""
    This class extracts the user input and translates it into a SQL query
    to grab the customer's order info

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


def extractMatchIndex(match):
    start_index = []
    end_index = []
    for i in range(len(match)):
        if match.startswith("'# ", i):
            start_index.append(i + 3)
        elif match.startswith("'#", i):
            start_index.append(i + 2)
        if match.startswith("'>", i):
            end_index.append(i)
    return start_index, end_index


def extractMatchText(start_index, end_index, match):
    allMatchText = []
    for i in range(len(start_index)):
        allMatchText.append(match[start_index[i]:end_index[i]])
    return allMatchText


def findOrder(match):
    match = int(match)
    sql = 'SELECT * from orders where order_id =?'
    crsr.execute(sql, (match,))
    matches = crsr.fetchall()
    if not matches:
        return print('No info found for order #' + str(match))
    table = bt()
    for row in matches:
        table.rows.append(row)
    df1 = pd.DataFrame(matches, columns=["Order #", "Customer ID", "Order Date", "Ship $", "Tax $", "Ship Date",
                                         "Ship Address ID", "Card Type", "Card #", "Card Expiration Date",
                                         "Billing Address ID"])
    df2 = df1.iloc[:, [0, 2, 3, 4, 5, 9]]
    return df2


def final(rematch):
    match = str(rematch)
    start_index, end_index = extractMatchIndex(match)
    matchText = extractMatchText(start_index, end_index, match)
    for i in matchText:
        print(findOrder(i))

