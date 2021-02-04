#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:08:54 2021

@author: davidmcintyre
"""

# This program determines how many days you are into the year
# February 1st, 2021
# Will McIntyre

# Split user input by month and day
def splitdate(date):
    splitdate = date.split()
    return splitdate

# Check date validity
def checkdate(date, months, dayspermonth):
    validity = False
    month = date[0]
    for i in range (0, len(months)):
        if month.upper() == months[i] and (int(date[1]) <= dayspermonth[i] and int(date[1]) > 0):
            validity = True
    return validity

# Convert user input of month into a number (January is 1, etc)
def monthnumber(date):
    month = date[0]
    numbermonth = 0
    for i in range (0, 12):
        if month.upper() == months[i] or month.upper() == months[i + 12]:
            numbermonth = i + 1
    return(numbermonth)    

# Add up all days that have occured in the prior months
def daystomonth(monthnumber, daysinmonth):
    dayssofar = 0
    for i in range (0, monthnumber - 1):
        dayssofar = dayssofar + daysinmonth[i]
    return(dayssofar)

# Determine total days into year, adding prior days and days into month
def totaldays(dayssofar, updateddate):
    total = dayssofar + int(updateddate[1])
    return total      

# Main Logic
months = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER", "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
dayspermonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while(True):
    date = splitdate(input("Please enter a date: "))
    validityofdate = checkdate(date, months, dayspermonth)
    if validityofdate == True:
        break
    else:
        print("This date is not valid, please try again")

monthasnumber = monthnumber(date)
daysprior = daystomonth(monthasnumber, dayspermonth)
totaldays = totaldays(daysprior, date)
print("You are: ", totaldays, "days into the year")

    