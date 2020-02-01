#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time: 2020-02-01 17:13
# @Project: anti-censorship
# @Version: 2020.02 builder 011713
# @Author: Peter Ren
# @Email: cnprogrammer@126.com
# @Github: https://github.com/cnprogrammer2019
# @Site: http://renpeter.com
# @File : interfere.py
# @Software: PyCharm
"""
有些网站贴图会有一些莫名其妙的审查，采用一定的策略可以规避被错杀
"""

import random
import copy

from PIL import ImageDraw

MIN_COLOR = 0
MAX_COLOR = 255
COLOR_RANGE = MAX_COLOR - MIN_COLOR + 1
MIDDLE_COLOR = int(COLOR_RANGE / 2)
MAX_ROTATE_DEGREE = 360
STANDARD_NOISE_DENSE = 0.3


def add_noise_lines_to_image(source_image, noise_dense=STANDARD_NOISE_DENSE,
                             start_color={'r': MIN_COLOR, 'g': MIN_COLOR, 'b': MIN_COLOR},
                             end_color={'r': MAX_COLOR, 'g': MAX_COLOR, 'b': MAX_COLOR}):
    """
    随机增加噪音线段在图片上
    :param source_image:原始图
    :param noise_dense: 加噪密度
    :param start_color: 开始颜色
    :param end_color: 截止颜色
    :return:
    """
    start_color_r, end_color_r = min(start_color['r'] % COLOR_RANGE, end_color['r'] % COLOR_RANGE), max(
        start_color['r'] % COLOR_RANGE, end_color['r'] % COLOR_RANGE)
    start_color_g, end_color_g = min(start_color['g'] % COLOR_RANGE, end_color['g'] % COLOR_RANGE), max(
        start_color['g'] % COLOR_RANGE, end_color['g'] % COLOR_RANGE)
    start_color_b, end_color_b = min(start_color['b'] % COLOR_RANGE, end_color['b'] % COLOR_RANGE), max(
        start_color['b'] % COLOR_RANGE, end_color['b'] % COLOR_RANGE)

    cut_dense = noise_dense
    if cut_dense < 0:
        cut_dense = 0

    image = copy.deepcopy(source_image)
    width, height = image.size

    print(width, height)

    line_number = int(max(width, height) * cut_dense) if cut_dense > 0 else 0
    print(line_number)

    points = []  # 随机点阵
    for index in range(0, line_number):
        point = (random.randint(0, width), random.randint(0, height))
        points.append(point)

    if cut_dense > 0:
        # 刮花
        draw_action = ImageDraw.Draw(image)
        random_line_pair_number = int(len(points) / 2)
        for index in range(0, random_line_pair_number):
            new_color = []
            new_color.append(random.randint(start_color_r, end_color_r))
            new_color.append(random.randint(start_color_g, end_color_g))
            new_color.append(random.randint(start_color_b, end_color_b))
            draw_action.line(
                [points[index][0], points[index][1], points[-index][0], points[-index][1]],
                fill=(new_color[0], new_color[1], new_color[2])
            )
            draw_action.arc(
                [points[index][0], points[index][1], points[-index][0], points[-index][1]],
                random.randint(0, 360), random.randint(0, 360),
                fill=(new_color[0], new_color[1], new_color[2])
            )

    return image


def add_noise_points_to_image(source_image, noise_dense=STANDARD_NOISE_DENSE,
                              start_color={'r': MIN_COLOR, 'g': MIN_COLOR, 'b': MIN_COLOR},
                              end_color={'r': MAX_COLOR, 'g': MAX_COLOR, 'b': MAX_COLOR}):
    """
    在原始图上，随机计算位置进行加噪音处理
    :param source_image: 原始图
    :param noise_dense: 噪点密度
    :param start_color: 噪点的开始颜色
    :param end_color: 噪点的截止颜色
    :return:
    """
    try:
        start_color_r, end_color_r = min(start_color['r'] % COLOR_RANGE, end_color['r'] % COLOR_RANGE), max(
            start_color['r'] % COLOR_RANGE, end_color['r'] % COLOR_RANGE)
        start_color_g, end_color_g = min(start_color['g'] % COLOR_RANGE, end_color['g'] % COLOR_RANGE), max(
            start_color['g'] % COLOR_RANGE, end_color['g'] % COLOR_RANGE)
        start_color_b, end_color_b = min(start_color['b'] % COLOR_RANGE, end_color['b'] % COLOR_RANGE), max(
            start_color['b'] % COLOR_RANGE, end_color['b'] % COLOR_RANGE)

        image = copy.deepcopy(source_image)
        image_width, image_height = image.size
        # 创建画笔对象
        draw = ImageDraw.Draw(image)
        # 调用画笔的point()函数绘制噪点
        noisy_number = int(image_height * image_width * noise_dense)
        for i in range(0, noisy_number):
            xy = (random.randrange(0, image_width), random.randrange(0, image_height))
            fill = (random.randrange(start_color_r, end_color_r),
                    random.randrange(start_color_g, end_color_g),
                    random.randrange(start_color_b, end_color_b))
            draw.point(xy, fill=fill)

        # 释放画笔
        del draw

        return image
    except Exception as e:
        return None


def add_random_points_to_image(source_image, noise_dense=STANDARD_NOISE_DENSE,
                               color={'r': MIDDLE_COLOR, 'g': MIDDLE_COLOR, 'b': MIDDLE_COLOR}):
    """
    增加随机噪点到图像上
    :param source_image:原始图
    :param noise_dense:噪点密度
    :param color:指定颜色
    :return:
    """
    try:
        color_r = color['r'] % COLOR_RANGE
        color_g = color['g'] % COLOR_RANGE
        color_b = color['b'] % COLOR_RANGE

        image = copy.deepcopy(source_image)
        image_width, image_height = image.size
        # 创建画笔对象
        draw = ImageDraw.Draw(image)
        # 调用画笔的point()函数绘制噪点
        noisy_number = int(image_height * image_width * noise_dense)
        for i in range(0, noisy_number):
            xy = (random.randrange(0, image_width), random.randrange(0, image_height))
            draw.point(xy, fill=(color_r, color_g, color_b))

        # 释放画笔
        del draw

        return image
    except Exception as e:
        return None


def add_points_to_image(source_image, noise_points=[(0, 0)],
                        color={'r': MIDDLE_COLOR, 'g': MIDDLE_COLOR, 'b': MIDDLE_COLOR}):
    """
    增加噪点到图像上
    :param source_image: 原始图
    :param noise_points: 点数据数组
    :param color: 指定颜色
    :return:
    """
    try:
        color_r = color['r'] % COLOR_RANGE
        color_g = color['g'] % COLOR_RANGE
        color_b = color['b'] % COLOR_RANGE

        image = copy.deepcopy(source_image)
        # 创建画笔对象
        draw = ImageDraw.Draw(image)
        # 调用画笔的point()函数绘制噪点
        draw.point(noise_points, fill=(color_r, color_g, color_b))

        # 释放画笔
        del draw

        return image
    except Exception as e:
        return None
