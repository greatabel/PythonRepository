import multiprocessing as mp
import cv2
import time


from gluoncv import model_zoo, data, utils
#from matplotlib import pyplot as plt
import mxnet as mx
import cv2
import argparse
from imutils import paths
from imutils.video import FileVideoStream

import numpy as np
from matplotlib import pyplot as plt
import webcolors
from sklearn.cluster import KMeans
import os
import pickle

def parse_args():
    parser = argparse.ArgumentParser(description='Train YOLO networks with random input shape.')
    parser.add_argument('--network', type=str, default='yolo3_darknet53_voc',
                        #use yolo3_darknet53_voc, yolo3_mobilenet1.0_voc, yolo3_mobilenet0.25_voc 
                        help="Base network name which serves as feature extraction base.")
    parser.add_argument('--short', type=int, default=416,
                        help='Input data shape for evaluation, use 320, 416, 512, 608, '                  
                        'larger size for dense object and big size input')
    parser.add_argument('--threshold', type=float, default=0.4,
                        help='confidence threshold for object detection')

    parser.add_argument('--gpu', type=bool, default=False,
                        help='use gpu or cpu.')
    
    args = parser.parse_args()
    return args


def image_put(q, user, pwd, ip, channel=1):
    # 用视频临时代替实时读取
    cap = cv2.VideoCapture("demo.mp4" )

    # 默认小车车载摄像头
    # cap = cv2.VideoCapture(0)

    # 如果是网络摄像头
    # if cap.isOpened():
    #     print('HIKVISION')
    # else:
    #     cap = cv2.VideoCapture("rtsp://%s:%s@%s/cam/realmonitor?channel=%d&subtype=0" % (user, pwd, ip, channel))
    #     print('DaHua')

    while True:
        q.put(cap.read()[1])
        #q.get() if q.qsize() > 1 else time.sleep(0.01)
        q.get() if q.qsize() > 5 else time.sleep(0.01)


# def render_as_image(a):
#     img = a.asnumpy() # convert to numpy array
#     img = img.transpose((1, 2, 0))  # Move channel to the last dimension
#     img = img.astype(np.uint8)  # use uint8 (0-255)

#     plt.imshow(img)
#     # plt.show()
#     import random
#     int_name = str(random.randint(1,10))
#     plt.savefig(int_name + '.png')

def closest_colour(requested_colour):
    min_colours = {}

    # for key, name in webcolors.css3_hex_to_names.items():
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

# https://stackoverflow.com/questions/43216772/how-to-check-rgb-colors-against-a-color-range
# TARGET_COLORS = {"red": (255, 0, 0), "yellow": (255, 255, 0), "green": (0, 255, 0)}

# def color_difference (color1, color2):
#     return sum([abs(component1-component2) for component1, component2 in zip(color1, color2)])


def forked_version_cv_plot_bbox(img, bboxes, scores=None, labels=None, thresh=0.5,
                 class_names=None, colors=None,
                 absolute_coordinates=True, scale=1.0):
    """Visualize bounding boxes with OpenCV.

    Parameters
    ----------
    img : numpy.ndarray or mxnet.nd.NDArray
        Image with shape `H, W, 3`.
    bboxes : numpy.ndarray or mxnet.nd.NDArray
        Bounding boxes with shape `N, 4`. Where `N` is the number of boxes.
    scores : numpy.ndarray or mxnet.nd.NDArray, optional
        Confidence scores of the provided `bboxes` with shape `N`.
    labels : numpy.ndarray or mxnet.nd.NDArray, optional
        Class labels of the provided `bboxes` with shape `N`.
    thresh : float, optional, default 0.5
        Display threshold if `scores` is provided. Scores with less than `thresh`
        will be ignored in display, this is visually more elegant if you have
        a large number of bounding boxes with very small scores.
    class_names : list of str, optional
        Description of parameter `class_names`.
    colors : dict, optional
        You can provide desired colors as {0: (255, 0, 0), 1:(0, 255, 0), ...}, otherwise
        random colors will be substituted.
    absolute_coordinates : bool
        If `True`, absolute coordinates will be considered, otherwise coordinates
        are interpreted as in range(0, 1).
    scale : float
        The scale of output image, which may affect the positions of boxes

    Returns
    -------
    numpy.ndarray
        The image with detected results.

    """
    


    if labels is not None and not len(bboxes) == len(labels):
        raise ValueError('The length of labels and bboxes mismatch, {} vs {}'
                         .format(len(labels), len(bboxes)))
    if scores is not None and not len(bboxes) == len(scores):
        raise ValueError('The length of scores and bboxes mismatch, {} vs {}'
                         .format(len(scores), len(bboxes)))

    if isinstance(img, mx.nd.NDArray):
        img = img.asnumpy()
    if isinstance(bboxes, mx.nd.NDArray):
        bboxes = bboxes.asnumpy()
    if isinstance(labels, mx.nd.NDArray):
        labels = labels.asnumpy()
    if isinstance(scores, mx.nd.NDArray):
        scores = scores.asnumpy()
    if len(bboxes) < 1:
        return img

    if not absolute_coordinates:
        # convert to absolute coordinates using image shape
        height = img.shape[0]
        width = img.shape[1]
        bboxes[:, (0, 2)] *= width
        bboxes[:, (1, 3)] *= height
    else:
        bboxes *= scale


    # use random colors if None is provided
    if colors is None:
        colors = dict()
    for i, bbox in enumerate(bboxes):
        if scores is not None and scores.flat[i] < thresh:
            continue
        if labels is not None and labels.flat[i] < 0:
            continue
        cls_id = int(labels.flat[i]) if labels is not None else -1
        if cls_id not in colors:
            if class_names is not None:
                colors[cls_id] = plt.get_cmap('hsv')(cls_id / len(class_names))
                # print(cls_id, ' @-> ', colors[cls_id])
            else:
                colors[cls_id] = (random.random(), random.random(), random.random())
                # print(cls_id, '-> ', colors[cls_id])
        xmin, ymin, xmax, ymax = [int(x) for x in bbox]
        # ---- 裁减到识别区域
        
        crop_img = img[ymin:ymax-int(int((ymax-ymin)/2)), xmin+int((xmax-xmin)/4):xmax-int((xmax-xmin)/4)]
        # crop_img = img[ymin:ymax, xmin:xmax]



        # print('crop_img.shape=', crop_img.shape)
        # mydata = np.reshape(crop_img, (-1,3))

        colorname = ''
        dominant_color = None
        # if mydata.shape[0] > 0:
        #     mydata = np.float32(mydata)

        #     criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        #     flags = cv2.KMEANS_RANDOM_CENTERS
        #     compactness,mylabels,centers = cv2.kmeans(mydata,1,None,criteria,10,flags)
        #     colorname = closest_colour(centers[0].astype(np.int32))
        #     dominant_color = centers[0].astype(np.int32)
        #     print('Dominant color is: bgr({})'.format(dominant_color))
        #     print('Dominant color is: bgr({})'.format(colorname))

        #reshaping to a list of pixels
        crop_img = crop_img.reshape((crop_img.shape[0] * crop_img.shape[1], 3))
        if len(crop_img) > 0:
            
            #using k-means to cluster pixels
            kmeans = KMeans(n_clusters = 1)
            kmeans.fit(crop_img)
            dominant_color = kmeans.cluster_centers_.astype(np.int32)[0]
            colorname = closest_colour(dominant_color)
            print(dominant_color, colorname)

            # differences = [[color_difference(dominant_color, target_value), target_name] for target_name, target_value in TARGET_COLORS.items()]
            # differences.sort()  # sorted by the first element of inner lists
            # my_color_name = differences[0][1]

            # print(my_color_name)
            # 因为centers传出的是bgr，需要改变顺序为 rgb
            # t = cv2.cvtColor(centers[0], cv2.COLOR_BGR2RGB).astype(np.int32)[0][0]
            # print('# color is: bgr({})'.format(t))
            # colorname = closest_colour(centers[0].astype(np.int32))

            # print('Dominant color is: bgr({})'.format(colorname))

        # from PIL import Image
        # new_img = Image.fromarray(crop_img, 'RGB')

        # plt.imshow(crop_img)
        # # plt.show()
        # import random
        # int_name = str(random.randint(1,10))
        # plt.savefig(int_name + '.png')
        # 识别颜色
        # from colorthief import ColorThief
        # color_thief = ColorThief(new_img)
        # # get the dominant color
        # dominant_color = color_thief.get_color(quality=1)
        # print(dominant_color, type(dominant_color))

        # # ----
        # bcolor = [x * 255 for x in colors[cls_id]]
        bcolor = (255, 255, 255) 
        # 默认设置为黄色，根据视频
        bcolor = (255,255,0)
        

        # cv2.rectangle(img, (xmin, ymin), (xmax, ymax), bcolor, 2)

        if class_names is not None and cls_id < len(class_names):
            class_name = class_names[cls_id]
        else:
            class_name = str(cls_id) if cls_id >= 0 else ''
        score = '{:d}%'.format(int(scores.flat[i]*100)) if scores is not None else ''
        warning_signal = None
        if class_name == 'person':
            print(scores.flat[i], '#'*10)
            #天蓝色
            bcolor =(0, 255, 255)
            if scores.flat[i] > 0.71:
                
                warning_signal = 'person'
                
                cv2.rectangle(img, (xmin, ymin), (xmax, ymax), bcolor, 2)
                y = ymin - 15 if ymin - 15 > 15 else ymin + 15
                cv2.putText(img, '{:s} {:s}'.format(class_name, score),
                    (xmin, y), cv2.FONT_HERSHEY_SIMPLEX, min(scale/2, 2),
                    bcolor, min(int(scale), 5), lineType=cv2.LINE_AA)

        elif class_name == 'hat':
            print(scores.flat[i], '^'*20)
            bcolor = (255,255,0)
            if scores.flat[i] > 0.65:
                if colorname in ('olivedrab', 'yellow', 'sienna','goldenrod', 'gold','palegoldenrod',
                 'darkgoldenrod','greenyellow','khaki','darkkhaki','blanchedalmond', 'wheat'):               
                    # 黄色
                    bcolor = (255,255,0)
                    # 警告音 
                    # duration = 0.5  # seconds
                    # freq = 660  # Hz
                    # os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
                    # logger.log(logging.CRITICAL, 'yellow-hat-in-area')

               
                    warning_signal = 'hat'
                    print('yhat', '@'*30)
                    # print('#'*10)

                elif colorname in ('saddlebrown', 'red', 'maroon','darkred','indianred','firebrick','brown','crimson'):
                    # 红色
                    bcolor =  (0, 0, 255)
                    # 警告音 
                    # duration = 1  # seconds
                    # freq = 440  # Hz
                    # os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
                    # logger.log(logging.CRITICAL, 'red-hat-in-area')
                    
                    warning_signal = 'red-hat'

                cv2.rectangle(img, (xmin, ymin), (xmax, ymax), bcolor, 2)
                y = ymin - 15 if ymin - 15 > 15 else ymin + 15
                cv2.putText(img, '{:s} {:s}'.format(class_name, score),
                    (xmin, y), cv2.FONT_HERSHEY_SIMPLEX, min(scale/2, 2),
                    bcolor, min(int(scale), 5), lineType=cv2.LINE_AA)
                # print('#'*20)
        print(warning_signal)

        # --------- share data -------
        shared = {"detected": warning_signal}
        fp = open("shared.pkl","wb")
        pickle.dump(shared, fp)
        # --------- share data end -------
    return img

def image_get(q, window_name):
    global images_prepares
    frame_index = 0


    args = parse_args()
    # print('是否使用GPU:', args.gpu)
    if args.gpu:
        ctx = mx.gpu()
        # print('here gpu')
    else:
        ctx = mx.cpu()
    # ctx = mx.cpu()

    net = model_zoo.get_model(args.network, pretrained=False)
    
    classes = ['hat', 'person']
    for param in net.collect_params().values():
        if param._data is not None:
            continue
        param.initialize()
    net.reset_class(classes)
    net.collect_params().reset_ctx(ctx)

    if args.network == 'yolo3_darknet53_voc':
        net.load_parameters('darknet.params',ctx=ctx)
        print('use darknet to extract feature')
    elif args.network == 'yolo3_mobilenet1.0_voc':
        net.load_parameters('mobilenet1.0.params',ctx=ctx)
        print('use mobile1.0 to extract feature')
    else:
        net.load_parameters('mobilenet0.25.params',ctx=ctx)
        print('use mobile0.25 to extract feature')

    # cv2.namedWindow(window_name, flags=cv2.WINDOW_FREERATIO)
    while True:
        frame = q.get()
        # cv2.imshow(window_name, frame)
        # cv2.waitKey(1)

        

            
        # frame = '1.jpg'
        # x, orig_img = data.transforms.presets.yolo.load_test(frame, short=args.short)
        # x = x.as_in_context(ctx)
        # box_ids, scores, bboxes = net(x)
        # ax = utils.viz.cv_plot_bbox(orig_img, bboxes[0], scores[0], box_ids[0], class_names=net.classes,thresh=args.threshold)
        # cv2.imshow('image', orig_img[...,::-1])
        # cv2.waitKey(0)
        # cv2.imwrite(frame.split('.')[0] + '_result.jpg', orig_img[...,::-1])
        # cv2.destroyAllWindows()
        count = 0

            

        if frame is not None:

            # Image pre-processing
            new_frame = mx.nd.array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).astype('uint8')

            # x, orig_img = data.transforms.presets.yolo.load_test(frame, short=args.short)
            # x, orig_img = data.transforms.presets.yolo.transform_test(new_frame, short=args.short)
            x, orig_img = data.transforms.presets.yolo.transform_test(new_frame,  short=512, max_size=2000)
            # print('Shape of pre-processed image:', x.shape)
            x = x.as_in_context(ctx)
            box_ids, scores, bboxes = net(x)

            # render_as_image(bboxes)
            # ---
            # if isinstance(bboxes[0], mx.nd.NDArray):

            #     bboxes_a = bboxes[0].asnumpy()
            # for i, bbox in enumerate(bboxes_a):
            #     xmin, ymin, xmax, ymax = [int(x) for x in bbox]
            #     print(xmin, ymin, xmax, ymax)
            #     if xmin > -1 :
            #         cv2.rectangle(orig_img, (xmin, ymin), (xmax, ymax), 122, 2)



            # for idx in range(len(bboxes.asnumpy())):
            #     x, y, w, h = cv2.boundingRect(bboxes.asnumpy()[idx])
            #     mask[y:y+h, x:x+w] = 0
            #     print("Box {0}: ({1},{2}), ({3},{4}), ({5},{6}), ({7},{8})".format(idx,x,y,x+w,y,x+w,y+h,x,y+h))
            #     cv2.drawContours(mask, bboxes.asnumpy(), idx, (255, 255, 255), -1)
            #     r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)

            #----


            # ax = utils.viz.cv_plot_bbox(orig_img, bboxes[0], scores[0], box_ids[0], class_names=net.classes,thresh=args.threshold)
            x = forked_version_cv_plot_bbox(orig_img, bboxes[0], scores[0], box_ids[0], 
                                            class_names=net.classes,thresh=args.threshold)

            # x = origin_cv_plot_bbox(orig_img, bboxes[0], scores[0], box_ids[0], 
            #                                 class_names=net.classes,thresh=args.threshold)

            # print('#'*10, type(bboxes), bboxes.shape)
            # 让窗口可以调整
            images_prepares.append(orig_img[...,::-1])
            # print(len(images_prepares), 'prepare')
            # cv2.imwrite('screenshots/' + str(len(images_prepares))+'.jpg',orig_img[...,::-1])
            # if len(images_prepares) == 46:
            #     size = (512, 910)
            #     video_write = cv2.VideoWriter("output_video.avi", cv2.VideoWriter_fourcc('M','J','P','G'), 25, size, False)
            #     for image in images_prepares:
            #         print(image.size)
            #         video_write.write(image)
            #     print('finished video_write')
            cv2.namedWindow("image", cv2.WINDOW_NORMAL)
            cv2.imshow('image', orig_img[...,::-1])
            # print(type(orig_img[...,::-1]))
            if cv2.waitKey(1) == 27:
                    break
            # count += 8
            # cap.set(1, count)





images_prepares = []

def run_single_camera():

    # user_name, user_pwd, camera_ip = "admin", "admin123", "10.248.10.100:554"
    user_name, user_pwd, camera_ip = "admin", "admin123", "10.248.10.100:554"
# admin:yxgl123456@192.168.200.153:554
    mp.set_start_method(method='spawn')  # init
    queue = mp.Queue(maxsize=2)
    processes = [mp.Process(target=image_put, args=(queue, user_name, user_pwd, camera_ip)),
                 mp.Process(target=image_get, args=(queue, camera_ip))]

    [process.start() for process in processes]
    [process.join() for process in processes]
    



if __name__ == '__main__':
    # python3 i3rstp_color_video.py --gpu=True --network=yolo3_darknet53_voc
    run_single_camera()

    pass
