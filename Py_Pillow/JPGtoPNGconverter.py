import sys
import os
from PIL import Image

path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)

count = 0
for filename in os.listdir(path):
	count += 1	
	clean_name = os.path.splitext(filename)[0]
	img = Image.open('{}{}'.format(path,filename))
	#added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
	#img.save('{}/{}.png'.format(directory, clean_name), 'png')
	print('all done!')