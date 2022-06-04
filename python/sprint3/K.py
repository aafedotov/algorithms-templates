def merge(arr, lf, mid, rg):

	left = arr[lf:mid]
	right = arr[mid:rg + 1]

	l, r = 0, 0
	k = lf

	while l < len(left) and r < len(right):
		if left[l] <= right[r]:
			arr[k] = left[l]
			l += 1
		else:
			arr[k] = right[r]
			r += 1
		k += 1

	while l < len(left):
		arr[k] = left[l]
		l += 1
		k += 1

	while r < len(right):
		arr[k] = right[r]
		r += 1
		k += 1

	return arr


def merge_sort(arr, lf, rg):

	if lf >= rg:
		return
	mid = (lf + rg) // 2
	merge_sort(arr, lf, mid)
	merge_sort(arr, mid + 1, rg)

	merge(arr, lf, mid + 1, rg)
