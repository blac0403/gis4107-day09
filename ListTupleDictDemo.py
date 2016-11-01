# File: ListTupleDict.py
# Author:
# Date:
# Purpose: Learn about Lists, Tuples and Dicts by creating functions
#          that deal with days of the week using these types.
#          NOTE:  For day numbers 1=Monday, ..., 7=Sunday

import sys
import inspect

listDays = ['Monday','Tuesday','Wednesday',
            'Thursday','Friday','Saturday','Sunday']
tupleDays = ('Monday','Tuesday','Wednesday',
            'Thursday','Friday','Saturday','Sunday')
dictDays = {1:'Monday', 2:'Tuesday', 3:'Wednesday',
            4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}


def main():
    test_getDayNameFromList()
##    test_getDayNameFromTuple()
##    test_getDayNameFromDict()
##    test_getDayNamesFromList()
##    test_getDayNamesFromTuple()
##    test_getDayNamesFromDict()
    print "\n%i of %i tests passed" % (testPassed, testCount)

def getDayNameFromList(dayNumber):
    return listDays[4]

def getDayNameFromTuple(dayNumber):
    pass

def getDayNameFromDict(dayNumber):
    pass

def getDayNamesFromList(firstDayNumber, lastDayNumber):
    return ['Wednesday', 'Thursday','Friday','Saturday']

def getDayNamesFromTuple(firstDayNumber, lastDayNumber):
    pass

def getDayNamesFromDict(firstDayNumber, lastDayNumber):
    # Create a list to which you will append day names
    #
    dayNames = []
    # Create a list of numbers from firstDayNumber to lastDayNumber
    ##    range(number) -> [0, ... number - 1]
    numbers = range(1,7)
    # Loop through the list of numbers
    #    Retrieve day name
    #    (i.e. Use the day number to get the day name from the dictionary
    ##   dayName = dictDays[dayNumber]
    #    Append each day name to the list of day names you want to return
    # Return this list of day names


    pass

# ------------------------------------------------------------------------------
# Tests setup
# ------------------------------------------------------------------------------
dayNumber = 2
firstDayNumber = 3
lastDayNumber = 6
testCount = 6
testPassed = 0
fmtPassed = "Passed: %s"
fmtFailed = "Failed: %s\n  Expected: %s\n  Actual: %s"

# ------------------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------------------
def test_getDayNameFromList():
    expect = 'Tuesday'
    actual = getDayNameFromList(dayNumber)
    funcName = inspect.stack()[0][3][5:]
    printTestResult(funcName,expect, actual)

def test_getDayNameFromTuple():
    expect = 'Tuesday'
    actual = getDayNameFromTuple(dayNumber)
    funcName = inspect.stack()[0][3][5:]
    printTestResult(funcName,expect, actual)

def test_getDayNameFromDict():
    expect = 'Tuesday'
    actual = getDayNameFromDict(dayNumber)
    funcName = inspect.stack()[0][3][5:]
    printTestResult(funcName,expect, actual)

def test_getDayNamesFromList():
    expect = ['Wednesday', 'Thursday', 'Friday', 'Saturday']
    actual = getDayNamesFromList(firstDayNumber, lastDayNumber)
    funcName = inspect.stack()[0][3][5:]
    printTestResult(funcName,expect, actual)

def test_getDayNamesFromTuple():
    expect = ['Wednesday', 'Thursday','Friday','Saturday']
    actual = getDayNamesFromTuple(firstDayNumber, lastDayNumber)
    funcName = inspect.stack()[0][3][5:]
    printTestResult(funcName,expect, actual)

def test_getDayNamesFromDict():
    expect = ['Wednesday', 'Thursday','Friday','Saturday']
    actual = getDayNamesFromDict(firstDayNumber, lastDayNumber)
    funcName = inspect.stack()[0][3][5:]
    printTestResult(funcName,expect, actual)

def printTestResult(funcName, expect, actual):
    global testPassed
    if actual == expect:
        print fmtPassed % funcName
        testPassed += 1
    else:
        print fmtFailed % (funcName, expect, actual)

if __name__ == '__main__':
    main()
