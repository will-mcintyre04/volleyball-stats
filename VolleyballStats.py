#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 19:10:29 2021

@author: williammcintyre
"""

# Volleyball Stats
# Will McIntyre
# Feb 4th, 2021

statsdata = ["S%", "H%", "PA"]
statsdatanames = ["Serving Percentage", "Hitting Percentage", "Passing Average"]

def checkvalidity(statchoice):
    validity = False
    for i in range (0, len(statsdata)):
        if statchoice == statsdata[i]:
            validity = True
            print("You have picked to determine your: "+ statsdatanames[i])
        elif statchoice == "?":
            printavailableoptions(statsdata)
            break
    return validity

def printavailableoptions(statsdata):
    for i in range (0, len(statsdata)):
        print("Enter '" + statsdata[i] + "' for " + statsdatanames[i],end = ". ")
                
def findanswer(statchoice):
    answer = 0
    if statchoice == "H%":
        answer = hittingpercentage()
    elif statchoice == "S%":
        answer = servepercentage()
    elif statchoice == "PA":
        answer = passingaverage()
    return answer

def hittingpercentage():
    userinput = splitbyspace(input("Please enter the data ('K' for kill, 'E' for error and 'C' for continuous... all seperated by space): "))
    datavalues = determinevalues(userinput)
    global kill
    kill = datavalues[0]
    global error
    error = datavalues[1]
    global total
    total = datavalues[2]
    answer = percentage(kill, error, total)
    return answer

def servepercentage():
    userinput = splitbyspace(input("Please enter the data ('A' for ace, 'E' for error and 'C' for continuous... all seperated by space): "))
    datavalues = determinevalues(userinput)
    global ace
    ace = datavalues[0]
    global error
    error = datavalues[1]
    global total
    total = datavalues[2]
    global continuous
    continuous = datavalues[3]
    answer = percentage(total, error, total)
    return answer

def determinevalues(userinput):
    userinput = userinput.upper()
    positive = 0
    negative = 0 
    continuous = 0
    total = 0
    for i in range(0, len(userinput)):
        if userinput[i] == "K" or userinput[i] == "A":
            positive = positive + 1
            total = total + 1
        elif userinput[i] == "E":
            negative = negative + 1
            total = total + 1
        elif userinput[i] == "C":
            continuous = continuous + 1
            total = total + 1
    return positive, negative, total, continuous

def passingaverage():
    userinput = splitbyspace(input("Please enter the data (3, 2, 1, 0 pass, all seperated by space): "))
    datavalues = turntointegers(userinput)
    answer = average(datavalues)
    return answer

def average(datavalues):
    answer = round((sum(datavalues) / len(datavalues)), 2)
    return answer
    
def turntointegers(userinput):
    integers = []
    for i in range (0, len(userinput)):
        integers.append(int(userinput[i]))
    return integers

def splitbyspace(data):
    splitdata = data.split()
    return splitdata

def percentage(positive, negative, total):
    percentage = round((((positive - negative) / total) * 100), 2)
    return percentage

def printanswer(answer, statchoice):
    if statchoice == statsdata[0]: # Serving Percentage
        print("Your", statsdatanames[0], "is:", answer, "%, with:", ace, "aces,", error, "errors,", continuous, "continuous, and", total, "total serves.")
    elif statchoice == statsdata[1]: # Hitting Percentage
        print("Your", statsdatanames[1], "is:", answer, "% with:", kill, "kills,", error, "errors,", continuous, "continuous and", total, "total swings.")
    elif statchoice == statsdata[2]: # Passing Average
        print("Your", statsdatanames[2], "is:", answer)
    




# Main Code
while(True):
    statchoice = input("\nWhat stat would you like? (Enter '?' to view choices): ")
    statchoice = statchoice.upper()
    statchoicevalidity = checkvalidity(statchoice)
    if statchoicevalidity == True:
        break
    if statchoicevalidity != True and statchoice != "?":
        print("This stat type is not valid. Please enter '?' next time to learn which stats this program finds.")
    
answer = findanswer(statchoice)
printanswer(answer, statchoice)
    

    

    
