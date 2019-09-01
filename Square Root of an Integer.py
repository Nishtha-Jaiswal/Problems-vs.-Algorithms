def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number ==  None:
        return None
    
    if number < 0:
        #print("enter a positive number")
        return None
    
    #Newton's method to calculate square root of any integer
    #using binary search
    x = number
    y = (x + 1) // 2 #integer division to get middle no from 0 to number
    while y < x: # square root of every number is less than its half so everytime we are only searching in the half range like in binary search
        x = y
        y = (x + number // x) // 2 # let x^2 = a.So, Xn+1 = (Xn + (a/Xn))/2,
                                    #since the number is getting divided by a constant amount so the time complexity is in logarithmic terms 

    return x
    pass

print ("Pass" if  (3 == sqrt(9)) else "Fail")#pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")#pass
print ("Pass" if  (4 == sqrt(16)) else "Fail")#pass
print ("Pass" if  (1 == sqrt(1)) else "Fail")#pass
print ("Pass" if  (5 == sqrt(27)) else "Fail")#pass
print ("Pass" if  (None == sqrt(-3)) else "Fail")#pass
print ("Pass" if  (None == sqrt(None)) else "Fail")#pass

""" source referred
https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf  """
