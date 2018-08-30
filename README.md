# pure_data
目录结构：
  videos（里边放置视频文件）
  images(初始空目录)
  video_cut.py
  vague_image.py
  
video_cut.py:视频切分图片，在ubuntu家目录执行命令（参数：视频目录，图片输出目录，贞/s）：python video_cut.py /home/ubuntu/videos /home/ubuntu/images/ 0.25

vague_image.py:去模糊图片已完成，在ubuntu家目录执行命令（参数：图片目录，阈值） python vague_image.py /home/ubuntu/images/ 50
