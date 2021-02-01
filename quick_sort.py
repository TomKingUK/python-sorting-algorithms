# ~~~ Quick Sort ~~~
def quick_sort(arr):
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr.pop(0)
		less = []
		more =[]
		# Quicksort Algorithm 
		for elem in arr:
			if elem < pivot:
				less.append(elem)
			else:
				more.append(elem)

	return quick_sort(less) + [pivot] + quick_sort(more)
		

