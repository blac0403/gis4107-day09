import sys
import inspect

__fmtPassed = "Passed: {}"
__fmtFailed = "{}\n  Expected: {}\n  Actual  : {}"
__testPassed = 0
__testCount = 0

def main():
    test_getMissingKeys()
    test_getMissingKeysWithCount()
    test_getUnique()
    test_flattenList()
    print "\n%i of %i tests passed" % (__testPassed, __testCount)
    # If you uncomment the following help statement, help for this module will be
    # output to the interpreter console.  You will notice the variables prefixed
    # with double underscores are not displayed.  Prefixing variables and
    # functions with double underscores "hides" them from global scope.
    #
    #help(__name__)

def getMissingKeys(dictRef, dictToCompare):
    missing =[]
    for item in dictRef.keys():
        if dictToCompare.has_key(item) is False:
            missing.append(item)
    return missing

def getMissingKeysWithCount(dictRef,dictToCompare):
    keys = getMissingKeys(dictRef,dictToCompare)
    keyLength = len(keys)
    return keyLength, keys

def getUnique(inList):
    uniqueList = []
    for unique in inList:
        if unique in uniqueList:
            continue
        else:
            uniqueList.append(unique)
    return uniqueList

def flattenList(inList):
    flatList = []
    for instance in inList:
        if type(instance) == tuple:
            list(instance)
            for newInstance in instance:
                flatList.append(newInstance)
        if type(instance) == list:
            for newInstance in instance:
                flatList.append(newInstance)

        if type(instance) != list and type(instance) != tuple:
            flatList.append(instance)
    return flatList

##Fucntion Tests

def test_getMissingKeys():
    # Test case 1
    expect = [1, 3]
    actual = getMissingKeys({1:1, 2:2, 3:3}, {2:4})
    funcName = inspect.stack()[0][3][5:]
    printTestResult(funcName, expect, actual)

def test_getMissingKeysWithCount():
    # Test Case 2
    expect = (2, [1, 3])
    actual = getMissingKeysWithCount({1:1,2:2,3:3}, {2:2})
    funcName = inspect.stack()[0][3][5:]
    printTestResult(funcName, expect, actual)

def test_getUnique():
    # Test Case 3
    expect = [1, 2, 3, 4, 5]
    actual = getUnique([1,2,2,3,3,4,5])
    funcName = inspect.stack()[0][3][5:]
    printTestResult(funcName, expect, actual)

def test_flattenList():
    # Test Case 4
   expect = '[1, 2, 3, 4, 5, 6]'
    expect = [1, 2, 3, 4, 5, 6]
    actual = flattenList([1,(2,3),4,[5,6]])
    funcName = inspect.stack()[0][3][5:]
    printTestResult(funcName, expect, actual)


def printTestResult(funcName, expect, actual):
    global __testPassed
    global __testCount
    __testCount += 1
    if actual == expect:
        print __fmtPassed.format(funcName)
        __testPassed += 1
    else:
        print __fmtFailed.format(funcName, expect, actual)

if __name__ == '__main__':
    main()