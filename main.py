# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
# Output:       Valid date is printed or user is alerted that an invalid date was entered.

# Change MIN_YEAR = 0 to 1935 to make years below invalid
validDate = True
MIN_YEAR = 1935
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

year = None
month = None
day = None

# Get the year, then the month, then the day
# housekeeping()
# PROMPT user to enter month, day, and year
# STORE the input in the variable month, day, and year
month = input("month = ")
day = input("day = ")
year = input("year = ")

# Check to be sure date is valid

if int(year) <= MIN_YEAR: # invalid year
    validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
    validDate = False
elif int(day) < MIN_DAY or int(day) > MAX_DAY: # invalid day
    validDate = False

# Test to see if date is valid and output date and whether it is valid or not

# endOfJob()
if validDate == True:
    # Output statement
    print(str(month) + "/" + str(day) + "/" + str(year) + " is a valid date")
else:
    # Output statement
    print(str(month) + "/" + str(day) + "/" + str(year) + " is an invalid date")