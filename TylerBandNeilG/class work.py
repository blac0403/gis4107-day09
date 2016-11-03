#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Neil
#
# Created:     01-11-2016
# Copyright:   (c) Neil 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def getMissingKeys(dictRef,dictToCompare):
    missing = []
    for item in dictRef.keys():
        if dictToCompare.has_key(item) is False:
            missing.append(item)
    return missing



def getMissingKeysWithCount(dictRef,dictToCompare):
    keys = getMissingKeys(dictRef,dictToCompare)
    keyLength = len(keys)
    return keyLength, keys


def test_getMissingKeysWithCount():
    print getMissingKeysWithCount({1:1,2:2,3:3}, {2:2})

test_getMissingKeysWithCount()

def getUnique(inList):
    uniqueList = []
    for unique in inList:
        if unique in uniqueList:
            continue
        else:
            uniqueList.append(unique)
    return uniqueList

def test_getUnique():
    print getUnique([1,2,2,3,3,4,5])

test_getUnique()


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

def test_getUnique():
    print flattenList([1,(2,3),4,[5,6]])

test_getUnique()

