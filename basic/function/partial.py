import functools

int2 = functools.partial(int, base=2)

int2('100') # 4
int2('100', base=10) # 100
