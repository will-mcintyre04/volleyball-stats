#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 19:10:29 2021

@author: williammcintyre
"""

# Volleyball Stats
# Will McIntyre
# Feb 4th, 2021

statsdata = ["S%", "H%"]
statsdatanames = ["Serving Percentage", "Hitting Percentage"]

def checkvalidity(statchoice):
    validity = False
    for i in range (0, len(statsdata)):
        if statchoice.upper() == statsdata[i]:
            validity = True
            print("You have picked to determine your: ", statsdatanames[i])
        elif statchoice == "?":
            print("Enter 'S%' for serve percentage, and 'H%' for hitting percentage.")
            break
    return validity

def percentage(positive, negative, total):
    percentage = ((positive - negative) / total) * 100
    return percentage

def splitbyspace(data):
    splitdata = data.split()
    return splitdata

def statpercentage(userinput):
    positive = 0
    negative = 0 
    total = 0
    for i in range(0, len(userinput)):
        if userinput[i].upper() == "A" or userinput[i].upper() == "K":
            positive = positive + 1
            total = total + 1
        elif userinput[i].upper() == "E":
            negative = negative + 1
            total = total + 1
        elif userinput[i].upper() == "C":
            total = total + 1
    answer = percentage(positive, negative, total)
    return answer

def printdata(percentage):
    print(percentage, "%")

# Main Code
while(True):
    statchoice = checkvalidity(input("What stat would you like? (Enter '?' to view choices): "))
    if statchoice == True:
        break
    
answer = statpercentage(splitbyspace(input("Please enter the data ('A' for ace, 'K' for kill, 'E' for error and 'C' for continuous... all seperated by space): ")))
printdata(answer)
    

    

    
