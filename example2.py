# -*- coding:utf-8 -*-
#图片相似度
from os import listdir
from PIL import Image


def getDiff(width, high, image):  # 将要裁剪成w*h的image照片 得到渐变序列
    diff = []
    im = image.resize((width, high))
    imgray = im.convert('L')  # 转换为灰度图片 便于处理
    pixels = list(imgray.getdata())  # 得到像素数据 灰度0-255
    print('test')
    print len(pixels)
    print pixels

    for row in range(high):
        rowStart = row * width  # 起始位置行号
        for index in range(width - 1):
            leftIndex = rowStart + index  # 当前位置号
            rightIndex = leftIndex + 1
            diff.append(pixels[leftIndex] > pixels[rightIndex])
    print('diff is ')
    print(diff)
    return diff

def getHamming(diff=[], diff2=[]):
    # print len(diff)
    hamming_distance = 0
    for i in range(len(diff)):
        if diff[i] != diff2[i]:
            hamming_distance += 1


    return hamming_distance

if __name__ == '__main__':
    width = 8
    high = 8
    dir_img = 'E:\\picture_process\\images'
    allDiff = []
    dirlist = listdir(dir_img)
    print dirlist
    cnt = 0
    for i in dirlist:
        cnt += 1
        print cnt
        # 文件后缀类型过滤
        if str(i).split('.')[-1] in ['jpg', 'png']:
            print ('%s\%s' % (dir_img, str(i)))
            im = Image.open(r'%s\%s' % (dir_img, unicode(str(i), "utf-8")))
            diff = getDiff(width, high, im)
            allDiff.append((str(i), diff))

    print('allDiff')
    print(allDiff)
    for i in range(len(allDiff)):
        for j in range(i + 1, len(allDiff)):
            if i != j:
                ans = getHamming(allDiff[i][1], allDiff[j][1])
                if ans <= 5:
                    print allDiff[i][0], "and", allDiff[j][0], "maybe same photo..."
