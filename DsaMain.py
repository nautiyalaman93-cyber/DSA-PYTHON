
#Binary Search


def binary_search(arr,k):
    l=0
    r=len(arr)

    while(r>=l):
        m=l+(r-l)//2

        if arr[m]==k:
            return m

        elif arr[m]>k:
            r=m-1

        else:
            l=m+1
        return -1


arr=[1,2,4,5,6,7,10]
k=7

# print(binary_search(arr,k))


#SORTING ALGORITHMS

#Bubble Sorting


def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
             arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr




#print(bubble_sort(arr))


#Selection Sorting

def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j


        arr[i],arr[min]=arr[min],arr[i]

    return arr

#print(selection_sort(arr))



"""Insertion Sort """


def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        j=i-1
        key=arr[i]
        while (j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j-=1

        arr[j+1]=key

    return arr
arr=[75,90,100,95,85,80]
print(insertion_sort(arr))
