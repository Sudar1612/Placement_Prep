# Average Time Complexity => O(nlogn)

def quickSort(arr):
    n = len(arr)
    if(n <= 1):
        return arr
    pivot = arr.pop()
    greater,lower=[],[]

    for num in arr:
        if(num > pivot):
            greater.append(num)
        else:
            lower.append(num)
    return quickSort(lower) + [pivot] + quickSort(greater)

print(quickSort([5,6,7,8,9,8,7,6,5,6,7,8,9,0]))
