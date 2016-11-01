import sys
import inspect

__fmtPassed = "Passed: {}"
__fmtFailed = "{}\n  Expected: {}\n  Actual  : {}"
__testPassed = 0
__testCount = 0

def main():
    test_getMissingKeys()
    print "\n%i of %i tests passed" % (__testPassed, __testCount)
    help(__name__)

def getMissingKeys(dictRef, dictToCompare):
    missing = []
    for keys in dictRef:
        if dictToCompare.has_key == False:
            missing.extend()
    return missing

def func2(params):
    pass

def test_getMissingKeys():
    # Test case 1
    expect = '[1,3]'
    actual = getMissingKeys({1:1, 2:2, 3:3}, {2:2})
    funcName = inspect.stack()[0][3][5:]
    printTestResult(funcName, expect, actual)

    # Test case 2 ...

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