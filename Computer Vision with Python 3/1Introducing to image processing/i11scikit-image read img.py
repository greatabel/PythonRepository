from skimage import io



io.imshow("images/image.jpg")
io.show()

img = io.imread('images/image.jpg')
print(img.shape)

io.save("images/new_image.jpg", img)