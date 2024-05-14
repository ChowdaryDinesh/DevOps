"""
 Find the smallest number, given a list of intergers with the following conditions:
    1. Length of the list is N (1 <= N <= 10^6)
    2. Each element in the list is an integer (1 <= A[i] <= 10^7)
Example:
    1. N = 5
    2. List = [1, 2, 3, 4, 5]
    3. Perform the following operations:
        a. Concat the consecutive elements in the list:
            example: [1, 2, 3, 4, 5] => [12, 34, 5]
        b. Return the smallest number from the list.

example 2:
    1. N = 6
    2. List = [123, 234, 986, 473, 876, 956]
    3. Perform the following operations:
        a. Concat the consecutive elements in the list:
            example: [123, 234, 986, 473, 876, 95] => [123234, 986473, 87695]
        b. Return the smallest number from the list.

"""

def smallest_number(arr: list):
    """Function to find the smallest number from the list"""
    length = len(arr)
    temp_list = list()
    for i in range(0, length-1,2):
        print(arr[i], arr[i+1])
        arr[i] = str(arr[i]) + str(arr[i+1])
        temp_list.append(int(arr[i]))
    if length % 2 != 0:
        temp_list.append(arr[-1])
    return min(temp_list)

def main():
    arr = list(map(int, input("Enter the list of integers: ").split()))
    if len(arr) > 10**6:
        print("Length of the list is greater than 10^6")
        return
    if any(i > 10**7 for i in arr):
        print("Element in the list is greater than 10^7")
        return
    print(smallest_number(arr))

main()