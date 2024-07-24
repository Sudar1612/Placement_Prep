# Time Complexity -> O(logn)
def iterative(arr,search):
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

def recursive(arr,search,begin,end):
    if(begin <= end):
        mid = (begin + end) //2
        if(arr[mid] == search):
            return mid
        elif (arr[mid] < search):
            recursive(arr,search,mid+1,end)
        else:
            recursive(arr,search,begin,mid-1)
    else:
        return None


arr = [2,4,5,6,7,8,9,10,12,13,14]
search = 19
print(iterative( arr,search))
print(recursive(arr,search,0,len(arr)-1))