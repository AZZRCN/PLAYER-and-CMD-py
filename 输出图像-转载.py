"""
-------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020/10/1 15:44:12
# @Author  : Giyn
# @Email   : giyn.jy@gmail.com
# @File    : video_processing.py
# @Software: PyCharm
-------------------------------------
"""

import cv2
#import logging

# log information settings
#logging.basicConfig(level=logging.INFO,
#                    format='%(asctime)s - %(levelname)s: %(message)s')


def save_image(num, image):
    """Save the images.

    Args:
        num: serial number
        image: image resource

    Returns:
        None
    """
    image_path = f'{num}.jpg'
    cv2.imwrite(image_path, image)


file_path = "强风大背头.mp4"

vc = cv2.VideoCapture(file_path)  # import video files

# determine whether to open normally
if vc.isOpened():
    ret, frame = vc.read()
else:
    #ret = False
    vc.release()
    exit()

count = 0  # count the number of pictures
#frame_interval = 1  # video frame count interval frequency
#frame_interval_count = 0

# loop read video frame
while ret and count <= 1000:
    ret, frame = vc.read()
    # store operation every time f frame
    #if frame_interval_count % frame_interval == 0:
    #    save_image(count, frame)
    #    print(frame_interval_count)
    #    count += 1
    save_image(count,frame)
    print(count)
    count += 1
    #frame_interval_count += 1
    #cv2.waitKey(1)

vc.release()