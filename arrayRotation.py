# 4, 5, 6, 1, 2, 3

def findRotation_helper(arr, low, high):
    if(high > low):
        return "NO MATCH"
    
    mid = low + ((high-low) // 2)
    
    if(mid < high and  arr[mid + 1] < arr[mid]):
        return (mid + 1)
    
    if(mid > low and arr[mid] < arr[mid-1]):
        return mid
    
    if(arr[high] > arr[mid]):
        rerturn findRotation_helper(arr, low, mid-1)
    
    return findRotation_helper(arr, mid+1, high)