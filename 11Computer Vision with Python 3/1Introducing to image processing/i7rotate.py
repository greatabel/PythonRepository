from PIL import Image

img = Image.open('images/image.jpg')

rotate_img = img.rotate(90)
rotate_img.show()