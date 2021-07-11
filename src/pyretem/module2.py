"""This module is used to perform certain operations.
"""

from collections.abc import Iterable


def get_values(a):
    """Gets first two values of an array.

    Args:
        a (array-like): An array where only the first two elements are relevant.

    Returns:
        tuple: A tuple containing:

            - *float*: First element of `a`.
            - *float*: Second element of `a`.
    """
    return a[0], a[1]


def get_value(a: Iterable) -> int:
    """Gets first value of an array.

    Args:
        a: An array where only the first element is relevant.

    Returns:
        First value of `a`.

    """
    return a[0]
