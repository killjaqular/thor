# <Document_Header Start>
"""
filename : ASCII_to_csv.py # name of this file
author : Adonay Pichardo # name of original engineer
date : 03-OCT-2021 # date of original commit

description :
Used to automate conversion of ASCII file to a CSV
"""
# <Document_Header End>

# <Standard Imports Start>
# List all imports alphabetically for Python3 standard libraries
from sys import argv, stdout
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
def main():
    if len(argv) != 3:
        stdout.write(f'USAGE: python3 ASCII_to_cvs.py <path\\of\\target\\file.txt> <path\\to\\save\\file.csv>\n')
        exit()

    try:
        ascii_file = open(argv[1], 'r')
        csv_file   = open(argv[2] + '.csv', 'w+')

        csv_file.write(ascii_file.read().replace('\t', ','))

        csv_file.close()
        ascii_file.close()
    except Error as error:
        stdout.write(f'ERROR:_> {error}\n')

# <Functions End>

if __name__ == "__main__":
    main()
