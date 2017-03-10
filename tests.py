import sys

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from unittest import TestCase

from pyprofmem.decorators import (
    memory_usage, profile_with_memory_usage, PROFILE_SORT_CUMULATIVE, PROFILE_SORT_CALLS,
    PROFILE_SORT_STDNAME, PROFILE_SORT_TIME
)


class StdOut(object):
    """Context manager to capture the output of the function calls"""

    def __init__(self):
        self.__lines = []

    def __enter__(self):
        self.__stdout = sys.stdout
        sys.stdout = self.__strio = StringIO()
        return self

    def __exit__(self, *args):
        self.__lines.extend(self.__strio.getvalue().splitlines())
        del self.__strio
        sys.stdout = self.__stdout

    def __len__(self):
        return len(self.__lines)

    def __str__(self):
        return '\n'.join(self.__lines)

    def __getitem__(self, item):
        return self.__lines[item]


class Test(TestCase):

    @memory_usage
    def func_test_memory(self):
        for _ in range(10):
            pass

    @profile_with_memory_usage()
    def func_test_profile_without_arguments(self):
        text = 'func_test_profile_without_arguments'
        return text

    @profile_with_memory_usage(sort_type=PROFILE_SORT_CUMULATIVE)
    def func_test_profile_cumulative(self):
        text = 'func_test_profile_cumulative'
        return text

    @profile_with_memory_usage(sort_type=PROFILE_SORT_CALLS)
    def func_test_profile_calls(self):
        text = 'func_test_profile_calls'
        return text

    @profile_with_memory_usage(sort_type=PROFILE_SORT_STDNAME)
    def func_test_profile_stdname(self):
        text = 'func_test_profile_stdname'
        return text

    @profile_with_memory_usage(sort_type=PROFILE_SORT_TIME)
    def func_test_profile_time(self):
        text = 'func_test_profile_time'
        return text

    def test_memory(self):
        with StdOut() as stdout:
            self.func_test_memory()
        self.assertEqual(len(stdout), 3)
        self.assertEqual(stdout[0].find('func_test_memory') > 0, True)

    def test_profile_without_arguments(self):
        with StdOut() as stdout:
            self.func_test_profile_without_arguments()
        self.assertEqual(len(stdout), 12)
        self.assertEqual(stdout[-3].find('func_test_profile_without_arguments') > 0, True)

    def test_profile_cumulative(self):
        with StdOut() as stdout:
            self.func_test_profile_cumulative()
        self.assertEqual(len(stdout), 12)
        self.assertEqual(stdout[-3].find('func_test_profile_cumulative') > 0, True)

    def test_profile_calls(self):
        with StdOut() as stdout:
            self.func_test_profile_calls()
        self.assertEqual(len(stdout), 12)
        self.assertEqual(stdout[-3].find('func_test_profile_calls') > 0, True)

    def test_profile_stdname(self):
        with StdOut() as stdout:
            self.func_test_profile_stdname()
        self.assertEqual(len(stdout), 12)
        self.assertEqual(stdout[-3].find('func_test_profile_stdname') > 0, True)

    def test_profile_time(self):
        with StdOut() as stdout:
            self.func_test_profile_time()
        self.assertEqual(len(stdout), 12)
        self.assertEqual(stdout[-3].find('func_test_profile_time') > 0, True)
