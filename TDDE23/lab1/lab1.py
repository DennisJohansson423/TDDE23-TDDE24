#Lab 1A
def div_by_three(n):
    """
    This function divides n by three and return
    true if it is a whole number, else false.
    """
    result = n/3
    print(result)
    return result%1 == 0

#Tests
print(div_by_three(6))
print(div_by_three(4))


#Lab 1B
def max2(x, y):
    """Returns the biggest number of x or y."""
    if x == y:
        return x
    elif x > y:
        return x
    else:
        return y


def max3(x, y, z):
    """Returns the biggest number of x or y or z."""
    if x == y == z:
        return x
    elif x > z or y > z:
        return max2(x, y)
    else:
        return z

#Tests
print(max2(4, 4))
print(max2(1, 7))
print(max3(9, 5, 3))
print(max3(8, 8, 4))
print(max3(4, 1, 6))
print(max2(3, 6) + max3(3, 3, 3))