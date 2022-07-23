import sqlite3
import csv

try:
    #Creating a CSV file4
    d = open('c:/Result.csv', 'w')
    c = csv.writer(d, delimiter=;)

    # Creating a connection to SQLite3
    sqliteConnection = sqlite3.connect('XYZ.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite and database provided")

    # Query for having the desired output
    sqlite_select_query = """SELECT s.customer_id, c.age, i.item_name, SUM(o.quantity) FROM CUSTOMER c 
                             INNER JOIN SALES s ON c.customer_id = s.customer_id
                             INNER JOIN ORDERS o ON s.sales_id = o.sales_id
                             INNER JOIN ITEMS i ON o.item_id = i.item_id
                             WHERE c.age BETWEEN 18 AND 35
                             GROUP BY o.item_id"""
    #Executing the Query
    cursor.execute(sqlite_select_query)
    # Writing the column heading
    co = [i[0] for i in cursor.description]
    c.writerow(co)

    #Fetch the data and save in the file
    data=cursor.fetchall()
    for item in data:
        if (item[3] == 0):
            print("Rows with quantity as 0 is being removed from the file")
        else:
            c.writerow(item)

    # Close the file
    d.close()
    print("Result.csv file is created!")

    # Close the cursor
    cursor.close()

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")




