from PIL import Image
import os

for file in os.listdir('orig'):
	if file.endswith('.png'):
		image_file = Image.open(os.path.join('orig',file))
		print(type(image_file))
		image_file = image_file.convert('L')
		image_file.save(os.path.join('converted', file[:-4] + '_converted.png'))
		print(file)