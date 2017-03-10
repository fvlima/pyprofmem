"""
A simple utility decorator to helps developers to see the memory usage
of a determined function and its  internal calls. It also provides a
decorator to see the profile stats usage with memory. In this case,
the cProfile implementation will be used.

    Examples:

    @profile_with_memory_usage()
    def some_function():
        pass

    @profile_with_memory_usage(sort_type=PROFILE_SORT_CALLS)
    def some_function():
        pass

    @memory_usage
    def some_function():
        pass
"""

from __future__ import print_function

import resource

from cProfile import Profile
from functools import wraps
from pstats import Stats
from time import time


PROFILE_SORT_CUMULATIVE = 'cumulative'
PROFILE_SORT_CALLS = 'calls'
PROFILE_SORT_STDNAME = 'stdname'
PROFILE_SORT_TIME = 'time'


def profile_with_memory_usage(sort_type=PROFILE_SORT_CUMULATIVE):
    def wrap(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            """
            Prints the profile stats and the memory usage to the decorated
            function
            """

            mem_initial = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

            profile = Profile()
            result = profile.runcall(func, *args, **kwargs)

            mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

            _print_stats(profile, sort_type)

            print('Ran profile_with_memory_usage to %s' % func.__name__)
            print('Initial RAM: %s ' % _format_size(mem_initial))
            print('Final RAM: %s' % _format_size(mem_final))

            return result
        return wrapped
    return wrap


def memory_usage(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        """
        Prints the initial and final amount of the memory usage to
        the decorated function. The time elapsed will be printed as well
        """

        begin = time()
        mem_initial = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        result = func(*args, **kwargs)

        end = time()
        mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        print('Ran memory_usage to %s in %d seconds' % (func.__name__, (end - begin)))
        print('Initial RAM: %s' % _format_size(mem_initial))
        print('Final RAM: %s' % _format_size(mem_final))

        return result
    return wrap


def _print_stats(profile, sort_type):
    """Generate the stats to the profile"""
    stats = Stats(profile)
    stats.strip_dirs()
    stats.sort_stats(sort_type)
    stats.print_stats()


def _format_size(size):
    """Copied from tracemalloc.py"""
    for unit in ('B', 'KiB', 'MiB', 'GiB', 'TiB'):
        if abs(size) < 100 and unit != 'B':
            # 3 digits (xx.x UNIT)
            return '%.1f %s' % (size, unit)
        if abs(size) < 10 * 1024 or unit == 'TiB':
            # 4 or 5 digits (xxxx UNIT)
            return '%.0f %s' % (size, unit)
        size /= 1024
