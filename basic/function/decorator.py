import functools

def log(func):
  def wrapper(*args, **kwargs):
    print(f'call {func.__name__}()')
    return func(*args, **kwargs)
  return wrapper

@log
def now():
  print('2023-10-01')

now()

now.__name__  # 'wrapper', the original function's name is lost.

def log2(text):
  def decorator(func):
    @functools.wraps(func)  # Preserve the original function's metadata
    def wrapper(*args, **kwargs):
      print(f'{text} {func.__name__}()')
      return func(*args, **kwargs)
    return wrapper
  return decorator

@log2('execute')
def now2():
  print('2023-10-01')

now2()

now2.__name__  # 'now2', the original function's name is preserved.
