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

def statchoiceasanumber(statchoice):
    for i in range(0, len(statsdata)):
        if statchoice == statsdata[i]:
            statnumber = i
    return statnumber

def percentage(positive, negative, continuous):
    percentage = ((positive - negative) / continuous) * 100
    return percentage

def splitbyspace(data):
    splitdata = data.split()
    return splitdata

def statpercentage(userinput):
    positive = 0
    negative = 0
    continuous = 0
    for i in range(0, len(userinput)):
        if userinput.upper()[i] == "A" or userinput.upper() == "K":
            positive = positive + 1
        elif userinput.upper()[i] == "E":
            negative = negative + 1
        elif userinput.upper()[i] == "C":
            continuous = continuous + 1
    answer = percentage(positive, negative, continuous)
    return answer

def printdata(percentage):
    print(percentage)

# Main Code
while(True):
    statchoice = checkvalidity(input("What stat would you like? (Enter '?' to view choices): "))
    if statchoice == True:
        break
    
statsnumber = statchoiceasanumber(statchoice)
answer = statpercentage(splitbyspace(input("Please enter the data ('A' for ace, 'K' for kill, 'E' for error and 'C' for continuous... all seperated by space): ")))
printdata(answer)
    

    

    
