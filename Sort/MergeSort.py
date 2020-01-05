#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import math


def mergesort(arr):
    if(len(arr) < 2 ):
        return arr
    middle = math.floor(len(arr)/2)
    left, right = arr[0:middle], arr[middle:]
    return merge(mergesort(left), mergesort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


def main():
    arr1 = [6, 4, 3, 7, 5, 1, 2]
    print(arr1)
    arr = mergesort(arr1)
    print(arr)


if __name__ == "__main__":
    main()

