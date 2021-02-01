# Tests
def test_sort(test):
	test_name = ' '.join(str(test.__name__).split('_'))
	print(f' Testing {test_name} '.center(52, '*'))

	print(' Sorting positive integers:\t\t\t\t\t', 'Passed' if \
	test([5, 2, 3, 1, 4]) == [1, 2, 3, 4, 5] else 'Failed')
	
	print(' Sorting mixed int, float and boolean:\t\t', 'Passed' if \
	test([-5, 500, 0, -1, False, 4, 3.0]) == [-5, -1, 0, False, 3.0, 4, 500] else 'Failed')
	
	print(' Sorting empty list:\t\t\t\t\t\t', 'Passed' if test([]) == [] else 'Failed')
	
	print(' Sorting upper and lower case characters:\t', 'Passed' if \
	test(['c', 'C', 'a', 'd', 'A', 'b', 'B']) == ['A', 'B', 'C', 'a', 'b', 'c', 'd'] else 'Failed')
	
	print(' Sorting boolean values:\t\t\t\t\t', 'Passed' if \
	test([True, False, True, False]) == [False, False, True, True] else 'Failed')
	
	print(' Sorting values around zero:\t\t\t\t', 'Passed' if \
	test([0.1, 0, 0.0, 1, -1, -0.1]) == [-1, -0.1, 0, 0.0, 0.1, 1] else 'Failed')
	
	print(f' {test_name.capitalize()} test complete '.center(52, '*'), end='\n\n')