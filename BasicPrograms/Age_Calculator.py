# 3. Write a python program that accepts that current date and the date of birth of the user then 
# calculate the age of the user and display it on the screen, note that the date should be display 
# in the format specified as dd/mm/yyyy. (6MARKS)

from datetime import date, datetime
 
def calculateAge(born):
    today = date.today()
    try:
        birthday = born.replace(year = today.year)
 
    # raised when birth date is February 29
    # and the current year is not a leap year
    except ValueError:
        birthday = born.replace(year = today.year,
                  month = born.month + 1, day = 1)
 
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year
         
dob = datetime.strptime(input("Enter Date of birth (dd/mm/yyyy) :"), "%d/%m/%Y").date()
print(type(dob))
print("Age is ",calculateAge(dob), "years")