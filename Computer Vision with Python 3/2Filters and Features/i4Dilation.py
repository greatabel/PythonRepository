from skimage import morphology
from skimage import io,data
# http://scikit-image.org/docs/dev/api/skimage.data.html


img = data.checkerboard()
dilated_img = morphology.binary_dilation(img)

io.imshow(dilated_img)
io.show()