import sys
import inspect

__fmtPassed = "Passed: {}"
__fmtFailed = "{}\n  Expected: {}\n  Actual  : {}"
__testPassed = 0
__testCount = 0

def main():
    test_func1()
    print "\n%i of %i tests passed" % (__testPassed, __testCount)
    help(__name__)

def func1(params):
    """Function documentation:
       - What does function do?
       - What is/are expected parameter value(s)?
       - What does function return, if anything
       - Example usage"""
    pass

def func2(params):
    pass

def test_func1():
    # Test case 1
    expect = ''
    actual = func1(0)
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