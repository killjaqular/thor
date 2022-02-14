# <Document_Header Start>
"""
filename : getDatabase.py
author : Adonay Pichardo
description :
"Given a string, creates an MD5 hash."
"""
# <Document_Header End>

# <Standard Imports Start>
# List all imports alphabetically for Python3 standard libraries
from sys import argv, stdout, stdin
# <Standard Imports End>


# <Internal Imports Start>
# List all imports alphabetically for libraries authored for Thor
# NONE
# <Internal Imports End>

# <External Imports Start>
# List all imports alphabetically for libraries NOT authored for Thor
# NONE
# <External Imports End>

# <Global Objects Start>
# NONE
# <Global Objects End>

# <Classes Start>
# NONE
# <Classes End>

# <Functions Start>
################################
# Checks if getDatabase.py is being used correctly
################################
def checkCLI(argv):
    if len(argv) < 1:
            stdout.write(f'USAGE:_> python3 {argv[0]} <some string to hash>\n')
            stdout.write(f'REQUIRED - a string to create a hash.\n')
            exit()

################################
# Checks if MD5hash.py is being used correctly
################################
def createMD5hash(key):
    from hashlib import md5
    return md5(key.encode("utf-8")).hexdigest()
# <Functions End>

def main():
    ################################
    # Verify the program has been called correctly
    ################################
    checkCLI(argv)

    ################################
    # Create the MD5 hash for every key given
    ################################
    while (1):
        key = stdin.readline().rstrip()
        if len(key) == 0:
            break
        stdout.write(f'{createMD5hash(key)}\n')

if __name__ == "__main__":
    main()
