'''
Created on Feb 24, 2013

@author: jsucsy
'''
#s = 'abc'

#print dir(s)
#print help(s.count)

fruits = ['apples', 'oranges', 'pears', 'bananas']
for fruit in fruits:
    print "%s for sale" % fruit

print map(lambda x: x * x, [1,2,3])
print filter(lambda x: x > 3, [1,2,3,4,5,4,3,2,1])

nums = [1,2,3,4,5,6]
plusOneNums = [x+1 for x in nums]
print plusOneNums
oddNums = [x for x in nums if x % 2 == 1]
print oddNums
oddNumsPlusOne = [x + 1 for x in nums if x % 2 ==1]
print oddNumsPlusOne

#exercise: write a list comprehension  which, from a list, 
#generates a lowercased version of each string that has length 
#greater than five
testStringList = ['A','BC','DEF','GHIJ','KLMNO','PQRSTUV','WXYZAAA123']
fivesLower = [x.lower() for x in testStringList if len(x) > 5]
print fivesLower