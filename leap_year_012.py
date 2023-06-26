# Python Program to Check Leap Year
year = int(input("Enter any year:"))

if year % 400 ==0 or year % 100 != 0 and year % 4 == 0:
    print("IT'S LEAP YEAR")
else:
    print("IT'S NOT  A LEAP YEAR")
