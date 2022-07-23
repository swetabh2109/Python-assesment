import sqlite3
import csv
import pandas as pd

try:
    

    # Creating a connection to SQLite3
    sqliteConnection = sqlite3.connect('XYZ.db')
    print("Successfully Connected to SQLite and database provided")

    # Putting the result of query into a dataframe
    df = pd.read_sql_query("SELECT s.customer_id, c.age, i.item_name, SUM(o.quantity) FROM CUSTOMER c INNER JOIN SALES s ON c.customer_id = s.customer_id INNER JOIN ORDERS o ON s.sales_id = o.sales_id INNER JOIN ITEMS i ON o.item_id = i.item_id WHERE c.age BETWEEN 18 AND 35 GROUP BY o.item_id" , sqliteConnection)
    
    #Convert Dataframe into CSV file
    df.to_csv('c:/Result.csv', sep= ';')
    

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")




