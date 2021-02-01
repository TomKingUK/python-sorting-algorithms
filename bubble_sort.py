# ~~~ Bubble Sort ~~~
# Very basic sort, not suitable for sorting large arrays
# https://en.wikipedia.org/wiki/Bubble_sort
def bubble_sort(arr):
	for i in range(len(arr)):
		# For current to penultimate
		for cur in range(len(arr) - 1 - i):
			# If current < next
			if arr[cur] > arr[cur + 1]:
				# Swap current and next
				arr[cur], arr[cur + 1] = arr[cur + 1], arr[cur]
	return arr