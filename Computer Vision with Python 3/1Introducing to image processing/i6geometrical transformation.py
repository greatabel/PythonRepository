from PIL import Image


img = Image.open('images/image.jpg')

resize_img = img.resize((200,200))
resize_img.show()