import os, sys, random

def num_comp(val1, val2):
	return val1 > val2

def partition(lst, start, end, idx_pivot, comp_fn):
	lst[start], lst[idx_pivot] = lst[idx_pivot], lst[start]
	pivot = lst[start]
	i, j = start + 1, start + 1

	# Two iterators. i stops wherever the value is greater than pivot.
	# When value j (normal iterator) is smaller than val at i, swap 'em' and move on
	while j <= end:
		if comp_fn(pivot, lst[j]):
			lst[j], lst[i] = lst[i], lst[j]
			i += 1
		j += 1
	lst[start], lst[i - 1] = lst[i - 1], lst[start]

	# return the point of pivot
	return i - 1


def quickSortRecurs(lst, start = 0, end = None, comp_fn = num_comp):
	if not end:
		end = len(lst) - 1

	if end - start < 1:
		return

	idx_pivot = random.randint(start, end)
	split_point = partition(lst, start, end, idx_pivot, comp_fn)

	quickSortRecurs(lst, start, split_point - 1, comp_fn)
	quickSortRecurs(lst, split_point + 1, end, comp_fn)

# For debugging purposes
if __name__=='__main__':
	test_lst1 = [5,2,6,4,7,8,1,0]
	quickSortRecurs(test_lst1)
	print(test_lst1)

	test_lst2 = [-4,2,6,-11,5,-12,8,1,0]
	def abs_comp(val1, val2):
		return abs(val1) > abs(val2)

	quickSortRecurs(test_lst2, comp_fn = abs_comp)		
	print(test_lst2)
