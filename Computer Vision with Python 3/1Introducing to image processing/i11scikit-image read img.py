from skimage import io


img = io.imread('images/image.jpg')
print(img.shape)

io.imshow("images/image.jpg")
io.show()
