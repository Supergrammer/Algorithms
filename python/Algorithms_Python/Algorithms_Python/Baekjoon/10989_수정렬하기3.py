import sys
input = sys.stdin.readline

def merge_sort(arr):
	if len(arr) <= 1:
		return arr

	mid = len(arr) // 2
	arr_left = merge_sort(arr[:mid])
	arr_right = merge_sort(arr[mid:])
	
	return merge(arr_left, arr_right)

def merge(arr_left, arr_right):
	merged = []
	lptr, rptr = 0, 0

	while lptr < len(arr_left) and rptr < len(arr_right):
		if arr_left[lptr] < arr_right[rptr]:
			merged.append(arr_left[lptr])
			lptr += 1
		else:
			merged.append(arr_right[rptr])
			rptr += 1

	if lptr < len(arr_left):
		merged.extend(arr_left[lptr:])
	else:
		merged.extend(arr_right[rptr:])

	return merged

def quick_sort(left, right):
	if left >= right:
		return

	pivot = partition(left, right)
	quick_sort(left, pivot - 1)
	quick_sort(pivot + 1, right)

def not_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    lesser, equal, greater = [], [], []

    for num in arr:
        if num < pivot:
            lesser.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)
    return quick_sort(lesser) + equal + quick_sort(greater)

def partition(left, right):
	pivot = array[left]
	lptr, rptr = left + 1, right

	while lptr < rptr:
		while array[lptr] <= pivot:
			lptr += 1
		while array[rptr] > pivot:
			rptr -= 1
		
		if lptr < rptr:
			array[lptr], array[rptr] = array[rptr], array[lptr]
	
	if array[rptr] <= pivot:
		array[left], array[rptr] = array[rptr], array[left]

	return rptr

N = int(input())
arr = [0] * 10001

for _ in range(N):
	arr[int(input())] += 1

for i in range(1, 10001):
	print(arr[i] * "{}\n".format(i), end='')