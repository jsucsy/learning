'''
Created on May 22, 2013

@author: JSU
'''

import numpy as np


def word_to_int(word):
    result = 1
    intdict = {'A':1,'B':2,'C':3,'D':4,'E':5,
               'F':6,'G':7,'H':8,'I':9,'J':10,
               'K':11,'L':12,'M':13,'N':14,'O':15,
               'P':16,'Q':17,'R':18,'S':19,'T':20,
               'U':21,'V':22,'W':23,'X':24,'Y':25,
               'Z':26}
    for char in word:
        result *= intdict[char.upper()]
        
    print result




def generate_random(quantity):
    '''generate quantity number of random integers'''
    results = np.random.random_integers(1,100,quantity)
    print results
    print sorted(results)


def print_sorted_results(values):
    print sorted(values)

def get_raw_input():
    '''get list of numbers from std input'''
    #values = [float(x) for x in raw_input("Enter numbers separated by ,: ").split(",")]    #method 1
    values = map(float, raw_input("Enter numbers separated by ,: ").split(","))             #method 2
    return values    

if __name__ == '__main__':
    
    generate_random(100)
    
    word_to_int('dog')
    word_to_int('cat')
    word_to_int('afathippos')
    #values = get_raw_input()
    #print_sorted_results(values)