# Helper Method
count = 0
def move_left(array, i):
	while i > 0 and array[i] < array[i-1]:
		# swap elements at i-1 and i
		array[i], array[i-1] = array[i-1], array[i]
		i -= 1 # move left

# Insertion Sort
def iSort(array):
	i = 1
	while i < len(array):
		move_left(array, i) 
		i += 1
	return array

a = [93, 85, 22, 69, 73, 59]

print("Original array : ", a)
print("Sorted array   : ", iSort(a))
print(count)
 