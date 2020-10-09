from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

box = (100, 100, 400, 400)
region = img.crop(box)
region.save('cropped.png', 'png')