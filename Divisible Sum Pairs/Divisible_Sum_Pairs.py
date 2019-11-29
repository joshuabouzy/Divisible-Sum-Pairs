import itertools

def divisibleSumPairs(divisor, numbers):
    countOfPairs = 0
    iterator = 1
    for outerNumber in numbers:
        for innerNumber in itertools.islice(numbers,iterator,len(numbers)):
            if ((outerNumber + innerNumber)%divisor==0):
                countOfPairs+=1
        iterator+=1
    return(countOfPairs) 

divisor = int(input("Input the divisor: "))

numbers = list(map(int, input("Input the list of numbers with a space in between each: ").rstrip().split()))

result = divisibleSumPairs(divisor, numbers)

print("There are " + str(result) + " pairs.\n")