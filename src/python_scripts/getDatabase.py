# <Document_Header Start>
"""
filename : getDatabase.py
author : Adonay Pichardo
description :
"Returns entire Thor Database as a 2d list"
"""
# <Document_Header End>

# <Standard Imports Start>
# List all imports alphabetically for Python3 standard libraries
from sys import argv, stdout
# <Standard Imports End>


# <Internal Imports Start>
# List all imports alphabetically for libraries authored for Thor
# NONE
# <Internal Imports End>

# <External Imports Start>
# List all imports alphabetically for libraries NOT authored for Thor
import mysql.connector
# <External Imports End>

# <Global Objects Start>
# NONE
# <Global Objects End>

# <Classes Start>
# NONE
# <Classes End>

# <Functions Start>
################################
# Returns entire database
# INPUT: connection - mysql.connector; Connection to a database that has already been
#                     authorized.
#        database   - string; Name of the database to get data from.
#        tables     - list; A list containing the names of all tables to be retrieved from
#                     the database
################################
def getAllData(connection, database, tables):
    all_tables = {} # Dictionary to hold all tables

    ################################
    # Create cursor to send queries
    ################################
    cursor = connection.cursor()

    ################################
    # Get data from table
    ################################
    for every_table in tables:
        data = [] # 2d list of a table's data
        cursor.execute(f'SELECT * FROM {database}.{every_table};\n')
        results     = cursor.fetchall()
        field_names = [each_column[0] for each_column in cursor.description]
        data.append(field_names)

        ################################
        # Step through each row
        ################################
        for every_result in results:
            # Create empty list for the current row
            row = []
            ################################
            # Step through each column
            ################################
            for every_value in every_result:
                # Collect each value in the current row
                row.append(every_value)
            # Add the row list into data of the current table
            data.append(row)

        ################################
        # Insert table and its data into the dictionary
        ################################
        all_tables[every_table] = data

    cursor.close()

    return all_tables
# <Functions End>

################################
# Creates connection to the database server with provided credentials
################################
def connectToDataBase(credentials):
    return mysql.connector.connect(host     = credentials['host'],
                                   user     = credentials['user'],
                                   password = credentials['password'],
                                   database = credentials['database']
                                   )

def main():
    ################################
    # Gather credential information
    ################################
    credentials_file = open(argv[1], 'r')
    credentials = {} # Used for authorizing the usage of the database

    # Read in credentialing information
    for line in credentials_file.readlines():
        key, value = line.rstrip().split(':')
        credentials[key] = value

    connection = connectToDataBase(credentials)

    entire_data_base = getAllData(connection,
                                  "Lightning_Data",
                                  ["lightning_record"])

    connection.close()

    for key in entire_data_base.keys():
        stdout.write(f'{key}\n')
        for table in entire_data_base[key]:
            stdout.write(f'{table}\n')

if __name__ == "__main__":
    main()
