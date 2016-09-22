# -*- coding:utf-8 -*- 
'''
Created on 2016-9-20
ThoughtWorks HomeWork 2017-chengdu
== Code party ==
@author: young
'''

import time

global lastDateTime,animalDict
lastDateTime = ''
animalDict = {}

def isDate(string):
    try:
        time.strptime(string, "%Y/%m/%d %H:%M:%S")
        return True
    except:
        return False

def isID(string):
    if ' ' not in string:
        return True
    else:
        return False

def isAnimal(string):
    dataSplit = string.split(' ')
    if len(dataSplit) == 3:
        try:
            int(dataSplit[1])
            int(dataSplit[2])
            return True
        except ValueError:
            return False
    elif len(dataSplit) == 5:
        try:
            int(dataSplit[1])
            int(dataSplit[2])
            int(dataSplit[3])
            int(dataSplit[4])
            return True
        except ValueError:
            return False
    else:
        return False
    
def isAnimalDataRight(line):
    """old: compare and update    new: add
    """
    dataSplit = line.split(' ')
    if len(dataSplit) == 3:
        if dataSplit[0] not in animalDict:
            animalDict[dataSplit[0]] = [int(dataSplit[1]), int(dataSplit[2]), time.mktime(time.strptime(lastDateTime, "%Y/%m/%d %H:%M:%S"))]
            return True
    elif len(dataSplit) == 5:
        if dataSplit[0] in animalDict:
            if int(dataSplit[1]) == animalDict[dataSplit[0]][0] and int(dataSplit[2]) == animalDict[dataSplit[0]][1]:
                animalDict[dataSplit[0]][0] = int(dataSplit[1])+int(dataSplit[3])
                animalDict[dataSplit[0]][1] = int(dataSplit[2])+int(dataSplit[4])
                return True
    return False

def isDateOrderRight(line):
    global lastDateTime
    if lastDateTime == '':
        lastDateTime = line
        return True
    elif time.mktime(time.strptime(line, "%Y/%m/%d %H:%M:%S"))- \
        time.mktime(time.strptime(lastDateTime, "%Y/%m/%d %H:%M:%S"))>0:
        lastDateTime = line
        return True
    else:
        return False

def getFinalPos(string):
    """ get animals and their positions match the ID input,
        and set their flag to 0, cuz 0 always less than other 'mktime'
    """
    a = string.split(" ")
    if len(a) == 3:
        animalDict[a[0]][0] = int(a[1])
        animalDict[a[0]][1] = int(a[2])
        animalDict[a[0]][2] = 0
    elif len(a) == 5:
        animalDict[a[0]][0] = int(a[1])+int(a[3])
        animalDict[a[0]][1] = int(a[2])+int(a[4])
        animalDict[a[0]][2] = 0
    
def sortAnimal(stime):
    """ sort animalDict, and traverse it, print the animals info with
        whose flag are 0.
        If their exist flag(time) less than input argument and unequal
        to 0, recalculate that animal's position by 'getTimePos'
    """
    sorted(animalDict, None, None, False)
    for i in animalDict:
        if stime>=animalDict[i][2]:
            if animalDict[i][2] != 0:
                getTimePos(i, animalDict[i][2])
            print i, animalDict[i][0], animalDict[i][1]
        
def getTimePos(animal, stime):
    """ find the first position and add the change till given time.
    """
    foundFlag = False
    firstFlag = False
    for line in historyData.split('\n'):
        line = line.strip()
        if not isDate(line) and foundFlag==False:
            continue
        if isDate(line):
            foundFlag=True
            nowDate =line
            sNowDate = time.mktime(time.strptime(nowDate, "%Y/%m/%d %H:%M:%S"))
        if sNowDate<animalDict[animal][2]:
            continue
        if sNowDate>stime:
            break
        if animal in line:
            target = line.split(" ")
            if firstFlag == False:
                animalDict[animal][0] = int(target[1])
                animalDict[animal][1] = int(target[2])
                firstFlag = True
            else:
                animalDict[animal][0] += int(target[3])
                animalDict[animal][1] += int(target[4])


def findID(historyData, id):
    foundFlag = False
    for line in historyData.split('\n'):
        line = line.strip()
        if line != id and foundFlag == False:
            continue
        foundFlag = True
        if line == id:
            continue
        if isDate(line):
            selectTime = time.mktime(time.strptime(line, "%Y/%m/%d %H:%M:%S"))
            continue
        if not ' ' in line:  #break when hit the next id
            break
        getFinalPos(line)
    sortAnimal(selectTime)
    
def input():
    global animalDict, historyData
    stopWord     = ''
    historyData  = ''
    lastID       = ''
    dataFlag = 0        #0:id and animal    1:datetime    2:animal only
    for line in iter(raw_input, stopWord):
        if dataFlag == 0:
            if isAnimal(line) and historyData == '':    #first line
                print  "Invalid format."
                return -1
            if not isAnimal(line):                      #id
                if not isID(line):
                    print  "Invalid format."
                    return -1
                lastID       = line
                historyData += lastID+'\n'
                dataFlag = 1
                continue
            if not isAnimalDataRight(line):             #animal
                print "Conflict found at", lastID
                return -2
            historyData += line+'\n'
        elif dataFlag == 1:
            if not isDate(line):
                print  "Invalid format."
                return -1
            if not isDateOrderRight(line):              #datetime
                print "Conflict found at", lastID
                return -2
            historyData += line+'\n'
            dataFlag = 2
        elif dataFlag == 2:
            if not isAnimal(line):                      #animal
                print  "Invalid format."
                return -1
            if not isAnimalDataRight(line):
                print "Conflict found at", lastID
                return -2
            historyData += line+'\n'
            dataFlag = 0
    if dataFlag !=0:                                    #last line must be animal data
        print  "Invalid format."
        return -1
        
    id = raw_input()
    while (id) == '':
        id = raw_input()
    if isID(id):
        findID(historyData, id)
    else:
        print  "Invalid format."
        return -1
    return 0
    
if __name__ == "__main__":
    input()
    
