# <Document_Header Start>
"""
filename    : CreateDatabase.py
author      : Adonay Pichardo
description : Python script to populate Thor database with schema.
"""
# <Document_Header End>

# <Standard Imports Start>
from sys import argv, stdin, stdout
# <Standard Imports End>

# <Internal Imports Start>
# <Internal Imports End>

# <External Imports Start>
import mysql.connector
# <External Imports End>

# <Global Objects Start>
credentials = {}
# <Global Objects End>

# <Classes Start>
# <Classes End>

# <Functions Start>
################################
# Creates database
################################
def createDatabase(connection, database):
    try:
        cursor = connection.cursor()

        ################################
        # Create the database ONLY if it does not exist.
        # If the database already exists, STOP, contact all members and ensure that
        # you may delete it. This is meant to prevent anyone from just deleting/overwritting
        # a currently existing database
        ################################
        cursor.execute("CREATE DATABASE IF NOT EXISTS " + str(database))
        cursor.close()
        connection.close()
        print("Created database " + str(database))

        # Return True if the database was created
        return True
    except Exception as error:
        stdout.write(f'ERROR:_> FROM:_> createDatabase():_> {error}\n')
        # Return False if the database was created
        return False

################################
# Parses input to create an INSERT MySQL statement
################################
def buildInsertStatement(given_table, given_record):
    formatted_record = "" # Empty string that is built up to the SQL statement
    list_of_values   = given_record.split(',') # Record to be inserted

    # Format every value as a string or integer accordingly
    for index, value in enumerate(list_of_values):
        # Check if value is a digit, positive or negative
        if value.isdigit() or (value[0] == '-' and value[1:].isdigit()):
            formatted_record += str(value)
        else:
            formatted_record += f"'{value}'"
        # If we have not inserted the last value
        if index + 1 != len(list_of_values):
            # Insert a comma delimiter
            formatted_record += ','

    complete_sql_statement = given_table + "(" + formatted_record + ");"
    stdout.write(f'{complete_sql_statement}\n')
    return complete_sql_statement

def main():
    ################################
    # 1. Verify the program has been given all required arguments
    ################################
    if len(argv) != 2:
        stdout.write(f'USAGE:_> python3 {argv[0]} <file used for credentials>\n')
        stdout.write(f'file used for credentials should look like:\n')
        stdout.write(f'host    :###.###.###.###\n')
        stdout.write(f'user    :string for the username\n')
        stdout.write(f'password:string for the password\n')
        stdout.write(f'database:string for the database name\n')
        exit()

    ################################
    # 2. Gather credential information
    ################################
    credentials_file = open(argv[1], 'r')

    for line in credentials_file.readlines():
        key, value = line.rstrip().split(':')
        credentials[key] = value

    ################################
    # 3. Connect to the database and create a cursor to write to database
    ################################
    connection = mysql.connector.connect(host = credentials['host'],
                                         user = credentials['user'],
                                         password = credentials['password'],
                                         database = credentials['database']
                                         )
    cursor = connection.cursor()

    ################################
    # 4. Create the database
    ################################
    createDatabase(connection, credentials['database'])

    ################################
    # 5. Read in the csv
    ################################
    csv_data = open('Thor.ddl', 'r')

    ################################
    # 6. Create schema
    ################################
    csv_data = csv_data.read()
    cursor.execute(str(ddl_statement), multi = True)

    ################################
    # 7. Create individual SQL INSERT statements
    ################################
    for line in csv_data.readlines():
        buildInsertStatement(line)

    ################################
    # 8. Concatinate all INSERT statements
    ################################

    ################################
    # 9. Send all INSERT statements
    ################################

    ################################
    # 10. Commit changes
    ################################

    ################################
    # 11. Close connection
    ################################

    ################################
    # 12. Close cursor
    ################################

# <Functions End>

if __name__ == "__main__":
    main()
