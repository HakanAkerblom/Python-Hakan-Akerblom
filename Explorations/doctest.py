import math
import doctest
def sphere_vol(r):
    """
    >>> sphere_vol(1)
    4.1887902047863905
    """
    #  r = input("enter radius")
    if not isinstance(r, (float, int)):
        raise TypeError(f"radius must be int or float, not {type(r)}")
    return (4*math.pi*r**3)/3
sphere_vol(5)
sphere_vol(1)
doctest.testmod()