import os
import sys
import time
import itertools
from os import system, name    

def clear(): 
    if name == 'nt': 
        _ = system('cls')   
    else: 
        _ = system('clear')

def divisibleSumPairs(divisor, numbers):
    countOfPairs = 0
    iterator = 1
    for outerNumber in numbers:
        for innerNumber in itertools.islice(numbers,iterator,len(numbers)):
            if ((outerNumber + innerNumber)%divisor==0):
                countOfPairs+=1
        iterator+=1
    return(countOfPairs) 

print(r"""

      _,,ddF```Ybb,,_
    ,d@#@#@#@g,   ``Yb,
  ,d#@#V``V@#@#b      `b,
 d@#@#I    I@#@8        `b
d@#@#@#A..A@#@#P         `b
8#@#@#@#@#@#@8`           8
8@#@#@#@#@#@J             8
8#@#@#@#@#P               8
Y@#@#@#@#P    ,db,       ,P
 Y@#@#@#@)    @DWB      aP
  `Y#@#@#b    `69`    aP`
    `Y@#@#g,,     _,dP`
      ```YBBgggddP```

Challenge: Divisible Sum Pairs

ASCII Artist: Donovan Bake @ https://www.asciiart.eu/
      
  """)

time.sleep(5)
clear() 
time.sleep(2)

divisor = int(input("Input the divisor: "))

numbers = list(map(int, input("\nInput the list of numbers with a space in between each: ").rstrip().split()))

result = divisibleSumPairs(divisor, numbers)

print("\nThere are " + str(result) + " divisible pairs.\n")

time.sleep(10)