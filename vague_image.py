# -*- coding: UTF-8 -*-
import cv2
import os
import sys
# for root, dir, files in os.walk('E:\\picture_process\\images'):
#     for image in files:
#         print(image)
#         image = cv2.imread('E:\\picture_process\\images\\' + image)
#         img2gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         # imgeVar的值决定了图片的模糊度。
#         # imgeVar数值越大，图片越清晰
#         imageVar = cv2.Laplacian(img2gray, cv2.CV_64F).var()
#         print(imageVar)

def test(images_path):
    pure_path = []
    count = 0
    for root, dirs, files in os.walk(images_path):
        if count == 0:
            for dir in dirs:
                pure_path.append(root+'/'+dir+'/pure')
        count += 1
    print(pure_path)
    for singgle_pure_path in pure_path:
        for root, dir, files in os.walk(pure_path):
            for image in files:
                print(image)
                image = cv2.imread(pure_path + '/' + image)
                img2gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                # imgeVar的值决定了图片的模糊度。
                # imgeVar数值越大，图片越清晰
                imageVar = cv2.Laplacian(img2gray, cv2.CV_64F).var()
                print(imageVar)


if __name__ == '__main__':
    images_path = sys.argv[1]
    test(images_path = images_path)