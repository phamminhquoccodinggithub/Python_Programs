# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]

def sumOfDigitNumber(num):
    """
        @note: Find sum of digits of a number
        @param num: given number
    """
    result = 0
    for digit in str(num):
        result += int(digit)
    return result

def sumOfDigitInList(lst):
    """
        @note: Find sum of digits of each number in list
        @param lst: given list
    """
    result = []
    for i in lst:
        result.append(sumOfDigitNumber(i))
    return result

def main():
    lst = [12, 67, 98, 34]
    print("Result is ", sumOfDigitInList(lst))


if __name__ == "__main__":
    main()