from skimage import io, color


img = io.imread('images/image.jpg')
gray = color.rgb2gray(img)
io.imshow(gray)
io.show()