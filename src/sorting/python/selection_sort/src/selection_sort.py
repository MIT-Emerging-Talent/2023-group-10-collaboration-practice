def selection_sort(num_array):
	array_len = len(num_array)
	for i in range(array_len - 1):
		for j in range(i + 1, array_len):
			if (num_array[j] < num_array[i]):
				temp = num_array[i]
				num_array[i] = num_array[j]
				num_array[j] = temp
    return num_array