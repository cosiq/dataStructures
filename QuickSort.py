def quickSort(lst):
	if len(lst) <= 1: return lst
	pivot = lst.pop()
	left, right = [], []
	for item in lst:
		if item >= pivot: right.append(item)
		if item < pivot: left.append(item)
	return quickSort(left) + [pivot] + quickSort(right)