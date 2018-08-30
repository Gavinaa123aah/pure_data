# -*- coding: UTF-8 -*-
import cv2
import os
import sys
import subprocess

def test(images_path,threshold):
    pure_path = []
    dirty_path = []
    count = 0
    for root, dirs, files in os.walk(images_path):
        if count == 0:
            for dir in dirs:
                pure_path.append(root+dir+'/pure')
                dirty_path.append(root+dir+'/dirty')
        count += 1

    print(pure_path)
    for single_pure_path, single_dirty_path in zip(pure_path,dirty_path):
        for root, dir, files in os.walk(single_pure_path):
            for image in files:
                print(image)
                img = cv2.imread(single_pure_path + '/' + image)
                img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # imgeVar的值决定了图片的模糊度。
                # imgeVar数值越大，图片越清晰
                imageVar = cv2.Laplacian(img2gray, cv2.CV_64F).var()
                print(imageVar)
                if imageVar < int(threshold):
                    result = subprocess.call('mv '+single_pure_path+'/'+image + ' ' + single_dirty_path, shell=True)
                    print(result)
if __name__ == '__main__':
    images_path = sys.argv[1]
    threshold = sys.argv[2]
    test(images_path, threshold)
