def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    #if input_list is None:
        #print("the list is empty")
        
    lower_bound = 0
    upper_bound = len(input_list)-1
    
    while (lower_bound <= upper_bound):
        mid=(lower_bound + upper_bound)//2
        
        if input_list[mid]==number:
            #print(mid)
            return mid
        
        if input_list[lower_bound] <= input_list[mid]:#left half of the list is sorted

            if input_list[lower_bound] <= number and input_list[mid] > number:#searching in the left half
                upper_bound = mid-1

            else: #searching in the right half
                lower_bound = mid+1

        else:#right half of the list is sorted

            if input_list[mid] <= number and input_list[upper_bound] >= number:#searching in the right half
                lower_bound = mid+1

            else:##searching in the left half
                upper_bound = mid-1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):

    if not test_case:
        print("the list is empty")
        return None
    else:    
        input_list = test_case[0]
        number = test_case[1]
        if linear_search(input_list, number) == rotated_array_search(input_list, number):
            print("Pass")
        else:
            print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])#pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])#pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])#pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])#pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])#pass
test_function([])#list is empty
test_function([[1, 2, 3, 4, 6, 7, 8 ], 4])#pass
