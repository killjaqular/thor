# <Document_Header Start>
"""
filename : InsertCSVIntoDatabase.py # name of this file
author : Adonay Pichardo # name of original engineer
date : 03-OCT-2021 # date of original commit

description :
Used to automate insertion of data into the database from a given csv
"""
# <Document_Header End>

# <Standard Imports Start>
# List all imports alphabetically for Python3 standard libraries
from sys import argv, stdout
import mysql.connector
# <Standard Imports End>

# <Internal Imports Start>
# List all imports alphabetically for libraries authored for Thor
# <Internal Imports End>

# <External Imports Start>
# List all imports alphabetically for libraries NOT authored for Thor
# <External Imports End>

# <Global Objects Start>
# <Global Objects End>

# <Classes Start>
# <Classes End>

# <Functions Start>
def insert_into_table(table_name, data_to_insert):
    '''
    table_name:     string, name of the table to insert into
    data_to_insert: list,   list of strings to insert into table
    '''
    INSERT_SYNTAX = "INSERT INTO " + table_name + " VALUES "
    for 

def main():
    if len(argv) != 2:
        stdout.write(f'USAGE: python3 InsertCSVIntoDatabase.py <path\\to\\csv\\file.csv>\n')
        exit()
ß
    ################################
    # Get locally stored database information
    ################################    
    # /home/pi/database_credentials on the Raspberry Pi 3
    database_credentials = open('D:\\FloTech_2021_FALL\\database_credentials.txt', 'r')
    host, user, password, database = [item for item in database_credentials.read().split('\n') if len(item) > 0]

    ################################
    # Create mySQL Connector
    ################################
    connection = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )

    try:
        csv_file = open(argv[1], 'r')



    except Error as error:
        stdout.write(f'ERROR:_> {error}\n')

# <Functions End>

if __name__ == "__main__":
    main()
