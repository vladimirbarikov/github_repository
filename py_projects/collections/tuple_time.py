import timeit

print(timeit.timeit("test1 = ('t', 'u', 'r', 'u', 'r', 'u', 'm')"))
print(timeit.timeit("test2 = ['t', 'u', 'r', 'u', 'r', 'u', 'm']"))

print(timeit.timeit("test1 = ('t', 'u', 'r', 'u', 'r', 'u', 'm')*500"))
print(timeit.timeit("test2 = ['t', 'u', 'r', 'u', 'r', 'u', 'm']*500"))

print(timeit.timeit("test1 = ('t', 'u', 'r', 'u', 'r', 'u', 'm')*1000"))
print(timeit.timeit("test2 = ['t', 'u', 'r', 'u', 'r', 'u', 'm']*1000"))

print(timeit.timeit("test1 = ('t', 'u', 'r', 'u', 'r', 'u', 'm')*5000"))
print(timeit.timeit("test2 = ['t', 'u', 'r', 'u', 'r', 'u', 'm']*5000"))