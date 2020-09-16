from PIL import Image, ImageFilter

img = Image.open('./Pukedox/pikachu.jpg')
filtered_img = img.convert('L')
filtered_img.save('grey.png', 'png')
filtered_img = img.convert('RGB')
filtered_img.save('rgb.png', 'png')
