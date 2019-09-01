def rearrange_digits(input_list):

    sorted_list = []
    result = []
    x = 0
    y = 0
    sorted_list = mergesort(input_list)
    length = len(sorted_list)-1
    i = length
    j = length-1
    while i >= 0:
        x = x*10 + sorted_list[i]
        i = i-2
    result = result+[x]
    while j >= 0:
        y = y*10 + sorted_list[j]
        j = j-2
    result = result+[y]
    #print(result) 
    return result

    
def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

def test_function(test_case):
    
    if not test_case:
        return []

    else:
        output = rearrange_digits(test_case[0])
        solution = test_case[1]
        if sum(output) == sum(solution):
            print("Pass")
        else:
            print("Fail")

test_function([[1, 2, 3, 4, 5], [531, 42]])#pass
#test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function ([[4, 6, 2, 5, 9, 8], [964, 852]])#pass
test_function ([[], []])#pass
test_function ([[4, 4, 4, 4, 4, 4], [444, 444]])#pass

