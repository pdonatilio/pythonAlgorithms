# Binary Search recursive with python

def binary_search(array, key, start, end):

    if start > end:
        return False

    middle = (start + end) // 2

    if key == array[middle]:
        return True

    # Pushing the search to the array's middle with recursivity
    if key < array[middle]:
        return binary_search(array, key, sart, middle - 1) # To the left
    return binary_search(array, key, middle + 1, end) # To the right

def binary_search_output(key):
    if binary_search(array, key, 0, len(array) - 1) == True:
        print(key,'exists inside the array')
    else:
        print(key,'not exists inside the array')

array = [11,5,10,20,15,4]
array.sort() # To the binary search works, we'll need an ordered array

#Running the examples
binary_search_output(20)
binary_search_output(30)