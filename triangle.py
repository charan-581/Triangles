"""
Module for classifying triangles based on side lengths.
"""

def classifyTriangle(a=None, b=None, c=None):
    """
    Classify the type of triangle based on side lengths.
    Args:
        a (int): Length of side a.
        b (int): Length of side b.
        c (int): Length of side c.
    Returns:
        str: Classification of the triangle.
    """
    if not all(isinstance(side, int) for side in [a, b, c]) or None in [a, b, c]:
        return 'InvalidInput'
    if any(side <= 0 for side in [a, b, c]) or any(side > 200 for side in [a, b, c]):
        return 'InvalidInput'
    if a + b <= c or b + c <= a or a + c <= b:
        return 'NotATriangle'
    if a == b == c:
        return 'Equilateral'
    if any(a ** 2 + b ** 2 == c ** 2 for a, b, c in [(a, b, c), (b, c, a), (c, a, b)]):
        return 'Right'
    return 'Scalene' if len(set([a, b, c])) == 3 else 'Isosceles'
