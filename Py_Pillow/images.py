from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

##print(img)
#print(dir(img))
# print(img.format)
# print(img.size)
# print(img.mode)

#covered to png since it supports this while jpg doesn't.
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png', 'png')

filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save('smooth.png', 'png')

filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save('sharpen.png', 'png')

filtered_img = img.convert('L')
filtered_img.save('grey.png', 'png')