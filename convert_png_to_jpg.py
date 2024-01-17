import os
from PIL import Image

dir_in="VOCdevkit/VOC2007/JPEGImages/"
dir_out="VOCdevkit/VOC2007/new/"
names = os.listdir(dir_in)
count=0
for name in names:
  img=Image.open(dir_in+name)
  name=name.split('.')
  if name[-1] == 'png':
    name[-1] = 'jpg'
    name = str.join(".", name)
    out_f = dir_out + name
    img = img.convert('RGB')
    img.save(out_f)
    count+=1
    print(name)
  else:
    continue
print('转换完成！共转换了 %d 张图片' % (count))