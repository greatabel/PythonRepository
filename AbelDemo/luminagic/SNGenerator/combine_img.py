import numpy as np
import PIL
from PIL import Image


list_im =  [
    'sns/M0BGDK15000101PLOWCHD52329b30.jpg', 
    'sns/M0BGDK15000301ST9VEMKZUV41ca4.jpg',
    'sns/M0BGDK15000401MGWCC5NKLPdc207.jpg',
    'sns/M0BGDK15000501YJHQGEFWQE8769d.jpg']
imgs    = [ PIL.Image.open(i) for i in list_im ]
# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

# save that beautiful picture
imgs_comb = PIL.Image.fromarray( imgs_comb)
imgs_comb.save( 'sns/Trifecta.jpg' )    

# for a vertical stacking it is simple: use vstack
imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
imgs_comb = PIL.Image.fromarray( imgs_comb)
imgs_comb.save( 'sns/Trifecta_vertical.jpg' )