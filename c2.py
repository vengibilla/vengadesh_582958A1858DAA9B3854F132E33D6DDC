#Variable definition and assignment
year = 2024

#Remove comments from the bottom line to take input from the user
#year = int(input("Enter a year: "))

#It is a centenary year if the value is divisible by 100 with no remainder.
#Centenary year is a leap year divided by 400
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

#If it is not divisible by 100 then it is not a centenary year
#A year divisible by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year.".format(year))

#If the Year is not divisible by both 400 (centenary year) and 4 (centenary year) then:
#The Year is not a leap year
else:
    print("{0} is not a leap year.".format(year))

