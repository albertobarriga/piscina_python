import sys

def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
        Args:
            function_to_apply: a function taking an iterable.
            iterable: an iterable object (list, tuple, iterator).
        Return:
            An iterable.
            None if the iterable can not be used by the function.
     """
    func = sys.argv[1]
    it = sys.argv[2]
    """controlar la entrad que iterable sea una tupla, list o conjunto(set)"""

    for i in it:
        yield func(i)

      
