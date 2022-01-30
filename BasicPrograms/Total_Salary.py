# 2.Write a python program to calculate salary of an employee given
# his basic pay (to be entered by the user) HRA=10% of basic pay. TA=5% of basic
# pay. Define HRA and TA as constants and use them to calculate the salary of the
# employee.(10 MARKS)

from collections import namedtuple
Constants = namedtuple('Constants', ['HRA', 'TA'])
constants = Constants(0.1, 0.05)
basic_pay = float(input("Enter the basic pay : "))

total_salary = basic_pay + (basic_pay*constants.HRA) + (basic_pay*constants.TA)

print("The salary of the employee =",total_salary)
