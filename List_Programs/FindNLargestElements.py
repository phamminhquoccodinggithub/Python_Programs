# Given a list of integers, the task is to find N largest elements assuming size of list is greater than or equal o N. 

# Examples :

# Input : [4, 5, 1, 2, 9] 
#         N = 2
# Output :  [9, 5]

# Input : [81, 52, 45, 10, 3, 2, 96] 
#         N = 3
# Output : [81, 96, 52]

def findNLargestElements(lst, n):
    newLst = set(lst)
    result = []
    for i in range(n):
        result.append(max(newLst))
        newLst.remove(max(newLst))
    return result

def findNLargestElements2(lst, n):
    newList = set(lst)
    newList = list(sorted(newList))
    return newList[-n:]

def main():
    lst = [81, 52, 45, 10, 3, 2, 96]
    lst2 = [4, 5, 1, 2, 9]
    n = 3
    print("Result is ", findNLargestElements(lst, n=n))
    print("Result is ", findNLargestElements2(lst2, n=2))


if __name__ == "__main__":
    main()