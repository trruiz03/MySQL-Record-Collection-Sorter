#import libraries 
import mysql.connector 
from mysql.connector import Error
import pandas as pd
from IPython.display import display

#Start MySQL Connection
def create_server_connection(host_name, user_name, user_password):
    connection = None

    try:
        connection = mysql.connector.connect(
            host = host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection = create_server_connection("localhost", "root", "FreddyThanosBB812")
#End of database Connection

#Create Database
#def create_database(connection, query):
    #cursor = connection.cursor()
    #try:
        #cursor.execute(query)
        #print("Database created successfully")
    #except Error as err:
        #print(f"Error: '{err}'")


#create_database_query = "CREATE DATABASE vinyl"
#create_database(connection, create_database_query)
#End of database creation

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_query(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

create_artist_table = """
CREATE TABLE artist (
artist_name VARCHAR(40) NOT NULL,
album_name VARCHAR(40) NOT NULL,
record_version VARCHAR(40) NOT NULL,
sale_price INT
);
"""


# populate the artist table
pop_artist ="""
    INSERT INTO artist (artist_name, album_name, record_version, sale_price)
    VALUES
    
"""


#connection = create_db_connection("localhost", "root", "FreddyThanosBB812", "vinyl")
#execute_query(connection, create_artist_table) #Execute defined query

#UNCOMMENT BELOW TO PUSH NEW DATA TO ARTIST TABLE
#execute_query(connection, pop_artist)

#view table/sort and execute MySQL command
#SELECT * FROM artist ORDER BY artist_name, album_name;

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

q1 = """
        SELECT * FROM artist ORDER BY artist_name, album_name;
        """
connection = create_db_connection("localhost", "root", "FreddyThanosBB812", "vinyl")

from_db = []

results = read_query(connection, q1)
for result in results:
            result = list(result)
            from_db.append(result)   

columns = ["Artist", "Album", "Version", "Price"]
df = pd.DataFrame(from_db, columns=columns)  
display(df)

connection.close()

'''
logged records
('ACDC', 'Who Made Who', 'Standard', 4)
('ACDC', '74 Jailrock', 'Standard', 4)
('ACDC', 'Highway to Hell', 'Standard', 4)
('ACDC', 'Flick of the Switch', 'Standard', 4)
('ACDC', 'Get your Wings', 'Standard', 4)
('ACDC', 'For Those About to Rock', 'Standard', 4)
('ACDC', 'Fly on The Wall', 'Standard', 4)
('ACDC', 'High Voltage', 'Standard', 4)
('ACDC', 'Back in Black', 'Standard', 4)
('Aerosmith', 'Rocks', 'Standard', 4)
__________________________________________

'''


