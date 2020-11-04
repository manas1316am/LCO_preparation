def binary_search(arr, val):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + ((high - low) // 2)

        if arr[mid] == val:
            return mid
        if val < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return "NO MATCH    "