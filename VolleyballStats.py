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
            printavailableoptions(statsdata)
            break
    return validity

def printavailableoptions(statsdata):
    for i in range (0, len(statsdata)):
                print("Enter '", statsdata[i], "' for", statsdatanames[i], end = ". ")

def determinepositivenegativetotal(userinput):
    positive = 0
    negative = 0 
    total = 0
    for i in range(0, len(userinput)):
        if userinput[i].upper() == "K" or userinput[i].upper() == "A":
            positive = positive + 1
            total = total + 1
        elif userinput[i].upper() == "E":
            negative = negative + 1
            total = total + 1
        elif userinput[i].upper() == "C":
            total = total + 1
    return positive, negative, total

def hittingpercentage():
    userinput = splitbyspace(input("Please enter the data ('K' for kill, 'E' for error and 'C' for continuous... all seperated by space): "))
    positivenegativetotal = determinepositivenegativetotal(userinput)
    positive = positivenegativetotal[0]
    negative = positivenegativetotal[1]
    total = positivenegativetotal[2]
    answer = percentage(positive, negative, total)
    return answer

def servepercentage():
    userinput = splitbyspace(input("Please enter the data ('A' for ace, 'E' for error and 'C' for continuous... all seperated by space): "))
    positivenegativetotal = determinepositivenegativetotal(userinput)
    total = positivenegativetotal[2]
    negative = positivenegativetotal[1]
    answer = percentage(total, negative, total)
    return answer

def splitbyspace(data):
    splitdata = data.split()
    return splitdata

def percentage(positive, negative, total):
    percentage = ((positive - negative) / total) * 100
    return percentage

def findanswer(statchoice):
    answer = 0
    if statchoice == "H%":
        answer = hittingpercentage()
    elif statchoice == "S%":
        answer = servepercentage()
    return answer

def printanswer(percentage):
    print(percentage, "%")

# Main Code
while(True):
    statchoice = input("\nWhat stat would you like? (Enter '?' to view choices): ")
    statchoicevalidity = checkvalidity(statchoice)
    if statchoicevalidity == True:
        break
    
answer = findanswer(statchoice)
printanswer(answer)
    

    

    
