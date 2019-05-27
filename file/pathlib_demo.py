# https://docs.python.org/3/library/pathlib.html#module-pathlib

# Correspondence to tools in the os module
# https://docs.python.org/3/library/pathlib.html#correspondence-to-tools-in-the-os-module

### Path
from pathlib import Path

Path.cwd()
__file__

# Listing subdirectories:
p = Path('.')
for dir in p.iterdir():
  if dir.is_dir():
    pass
[dir for dir in p.iterdir() if dir.is_dir()]

# Listing Python source files in this directory tree:
list(p.glob('**/*.py'))

# Navigating inside a directory tree:
p / 'lib'

# Querying path properties:
p.exists()
p.is_dir()
p.is_file()
p.stat()
p.resolve() # Make the path absolute, resolving any symlinks. A new path object is returned.
# p.mkdir('sub_folder')
# p.rename('new_name.py')

# Opening a file:
q = p / 'lib' / 'main.py'
with open(q) as f: f.readline()


### PurePath

from pathlib import PurePath

p = PurePath(__file__)

p.parent
p.parents[0]

p.joinpath('test', 'demo.py')
p.as_uri() # 'file://.../pathlib_demo.py'

p.name # pathlib_demo.py
p.with_name('demo.py') # replace filename with same path.
p.suffix # .py
p.with_suffix('.pyc') # replace file suffix.
p.stem # pathlib_demo, filename without suffix.
