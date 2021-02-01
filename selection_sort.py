#### Selection Sort ###
'''
Swap-based algorithm. One of the most efficient sorting
algorithms for arrays of 20 or fewer elements.
Time complexity O(n**2).
Space complexity 2(n-1) writes.
Low # of writes makes this good for EEPROM or flash memory
where each write shortens the lifespan of the memory.
Selection sort always scans every item of the unsorted portion
of the list, therefore it always takes the same amount of time
regardless of the starting order of the list.
https://en.wikipedia.org/wiki/Selection_sort
'''
def selection_sort(lst):
	for i in range(len(lst) - 1):
		value = lst[i]
		current = i
		for j in range(i + 1, len(lst)):
			if lst[j] < lst[current]:
				current = j
		lst[i] = lst[current]
		lst[current] = value
	return lst
