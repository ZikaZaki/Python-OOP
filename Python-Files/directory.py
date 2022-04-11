import os
import shutil

print(os.getcwd())

os.chdir('C:\\POS')
print(os.getcwd())
print(os.listdir())
print(os.listdir('C:\\'))

print(os.getcwd())
# os.mkdir('test')
print(os.listdir())

# os.rename('test', 'new_one')
print(os.listdir())

# os.rmdir('new_one') # Cannot remove none-empty directory
# shutil.rmtree('new_one')
print(os.listdir())

print(dir(locals()['__builtins__']))
