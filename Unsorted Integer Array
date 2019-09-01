def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return None
    else:
        min_no = ints[0]
        max_no = ints[0]
        for i in range(len(ints)):
            if min_no > ints[i]:
                min_no = ints[i]
            if max_no < ints[i]:
                max_no = ints[i]
        return (min_no,max_no)
            

## Example Test Case of Ten Integers
import random
def main():
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)

    print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")#pass


    l = [i for i in range(90, 100)]  # a list containing 90 - 100
    random.shuffle(l)

    print ("Pass" if ((90, 99) == get_min_max(l)) else "Fail")#pass


    l = [i for i in range(40, 50)]  # a list containing 40 - 50
    random.shuffle(l)

    print ("Pass" if ((40, 49) == get_min_max(l)) else "Fail")#pass


    l = [4]  # a list containing only one element
    #random.shuffle(l)

    print ("Pass" if ((4, 4) == get_min_max(l)) else "Fail")#pass


    l = []  # empty list
    #random.shuffle(l)

    print ("Pass" if (None == get_min_max(l)) else "Fail")#pass

if __name__ == '__main__':
	main()
