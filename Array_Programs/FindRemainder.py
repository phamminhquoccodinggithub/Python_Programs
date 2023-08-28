# Given multiple numbers and a number n, the task is to print the remainder after multiplying all the numbers divided by n.
# Examples: 

# Input : arr[] = {100, 10, 5, 25, 35, 14}, n = 11
# Output : 9
# Explanation: 100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9

# Naive approach: First multiple all the numbers then take % by n to find the remainder, 
# But in this approach, if the number is a maximum of 2^64 then it gives the wrong answer.

# An approach that avoids overflow: First take a remainder or individual number like arr[i] % n. 
# Then multiply the remainder with the current result. After multiplication, again take the remainder to avoid overflow. 
# This works because of the distributive properties of modular arithmetic. ( a * b) % c = ( ( a % c ) * ( b % c ) ) % c 

def findRemainder(arr, n):
    """
        This function is find remainder of array
        @param arr: Input array
        @param n: divided number
    """
    result = 1
    for i in arr:
        result = result * (i % n)
    return result % n

def main():
    # Input array
    arr = [100, 10, 5, 25, 35, 14]
    n = 11
    print("Result is ", findRemainder(arr, n))

if __name__ == "__main__":
    main()
