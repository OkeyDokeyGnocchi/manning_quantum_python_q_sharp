# Linear Algebra Examples
#  - Working through the examples in Appendix C

import numpy as np

# Initial example
directions_in_meters = np.array([[30], [50]])
directions_in_feet = 3.28 * directions_in_meters
print(directions_in_feet)

# Exercise C.1: Unit conversion
#  - What are 25 meters west and 110 meters north in feet?
#  - In terms of thinking of cardinal directions like a 2D graph:
#    - North and East are positive
#    - West and South are negative
conversion_factor = 3.28
c1_array_meters = np.array([[-25], [110]])
c1_array_feet = c1_array_meters * conversion_factor
print(c1_array_feet)

# Exercise C.2: Linearity Check
#  - Functions are linear if f(ax + by) = af(x) + bf(y)
#  - Which functions are linear:
#    - f(x) = 2x
#    - f(x) = x^2
#    - f(x) = 2^x

# f(x) = 2x
# 2(ax + by)
# Result 2ax + 2by
# af(x) + bf(y)
# Result a(2x) + b(2y)
# 2ax + 2by == a(2x) + b(2y)
# Linear

# f(x) = x^2
# (ax + by)^2
# (ax + by) * (ax + by)
# Result ax^2 + 2axby + by^2
# af(x) + bf(y)
# a(x^2) + b(x^2)
# ax^2 + 2axby + bx^2 != ax^2 + by^2
# Not Linear

# f(x) = 2^x
# 2^(ax + by)
# Result 2^ax * 2^by
# af(x) + bf(y)
# Result a2^x + b2^y
# 2^ax * 2^by != a2^x + b2^y
# Not Linear

# Computing f(np.array([[2], [3]]))
# Basis horiz = [[1], [0]], vert [[0], [1]]
horizontal = np.array([[1], [0]])
vertical = np.array([[0], [1]])
vec = 2 * horizontal + 3 * vertical
print(vec)
f_horizontal = np.array([[1], [1]])
f_vertical = np.array([[1], [-1]])
new_vec = 2 * f_horizontal + 3 * f_vertical
print(f'{new_vec}\n')

# Exercise C.3
# Linear function g such that:
#  - g([[1], [0]]) = [[2.3], [-3.1]]
#  - g([[0], [1]]) = [[-5.2], [0.7]]
# Compute g([[2], [-2]])
# To solve: set g_horiz and g_vert to the ref values above
#    then multiply by 2 and -2, respectively
print("Exercise C.3:")
g_horizontal = np.array([[2.3], [-3.1]])
g_vertical = np.array([[-5.2], [0.7]])
c3_g_vec = 2 * g_horizontal + -2 * g_vertical
print(c3_g_vec)