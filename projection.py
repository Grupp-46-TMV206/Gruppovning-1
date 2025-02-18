from numpy import cross, dot, array, linalg
import math

def point_projection(p, v1, v2, n=None):
    p = array(p)

    if n is None:
        n = cross(v1, v2)
    else:
        n = array(n)

    """The equation below is partly taken from the coursebook, page 65, thesis 1:
    u' = ((u(*)v/abs(v)^2)*v. It is as such safe to use. The rest of the equation is included from complementation."""

    result = p - (n * ((dot(p, n)) / pow(abs(linalg.norm(n)), 2)))
    return print(f"The point-projection is: {result}")

"""These two values will be the same. v1 x v2 give the normals (0, 0, -1) and (0, 0, 1) for each respective value v2.
In this calculation, the direction of the normal's values doesn't matter, just the magnitudes.
(0, 0, -1) is essentially a scaled version of (0, 0, 1), by a factor of -1.
As the equation includes a division by abs(n)^2, scaled vectors will all give the same result.

Additionally, a negative sign does not matter in the dot product of p and n, or in the multiplication by n.
A negative value in the dot product negates the whole dot product. n * also becomes -n *.
This gives a double negation between the two mentioned n-related values, which results in the same positive."""

point_projection([math.pi, math.e, 1], [1, 1, 0], [0, -1, 0])
point_projection([math.pi, math.e, 1], [1, 1, 0], [0, 1, 0])

"""These two values will be the same, as the normal (3, 3 ,3) is just a scaled version of (1, 1, 1).
As the equation includes a division by abs(n)^2, scaled vectors will all give the same result."""

point_projection([math.pi, math.e, 1], None, None, [1, 1, 1])
point_projection([math.pi, math.e, 1], None, None, [3, 3, 3])
