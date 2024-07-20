'''
The cumulative sum of a sequence of numbers is a running total that adds up the elements in the sequence as it progresses. 
Given a list of numbers, the cumulative sum at each position is computed by adding the sum of all previous numbers in the list up to the current position, including the number at the current position itself.
We're writing a recursive function in Python that calculates the cumulative sum of a list of numbers. 
The function's input: a single list as an argument.
Output: a new list containing the cumulative sums.
'''

def cumsum(numbers):
    return recursive_cumsum(numbers, index=0, accu=[])

def recursive_cumsum(numbers, index, accu):
    if index == len(numbers):
        return accu
    if index == 0:
        accu.append(numbers[index])
    else:
        accu.append(accu[-1] + numbers[index])
    
    return recursive_cumsum(numbers, index + 1, accu)
