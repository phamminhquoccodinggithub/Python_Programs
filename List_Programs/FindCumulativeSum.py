# The problem statement asks to produce a new list whose i^{th} element will be equal to the sum of the (i + 1) elements.

# Examples : 
 

# Input : list = [10, 20, 30, 40, 50]
# Output : [10, 30, 60, 100, 150]

# Input : list = [4, 10, 15, 18, 20]
# Output : [4, 14, 29, 47, 67]

def findCumulativeSum(lst):
    s = 0
    result = []
    for i in lst:
        s += i
        result.append(s)
    return result

def main():
    lst = [4, 10, 15, 18, 20]
    print("Result is ", findCumulativeSum(lst))


if __name__ == "__main__":
    main()
