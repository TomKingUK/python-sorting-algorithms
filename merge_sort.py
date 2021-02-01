# ~~~ Merge Sort ~~~

def merge_sort(arr):
	if len(arr) > 1:
		# Define mid point of array
		middle = len(arr) //2
		# Define left portion of array
		left = arr[0:middle]
		# Define left portion of array
		right = arr[middle: ]
		# Perform merge sort on left portion
		merge_sort(left)
		# Perform merge sort on left portion
		merge_sort(right)
		#Merge sort algorithm
		i = j = 0
		for elem in range(len(arr)):
			L = left[i] if i < len(left) else None
			R = right[j] if j < len(right) else None
			if (L is not None and R is not None) and \
				(L < R) or R is None:
				arr[elem] = L
				i += 1
			elif (L is not None and R is not None) and \
				(L >= R) or L is None:
				arr[elem] = R
				j += 1
	return arr
