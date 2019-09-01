"""
    Approach
    Solution is similar to implementig quicksort, here pivot is the first element.
    The difference here is that the value of pivot keeps changing depending on
    whether the value of pivot is 0,1 or 2
    """

def swap(input_list,a,b):
    temp = input_list[a]
    input_list[a] = input_list[b]
    input_list[b] = temp
    
def sort_012(input_list):

    lower_bound = 0
    pivot = 0
    upper_bound = len(input_list)-1
    while (pivot <= upper_bound):
        
        if input_list[pivot] == 0:
            swap(input_list,lower_bound,pivot)#swapping the value at pivot with the value at lb
            lower_bound = lower_bound + 1
            pivot = pivot + 1
        elif input_list[pivot] == 1:
            pivot = pivot + 1
        else:
            swap(input_list,pivot,upper_bound)#swapping the value at pivot with the value at hb
            upper_bound = upper_bound - 1
    return input_list
     
    pass

def test_function(test_case):

    if not test_case:
        print("empty list")
        return None
    else:
        sorted_array = sort_012(test_case)
        print(sorted_array)
        if sorted_array == sorted(test_case):
            print("Pass")
        else:
            print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
#[0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
#Pass

test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
#Pass

test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
#[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
#Pass

test_function([])
#empty list
