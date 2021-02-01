#### Insertion Sort with debug text ###
'''
https://en.wikipedia.org/wiki/Insertion_sort
'''
def insertion_sort(arr):
	for i in range(1, len(arr)):
		print('START ITERATION #', i, flush=True)
		print('List in -->', arr, flush=True)

		value = arr[i]
		print('Value =', value, flush=True)
		while arr[i - 1] > value and i >= 1:
			print(f'Swapping arr[{i}]: {arr[i]} with list[{i - 1}]: {arr[i - 1]}')
			arr[i] = arr[i - 1]
			print(arr, flush=True)
			i -= 1
			print(f'Swapping arr[{i}]: {arr[i]} with value: {value}')
			arr[i] = value
			print(arr, flush=True)
			print('Remaining checks in current iteration =', i, flush=True)
		else:
			print(f'arr[{i}]: {arr[i]} > list[{i - 1}]: {arr[i - 1]} - NO SWAP')
		print('List out -->', arr, flush=True)
		print('END ITERATION #', i, '\n', flush=True)
	return arr


# Tests
print('Result:', *insertion_sort([4, 3, 2, 1]), '\n\n')
print('Result:', *insertion_sort([1, 3, 4, 2]), '\n\n')