# files/existence.py
from pathlib import Path

p = Path('fear.txt')
path = p.parent.absolute()

print(p.is_file()) # True
print(path) # should be an absolute path
print(path.is_dir()) # True

q = Path('C:\\Users\\pc\\Documents\\GitHub\\Learn-Python-Programming\\08. Files and Data Persistence\\files')
print(q.is_dir()) # True
