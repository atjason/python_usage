import sys

'''
try:
except: when has error.
else: when has no error.
finally: no matter has error or not.
'''

try:
  1/0
except OSError as e:
  print(f"OS error: {e}")
except Exception as e:
  print(f"Error: {e}")
else:
  print('Good, no error.')
finally:
  print('Done')

assert ('darwin' in sys.platform), 'Can only run on macOS.'
