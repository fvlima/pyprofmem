[![Build Status](https://travis-ci.org/fvlima/pyprofmem.svg?branch=master)](https://travis-ci.org/fvlima/pyprofmem)
[![Coverage Status](https://coveralls.io/repos/github/fvlima/pyprofmem/badge.svg)](https://coveralls.io/github/fvlima/pyprofmem)

# pyprofmem

A simple utility decorator to helps developers to see the memory usage of a determined function and its internal calls. It also provides a decorator to see the profile stats usage with memory. In this case, the cProfile implementation will be used.

## usage

#### @profile_with_memory_usage 

```python
from concurrent import futures
from time import sleep
 
from decorators import profile_with_memory_usage, PROFILE_SORT_STDNAME
 
 
@profile_with_memory_usage(sort_type=PROFILE_SORT_STDNAME)
def execute():
    with futures.ProcessPoolExecutor() as executor:
        l = [executor.submit(sleep, 1) for _ in range(10)]
        results = []
        for f in futures.as_completed(l):
            results.append(f.result())
 
  
if __name__ == '__main__':
    execute()
```

The profile_with_memory_usage decorator will print
 
```
         1955 function calls in 3.021 seconds
 
   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:102(release)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:142(__init__)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:146(__enter__)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:153(__exit__)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:159(_get_module_lock)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:173(cb)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:197(_call_with_frames_removed)
      
        ...
 
       42    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'setter' of 'property' objects}
       11    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
 
 
Ran profile_with_memory_usage to execute
Initial RAM: 13.1 MiB
Final RAM: 13.5 MiB
```

#### @memory_usage
 
```python
 
@memory_usage
def execute():
    for _ in range(10):
        pass
 
if __name__ == '__main__':
    execute()
```

The memory_usage decorator will print 

```
Ran memory_usage to execute in 1.00135 seconds
Initial RAM: 12.9 MiB
Final RAM: 12.9 MiB
```