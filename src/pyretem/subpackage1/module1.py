"""This module contains classes.
"""


class AnObject:
    """Defines an object

    Args:
        a (bool): This is param `a` description.
        b (np.array): This is param `b` description.

    Attributes:
        a (bool): An attribute.
        b (np.array): Another attribute.

    Notes:
        There's a little of repeatability in paramaters and attributes.
        Nevertheless, the output is quite different (take a look).
    """

    def __init__(self, a, b):
        pass


    def operate_on_attributes(self, operator):
        """Operates on attributes accordingly to passed method.

        Args:
            operator (callable): A function that receives `a` and `b`.
        """
        pass

