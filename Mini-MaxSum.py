# Completed Mini-Max Sum Problem from Hackerrank

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_sum = sum(arr) - arr[0]
    max_sum = sum(arr) - arr[0]
    for i in range(len(arr)):
        if sum(arr) - arr[i] > max_sum:
            max_sum = sum(arr) - arr[i]
        elif sum(arr) - arr[i] < min_sum:
            min_sum = sum(arr) - arr[i]
    print(min_sum, max_sum)
