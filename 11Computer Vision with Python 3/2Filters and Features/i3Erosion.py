from skimage import morphology
from skimage import io, data

img = data.camera()
eroded_img = morphology.binary_erosion(img)

io.imshow(eroded_img)
io.show()
