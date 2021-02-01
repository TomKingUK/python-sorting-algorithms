#### Insertion Sort ###
'''
https://en.wikipedia.org/wiki/Insertion_sort
'''
def insertion_sort(arr):
	# From second element to last element in array
	for i in range(1, len(arr)):
		# While current element larger than previous element
		# (1 >= 1 checks if previous element exists)
		while arr[i - 1] > arr[i] and i >= 1:
			# Swap current and previous values
			arr[i] , arr[i - 1] = arr[i - 1], arr[i]
			# Repeat with previous element, swapping until a 
			# previous element < than current element is found,
			# or no previous element exists
			i -= 1
	return arr
