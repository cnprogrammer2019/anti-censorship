#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time: 2020-02-01 17:16
# @Project: anti-censorship
# @Version: 2020.02 builder 011716
# @Author: Peter Ren
# @Email: cnprogrammer@126.com
# @Github: https://github.com/cnprogrammer2019
# @Site: http://renpeter.com
# @File : sample.py
# @Software: PyCharm


import lib.interfere as ii
from PIL import Image


image_file_path = r'image/s.jpeg'
old_image = Image.open(image_file_path)
saved_image_quality = 10

# 加线
new_image = ii.add_noise_lines_to_image(old_image, noise_dense=0.5, start_color={'r': 0, 'g': 0, 'b': 0})
new_image.show()
new_image.save('s0.jpeg', quality=saved_image_quality)

# 加随机噪点1
new_image = ii.add_noise_points_to_image(old_image, noise_dense=0.15)
new_image.show()
new_image.save('s1.jpeg', quality=saved_image_quality)

# 将指定颜色变换为指定颜色，效果不明显
# new_image = imgf.reset_color(old_image, source_color=(0, 0, 0), destension_color=(255, 255, 255, 255))
# new_image.show()

# 将指定颜色变换为随机，效果不明显
# new_image = imgf.reset_random_color(old_image, source_color=(0, 0, 0))
# new_image.show()

# 固定噪点
new_image = ii.add_random_points_to_image(old_image, noise_dense=0.3)
new_image.save('s2.jpeg', quality=saved_image_quality)
noise_points = []
for h in range(960):
    for v in range(540):
        noise_points.append((h * 2, v * 3))

new_image = ii.add_points_to_image(new_image, noise_points, color={'r': 127, 'b': 127, 'g': 127})
new_image.show()
new_image.save('s3.jpeg', quality=saved_image_quality)
