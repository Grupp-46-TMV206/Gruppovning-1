from numpy import cross, dot, array, linalg
import math

# The formula implemented on line 14 is taken straight from the coursebook on page 65, thesis 1:
# u' = ((u(*)v)/abs(v)^2)*v.
# As such, it will work just like the original function would.
# This is proven by our first 2 point projections giving the same result.

def point_projection(p, v1, v2, n=None):
    p = array(p)

    if n is None:
        n = cross(v1, v2)
    else:
        n = array(n)

    result = n * ((dot(p, n)) / pow(abs(linalg.norm(n)), 2))
    return print(f"The point-projection is: {result}")

# The two calculations below will assume the same value as each other.
#  All values will be non-negative, so -1 does not matter over 1.
point_projection([math.pi, math.e, 1], [1, 1, 0], [0, -1, 0])
point_projection([-math.pi, math.e, 1], [1, 1, 0], [0, 1, 0])

# The two calculations below will -also- assume the same value as each other.
# The normal has the same direction in both, and assumes the same value.
point_projection([math.pi, math.e, 1], None, None, [1, 1, 1])
point_projection([-math.pi, math.e, 1], None, None, [3, 3, 3])
