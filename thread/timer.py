from threading import Timer

def timer_func(byTimer=False):
  print(1)

  if not byTimer:
    Timer(1.5, timer_func, (True,)).start()

timer_func()