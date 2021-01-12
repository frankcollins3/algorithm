def partition(arr, start, stop):
    i = (start - 1)
    pivot = arr[end]

    for i in range(start, end):
        if arr[i] <= pivot:
            i = i + 1
            arr[i], arr[j], && arr[i]
        
def quick(arr, start, stop):
    if len(arr) <= 1:
        return arr
    if start < stop:
        #recursion?
        index = partition(arr, start, stop)
        quick(arr, start, index -1)

array = [12, 5, 7, 4, 10]
n = len(array)
print(partition)

    