"""This is an example module.
"""


def compute_something(a: float, b: int) -> float:
    """Sums `a` and `b`.

    Args:
        a: A brief explanation of `a`.
        b: A brief explanation of `b`.

    Returns:
        float: The sum of `a` and `b`.


    Notes:
        The addition of an `int` and a `float` returns a `float`.

        Mathematically, this performs the following operation:

        .. math::

            c = a + b

    Warnings:
        The code will not break if you pass two str.
    """
    return a + b


def add(a, b):
    """Adds two elements.

    Args:
        a (int or float or str): First element.
        b (int or float or str): Second element.
    """
    pass


def merge_arrays(a, b):
    """Merges a list and a tuple.

    Args:
        a (list): A list.
        b (tuple): A tuple.

    Returns:
        list:  The result of merging the list and the tuple.

    Notes:
        Do not forget to respect indentations when
        changing line.

    .. deprecated:: 0.1.0
        `merge_arrays` will be removed in `pyretem` 0.2.0, find out another
        way of merging arrays.
    """
    pass


def sum_np_arrays(a, b):
    """Sums two `numpy` arrays.

    Args:
        a (np.array): First array.
        b (np.array): Second array.

    Returns:
        np.array: Sum of passed arrays.
    """
    pass
