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
            animalDict[dataSplit[0]] = [int(dataSplit[1]), int(dataSplit[2]), True]
            return True
    elif len(dataSplit) == 5:
        if dataSplit[0] in animalDict:
            if int(dataSplit[1]) == animalDict[dataSplit[0]][0] and int(dataSplit[2]) == animalDict[dataSplit[0]][1]:
                animalDict[dataSplit[0]] = [int(dataSplit[1])+int(dataSplit[3]), int(dataSplit[2])+int(dataSplit[4]), True]
                return True
    return False

def delFalseAnimal(animalDict):
    finishDelDict = {}
    for item in animalDict:
        if  animalDict[item][2] == True:
            animalDict[item][2] = False
            finishDelDict[item] = animalDict[item]
    return finishDelDict
    ''' solve 2:      del animalDict[item] while animalDict[item][2] == False, 
        insufficient: sometimes raise RuntimeError: dictionary changed size during iteration
    '''

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
        animalDict[a[0]] = [int(a[1]), int(a[2])]
    elif len(a) == 5:    #even 5, animals still can run out of range
        animalDict[a[0]] = [int(a[1])+int(a[3]), int(a[2])+int(a[4])]
    
def sortAnimal():
    sorted(animalDict, None, None, False)
    for i in animalDict:
        print i, animalDict[i][0], animalDict[i][1]
        
def findID(historyData, id):
    '''select animal belong to id input
    '''
    foundFlag = False
    animalDict.clear()
    for line in historyData.split('\n'):
        line = line.strip()
        if line != id and foundFlag == False:
            continue
        foundFlag = True
        if line == id or isDate(line):
            continue
        if not ' ' in line:  #break when hit the next id
            break
        getFinalPos(line)
    sortAnimal()
    
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
                animalDict   = delFalseAnimal(animalDict)
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
    id = raw_input()
    while (id) == '':
        id = raw_input()
    findID(historyData, id)
    return 0

if __name__ == "__main__":
    input()
