from skimage import io, data, color

img = data.astronaut()
img_hsv = color.rgb2hsv(img)
io.imshow(img_hsv)
io.show()