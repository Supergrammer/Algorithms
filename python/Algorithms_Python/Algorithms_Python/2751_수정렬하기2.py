import sys
input = sys.stdin.readline

# 1
N = int(input())
array = [int(input()) for _ in range(N)]
array.sort()

for i in array:
	print(i)

# 2
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

N = int(input())
array = [int(input()) for _ in range(N)]

for i in merge_sort(array):
	print(i)