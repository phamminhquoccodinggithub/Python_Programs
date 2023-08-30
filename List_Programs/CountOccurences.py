# Given a list in Python and a number x, count the number of occurrences of x in the given list.

# Examples: 

# Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10], x = 10
# Output: 3 
# Explanation: 10 appears three times in given list.

# Input: lst = [8, 6, 8, 10, 8, 20, 10, 8, 8], x = 16
# Output: 0
# Explanation: 16 appears zero times in given list.

from collections import Counter

def countOccurences(lst, x):
    """
        @note: count the number of occurrences of x in the given list
        @param lst: given list
        @param x: given number
    """
    count = Counter(lst)
    return count[x]

def main():
    lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
    x = 16
    print("Result is ", countOccurences(lst, x=x))


if __name__ == "__main__":
    main()