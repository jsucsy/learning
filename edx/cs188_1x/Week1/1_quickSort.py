'''
Created on Feb 24, 2013

@author: jsucsy
'''


def quickSort(lst):
    if len(lst) <= 1:
        return lst
    smaller = [x for x in lst[1:] if x < lst[0]]
    larger = [x for x in lst[1:] if x >= lst[0]]
    
    return quickSort(smaller) + [lst[0]] + quickSort(larger)
    

if __name__ == '__main__':
    nums = [2,3,5,1,6]
    print quickSort(nums)