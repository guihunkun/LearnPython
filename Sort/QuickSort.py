#!/usr/bin/env python 
# -*- coding:utf-8 -*-

def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(arr)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr


def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while  i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr,pivot,index - 1)
    return index - 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def main():
    arr1 = [6, 4, 3, 7, 5, 1, 2]
    print(arr1)
    arr = quickSort(arr1)
    print(arr)


if __name__ == "__main__":
    main()

