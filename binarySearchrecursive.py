# recursive way

def binary_search_helper(arr, val, low, high):
    if low > high:
        return "NO MATCH"
    
    mid = low + ((high - low) // 2)

    if arr[mid] == val:
        return mid 
    elif val < arr[mid]:
        return binary_search_helper(arr, val, low, mid-1)
    else:
        return binary_search_helper(arr, val, mid+1, high)
    
def binary_search(arr, val):
    return binary_search_helper(arr, val, 0, len(arr)-1)