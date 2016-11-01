import sys
import inspect

__fmtPassed = "Passed: {}"
__fmtFailed = "{}\n  Expected: {}\n  Actual  : {}"
__testPassed = 0
__testCount = 0

def main():
    test_getMissingKeys()
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

def getMissingKeysWithCount(dictRef, dictToCompare):

    return len(missing).append(getMissingKeys(dictRef, dictToCompare))


def test_getMissingKeys():
    # Test case 1
    expect = '[1,3]'
    actual = getMissingKeys({1:1, 2:2, 3:3}, {2:4})
    funcName = inspect.stack()[0][3][5:]
    printTestResult(funcName, expect, actual)

    print getMissingKeysWithCount({1:1, 2:2, 3:3}, {2:4})

def printTestResult(funcName, expect, actual):
    global __testPassed
    global __testCount
    __testCount += 1
    if actual == expect:
        print __fmtPassed % funcName
        __testPassed += 1
    else:
        print __fmtFailed.format(funcName, expect, actual)

if __name__ == '__main__':
    main()