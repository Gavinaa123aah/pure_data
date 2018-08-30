# -*- coding: UTF-8 -*-
import sys
import os
import subprocess
def videos_cut(input_dir, output_dir, frequency):
    video_files = []
    out_dir_name = []
    #获取视频名称，以及视频的据对路径，存到列表里
    for root, dirs, files in os.walk(input_dir):
        for i in files:
            video_files.append(root+'/' + i)
            out_dir_name.append(i[:-4])

    # 在images下建立以视频名命名的目录
    for i in out_dir_name:
        result = subprocess.call('mkdir /home/ubuntu/images/'+i, shell=True)
        print(result)
        result = subprocess.call('mkdir /home/ubuntu/images/'+i+'/pure', shell=True)
        print(result)
        result = subprocess.call('mkdir /home/ubuntu/images/' + i + '/dirty', shell=True)
        print(result)
        result = subprocess.call('mkdir /home/ubuntu/images/' + i + '/duplicate', shell=True)
        print(result)

    #开始视频切分
    count = 0
    for video_file in video_files:
        print('ffmpeg -i ' + video_file + ' -r ' + str(frequency) + output_dir + '/' + out_dir_name[
            count] + '/pure/image_%06d.jpg')
        result = subprocess.call('ffmpeg -i ' + video_file + ' -r ' + str(frequency) + ' '+output_dir + '/' + out_dir_name[count] + '/pure/image_%06d.jpg', shell=True)
        print(result)
        count += 1

if __name__ == '__main__':
    print(len(sys.argv))
    if len(sys.argv) != 4:
        print('wrong parameter')
    else:
        videos_cut(sys.argv[1], sys.argv[2], sys.argv[3])
