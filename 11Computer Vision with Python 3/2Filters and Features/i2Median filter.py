from PIL import Image
from PIL import ImageFilter


img = Image.open("images/image.jpg")
blur_img = img.filter(ImageFilter.MedianFilter(7))
blur_img.show()