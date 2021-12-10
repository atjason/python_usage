
import os
import os.path

print(os.getcwd()) # path of where python starts.

os.mkdir('./a') # raise error if recursively create or the folder exists.
os.makedirs('./a/b/c') # recursively mkdir, raise error if `./a/b/c` exists.

os.chdir('./a')
os.removedirs('./b/c')

os.chdir('..')
os.rmdir('./a')

# os.remove(file)

print('\nPath')
print(__file__) # full path
print(os.path.abspath(__file__)) # full path
print(os.path.basename(__file__)) # filname
print(os.path.dirname(__file__)) # current folder
print(os.path.dirname(os.path.abspath(__file__))) # current folder

print('\nFile')
print(os.path.exists(__file__)) # True
print(os.path.isabs(__file__)) # True
print(os.path.isfile(__file__)) # True
print(os.path.isdir(__file__)) # False
print(os.path.join(os.getcwd(), 'file', 'os.py'))
print(os.path.split(__file__)) # (path, basename)
print(os.path.splitext(__file__)) # (path + basename, .ext)
