# <Document_Header Start>
"""
filename    : CreateDatabase.py
author      : Adonay Pichardo
description : Python script to populate Thor database with schema and data.
"""
# <Document_Header End>

# <Standard Imports Start>
from sys import argv, stdout
# <Standard Imports End>

# <Internal Imports Start>
# <Internal Imports End>

# <External Imports Start>
import mysql.connector
# <External Imports End>

# <Global Objects Start>
# <Global Objects End>

# <Classes Start>
# <Classes End>

# <Functions Start>
################################
# Creates empty database with no schema or data
################################
def createDatabase(connection, database):
    try:
        cursor = connection.cursor()

        ################################
        # Create the database ONLY if it does NOT exist.
        # If the database already exists, STOP, contact all members and ensure that
        # you may delete it. This is meant to prevent anyone from just deleting/overwritting
        # a currently existing database
        ################################
        cursor.execute("CREATE DATABASE IF NOT EXISTS " + str(database))
        cursor.close()
        stdout.write("Created database " + str(database))

        # Return True if the database was created
        return True
    except Exception as error:
        stdout.write(f'ERROR:_> FROM:_> createDatabase():_> {error}\n')
        # Return False if the database was not created
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

################################
# Checks if CreateDatabase.py is being used correctly
################################
def checkCLI(argv):
    if len(argv) < 3:
            stdout.write(f'USAGE:_> python3 {argv[0]} <file used for credentials> <file used for ddl> <file with data>+\n\n')
            stdout.write(f'REQUIRED - a file used for credentials should look like:\n')
            stdout.write(f'host:###.###.###.###\n')
            stdout.write(f'user:string for the username\n')
            stdout.write(f'password:string for the password\n')
            stdout.write(f'database:string for the database name\n\n')
            stdout.write(f'REQUIRED - a file used for ddl should be in valid SQL.\n\n')
            stdout.write(f'REQUIRED - each file with data needs to be a csv file.\n')
            stdout.write(f'REQUIRED - One or more CSV file, must be the name of a table in the database\n')
            exit()

################################
# Creates connection to the database server with provided credentials
################################
def connectToDataBase(credentials):
    return mysql.connector.connect(host     = credentials['host'],
                                   user     = credentials['user'],
                                   password = credentials['password']
                                   )

def main():
    ################################
    # Verify the program has been called correctly
    ################################
    checkCLI(argv)

    ################################
    # Gather credential information
    ################################
    credentials_file = open(argv[1], 'r')
    credentials = {} # Used for authorizing the usage of the database

    # Read in credentialing information
    for line in credentials_file.readlines():
        key, value = line.rstrip().split(':')
        credentials[key] = value
    credentials['database'], _ = argv[2].split(".")

    ################################
    # Connect to the database and create a cursor to write to database
    ################################
    connection = connectToDataBase(credentials)
    cursor = connection.cursor()

    ################################
    # Create the database
    ################################
    createDatabase(connection, credentials['database'])

    ################################
    # Read in the Data Defining Language csv
    ################################
    cursor.execute(open('Thor.ddl', 'r').read(), multi = True)
    connection.commit()

    ################################
    # Open all CSV files passed in from Command Line Input
    ################################
    for every_csv_file in argv[2:]:
        csv_file = open(every_csv_file, 'r')
        all_insertions = '' # All insertions for a CSV file
    
        for line in csv_file.readlines():
            all_insertions += buildInsertStatement(every_csv_file, line) + "\n"

        # Close file after reading it
        every_csv_file.close()

        ################################
        # Send all INSERT statements for current CSV file
        ################################
        cursor.execute(all_insertions, multi = True)

        ################################
        # Commit changes
        ################################
        cursor.commit()

    ################################
    # Close connection
    ################################
    connection.close()

    ################################
    # Close cursor
    ################################
    cursor.close()

# <Functions End>

if __name__ == "__main__":
    main()
