# Time Complexity -> O(logn)
def binarySearch(arr,search):
    begin ,end = 0, len(arr)-1

    while(begin <= end):
        mid_ind = (end + begin)//2
        if(search == arr[mid_ind]):
            return mid_ind
        elif(search < arr[mid_ind]):
            end = mid_ind -1
        else :
            begin = mid_ind + 1

    return None

print(binarySearch( [2,4,5,6,7,8,9,10,12,13,14],8))