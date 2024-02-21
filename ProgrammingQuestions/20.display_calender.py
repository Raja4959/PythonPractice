import calendar
# 1. Display Calendar of a Specific Month and Year:


def display_calendar(year, month):
    cal = calendar.month(year, month)
    print(f"Calendar for {calendar.month_name[month]} {year}:\n")
    print(cal)


# 2. Determine if a Given Year is a Leap Year:
def is_leap_year(year):
    return calendar.isleap(year)


# 3. Find the Day of the Week for a Given Date:
def day_of_week(year, month, day):
    day_index = calendar.weekday(year, month, day)
    return calendar.day_name[day_index]


# 4. Display a Whole Year's Calendar:
def display_year_calendar(year):
    cal = calendar.TextCalendar()
    year_calendar = cal.formatyear(year)
    print(f"Calendar for the year {year}:\n")
    print(year_calendar)


# 1.Example usage:
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
display_calendar(year, month)


# 2.Example usage:
year = int(input("Enter the year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 3.Example usage:
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day: "))
weekday = day_of_week(year, month, day)
print(f"The day of the week for {month}/{day}/{year} is {weekday}.")

# 4.Example usage:
year = int(input("Enter the year: "))
display_year_calendar(year)
