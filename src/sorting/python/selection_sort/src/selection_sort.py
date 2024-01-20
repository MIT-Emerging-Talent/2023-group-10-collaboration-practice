def selection_sort(numArray):
	array_len = len(numArray)
	for i in range(array_len - 1):
		for j in range(i + 1, array_len):
			if (numArray[j] < numArray[i]):
				temp = numArray[i]
				numArray[i] = numArray[j]
				numArray[j] = temp
    return numArray