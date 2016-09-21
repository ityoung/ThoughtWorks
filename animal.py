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
    """old: compare    new: format
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
    a = string.split(" ")
    if len(a) == 3:
        animalDict[a[0]][0] = int(a[1])
        animalDict[a[0]][1] = int(a[2])
    elif len(a) == 5:    #even 5, animals still can run out of range
        animalDict[a[0]][0] = int(a[1])+int(a[3])
        animalDict[a[0]][1] = int(a[2])+int(a[4])
    
def sortAnimal(stime):
    sorted(animalDict, None, None, False)
    for i in animalDict:
        if stime<animalDict[i][2]:
            continue
        print i, animalDict[i][0], animalDict[i][1]
        
    '''select animal belong to id input
    '''
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
    global animalDict
    stopWord     = ''
    historyData  = ''
    lastID       = ''
    nextDateFlag = False        #0:id and animal    1:datetime
    for line in iter(raw_input, stopWord):
        if nextDateFlag == False:
            if isAnimal(line) and historyData == '':
                print  "Invalid format."
                return -1
            if not isAnimal(line):
                if not isID(line):
                    print  "Invalid format."
                    return -1
                lastID       = line
                historyData += lastID+'\n'
                nextDateFlag = True
                continue
            if not isAnimalDataRight(line):
                print "Conflict found at", lastID
                return -2
            historyData += line+'\n'
        elif nextDateFlag == True:
            if not isDate(line):
                print  "Invalid format."
                return -1
            if not isDateOrderRight(line):
                print "Conflict found at", lastID
                return -2
            historyData += line+'\n'
            nextDateFlag = False
    print animalDict
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
