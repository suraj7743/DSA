import os 
import datetime as datetime

os.chdir('/home/suraj/Desktop/Django')
# os.mkdir('sample')# mkdir make top level directory 
# os.makedirs('sample/sample.py')# makedirs make all sub level diretory 

# os.rename('original_name.txt','new_name.txt')
# os.stat('demo.txt') # this gives the description of the file  like size, last modification time etc 
# os.path.join(os.getcwd(), 'another_location')# it join the path for all os 
# os.path.basename('sample/test.txt')# it gives base file name => test.txt
# os.path.dirname('sample/test.txt')# it gives base directory  name => sample.txt
# os.path.split('sample/test.txt')# it split both  base directory and file  name => [sample, /test.txt]
# os.path.exists('sample/test.txt')# it check whether that path exists or not 
# os.path.isdir('sample/test.txt') # it check whether given path is directory or not 
# os.path.isfile('sample/test.txt')# it check whether given path is file or not 
# os.path.splitext('sample/test.txt')# it check for extension =>('sample/test', '.txt')

# os.walk ()gives the all file folder tree information till it reaches last node 
# for dirpath, dirname, filename in os.walk('/home/suraj/Desktop/Django'):
#     print('current path', dirpath)
#     print('dirname', dirname)
#     print('File', filename)
#     print()
# os.rmdir('sample')# to remove the directory 
print(os.environ.get('HOME'))
print(dir(os))# gives all function related to os 
print(dir(os.path))# gives all function that can be used with os.path