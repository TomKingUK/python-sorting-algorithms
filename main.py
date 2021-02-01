import tests

from copy_sort import copy_sort
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

# Test sorting methods		
tests.test_sort(copy_sort)
tests.test_sort(bubble_sort)
tests.test_sort(selection_sort)
tests.test_sort(insertion_sort)
tests.test_sort(merge_sort)
tests.test_sort(quick_sort)