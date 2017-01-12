def solution(number):  # Finish the solution so that it returns the sum of all the
    sumofMultiples = 0  # multiples of 3 or 5 below the number passed in.
    for i in range(1, number):
        if (i % 3 == 0 or i % 5 == 0):
            sumofMultiples += i
    return sumofMultiples
if __name__ == '__main__':
    solution(1000)
