import datetime

print("Please enter your birthday to calculate age")
birth_day = int(input("day of birth: "))
birth_month = int(input("month of birth: "))
birth_year = int(input("year of birth: ")) 

current_day = datetime.date.today().day
current_month = datetime.date.today().month
current_year = datetime.date.today().year

age_year = current_year - birth_year
age_month = abs(current_month - birth_month)
age_day = abs(current_day - birth_day)

print("Your age is exactly:", age_year, "years", age_month, "months and", age_day, "days." )

                                                          