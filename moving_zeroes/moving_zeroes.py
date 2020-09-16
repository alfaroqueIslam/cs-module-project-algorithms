'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1):  
        for j in range(0, n-i-1):              
            if arr[j] == 0 and arr[j+1] != 0: 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")