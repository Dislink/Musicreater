# -*- coding: utf-8 -*-


# 音·创 开发交流群 861684859
# Email EillesWan2006@163.com W-YI_DoctorYI@outlook.com EillesWan@outlook.com
# 版权所有 金羿("Eilles Wan") & 诸葛亮与八卦阵("bgArray") & 鸣凤鸽子("MingFengPigeon")
# 若需转载或借鉴 许可声明请查看仓库目录下的 Lisence.md


"""
音·创 库版 MIDI转换展示程序
Musicreater Package Version : Demo for Midi Conversion

Copyright 2023 all the developers of Musicreater

开源相关声明请见 ./Lisence.md
Terms & Conditions: ./Lisence.md
"""

from msctPkgver.main import *
import os

convertion = midiConvert()

while True:
    midipath = input('请输入midi文件路径：')
    if os.path.exists(midipath):
        break
    else:
        print('文件不存在，请重新输入')

outpath = input('请输入输出路径：')

if not os.path.exists(outpath):
    os.makedirs(outpath)

while True:
    try:
        outFormat = int(input('请输入输出格式(0:mcpack|1:BDX结构)：'))
        if outFormat == 0:
            isAutoReset = input('是否自动重置计分板(1|0)：')
            if isAutoReset != '':
                isAutoReset = bool(int(isAutoReset))
            while True:
                isProgress = input('*进度条[本Demo不支持自定义]：')
                if isProgress != '':
                    if isProgress in ('1', 'True'):
                        isProgress = True
                    elif isProgress in ('0', 'False'):
                        isProgress = False
                    else:
                        isProgress = isProgress
                else:
                    continue
                break
            sbname = input('请输入计分板名称：')
            volume = input('请输入音量（0-1）：')
            if volume != '':
                volume = float(volume)
            speed = input('请输入速度倍率：')
            if speed != '':
                speed = float(speed)
        elif outFormat == 1:
            author = input('请输入作者：')
            while True:
                isProgress = input('*进度条[本Demo不支持自定义]：')
                if isProgress != '':
                    if isProgress in ('1', 'True'):
                        isProgress = True
                    elif isProgress in ('0', 'False'):
                        isProgress = False
                    else:
                        isProgress = isProgress
                else:
                    continue
                break
            maxHeight = input('请输入指令结构最大生成高度：')
            if maxHeight != '':
                maxHeight = int(maxHeight)
            sbname = input('请输入计分板名称：')
            volume = input('请输入音量（0-1）：')
            if volume != '':
                volume = float(volume)
            speed = input('请输入速度倍率：')
            if speed != '':
                speed = float(speed)
            isAutoReset = input('是否自动重置计分板(1|0)：')
            if isAutoReset != '':
                isAutoReset = bool(int(isAutoReset))
        break
    except BaseException:
        print('输入错误，请重新输入')




m = 1
'''采用的算法编号'''


if os.path.isdir(midipath):
    for i in os.listdir(midipath):
        if i.lower().endswith('.mid'):
            print(f'正在操作{i}')
            convertion.convert(midipath + '/' + i, outpath + '/' + i[:-4])
            if outFormat == 0:
                print(convertion.tomcpack(
                    m,
                    isAutoReset
                    if isAutoReset != ''
                    else bool(int(input('是否自动重置计分板(1|0)：'))),
                    isProgress,
                    sbname if sbname != '' else input('请输入计分板名称：'),
                    volume if volume != '' else float(input('请输入音量（0-1）：')),
                    speed if speed != '' else float(input('请输入速度倍率：')),
                ))
            elif outFormat == 1:
                print(convertion.toBDXfile(
                    m,
                    author if author != '' else input('请输入作者：'),
                    isProgress,
                    maxHeight if maxHeight != '' else int(input('请输入指令结构最大生成高度：')),
                    sbname if sbname != '' else input('请输入计分板名称：'),
                    volume if volume != '' else float(input('请输入音量（0-1）：')),
                    speed if speed != '' else float(input('请输入速度倍率：')),
                    isAutoReset
                    if isAutoReset != ''
                    else bool(int(input('是否自动重置计分板(1|0)：'))),
                ))
else:
    convertion.convert(midipath, outpath)
    if outFormat == 0:
        print(convertion.tomcpack(
            m,
            isAutoReset if isAutoReset != '' else bool(int(input('是否自动重置计分板(1|0)：'))),
            isProgress,
            sbname if sbname != '' else input('请输入计分板名称：'),
            volume if volume != '' else float(input('请输入音量（0-1）：')),
            speed if speed != '' else float(input('请输入速度倍率：')),
        ))
    elif outFormat == 1:
        print(convertion.toBDXfile(
            m,
            author if author != '' else input('请输入作者：'),
            isProgress,
            maxHeight if maxHeight != '' else int(input('请输入指令结构最大生成高度：')),
            sbname if sbname != '' else input('请输入计分板名称：'),
            volume if volume != '' else float(input('请输入音量（0-1）：')),
            speed if speed != '' else float(input('请输入速度倍率：')),
            isAutoReset if isAutoReset != '' else bool(int(input('是否自动重置计分板(1|0)：'))),
        ))