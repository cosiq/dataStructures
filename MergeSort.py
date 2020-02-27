def merge(a, b):
	res = []
	aIndex, bIndex = 0, 0
	while aIndex < len(a) and bIndex < len(b):
		if a[aIndex] < b[bIndex]: 
			res.append(a[aIndex])
			aIndex += 1
		else: 
			res.append(b[bIndex])
			bIndex += 1
	if aIndex == len(a): res.extend(b[bIndex:])
	else: res.extend(a[aIndex:])
	return res

def mergeSort(A):
	if len(A) <= 1: return A
	return merge(mergeSort(A[:len(A) // 2]), mergeSort(A[len(A) // 2:]))
