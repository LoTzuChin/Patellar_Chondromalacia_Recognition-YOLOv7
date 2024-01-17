import os
import shutil

# 定义源文件夹路径
source_folder = 'VOCdevkit/VOC2007/JPEGImages'  # 假设源文件夹中包含图像文件

# 定义目标文件夹路径
destination_folder = 'img'  # 创建的目标文件夹路径

# 读取包含文件名的文本文件
with open('VOCdevkit/VOC2007/ImageSets/Main/test.txt', 'r') as f:
    image_filenames = f.read().splitlines()

# 创建目标文件夹
os.makedirs(destination_folder, exist_ok=True)

# 遍历文件名列表，将文件从源文件夹复制到目标文件夹
for image_filename in image_filenames:
    source_path = os.path.join(source_folder, image_filename + '.jpg')  # 假设文件是JPG格式
    destination_path = os.path.join(destination_folder, image_filename + '.jpg')

    # 复制文件
    shutil.copy(source_path, destination_path)

