# ~~~ Copy sort ~~~
# This is a very basic sort which is neither time or space efficient
def copy_sort(arr):
	copy = arr
	sorted_copy = []
	while len(copy) > 0:
		minimum = 0
		for elem in range(len(copy)):
			if copy[elem] < copy[minimum]:
				minimum = elem
		sorted_copy.append(copy.pop(minimum))
	return sorted_copy
