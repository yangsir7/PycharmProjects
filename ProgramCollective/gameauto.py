import os
import math
# 这两个库用于图片的操作
import matplotlib.pyplot as plt
from PIL import Image


class WechatJump:
    def __init__(self):
        # 按压系数，不同分辨率的手机需要做调整
        self._coefficient = 2.05
        # 记录按压次数
        self._click_count = 0
        # 记录点击点坐标的数组
        self._coords = []

    def generate_screenshot(self):
        # 截图，并将图片保存为 /sdcard/screenshot.png
        os.system('adb shell screencap -p /sdcard/screenshot.png')
        # pull 命令是将图片从手机发送到电脑本地
        os.system('adb pull /sdcard/screenshot.png D:\\')

    # event 是点击事件

    def on_click(self, event):
        # event.xdata, event.ydata 分别是点击的横纵坐标，将坐标依次保存到 _coords 数组中
        self._coords.append((event.xdata, event.ydata))
        # 这里是每两次点击（起始点和目标点）就会执行按压按压屏幕操作，所以当
        # self._click_count == 2 时才执行
        self._click_count += 1
        if self._click_count == 2:
            self._click_count = 0
            # 弹出第二次点击时的坐标
            _next = self._coords.pop()
            # 弹出第一次点击时的坐标
            _prev = self._coords.pop()
            # 根据勾股定理计算出两点之间的距离
            self.jump_to_next(math.sqrt((_next[0] - _prev[0]) ** 2 + (_next[1] - _prev[1]) ** 2))

    def jump_to_next(self, distance):
        press_time = int(distance * self._coefficient)
        # cmd 最后一个参数 press_time 为按压时间，按压时间为 距离x按压系数，至于按压系数是
        # 多少则要根据每个人的手机分辨率而定，可自行测试调整
        # 100 100 200 200 这四个数字其实无所谓，只是模拟 swipe 操作时的坐标点而已
        cmd = 'adb shell input swipe 100 100 200 200 {}'.format(press_time)
        print(cmd)
        # 执行命令
        os.system(cmd)

    def run(self):
        # 循环执行操作
        while True:
            # 这里执行两次截图操作，不然会提示远程图片未找到的问题（可以注释其中一行试试看）
            self.generate_screenshot()
            self.generate_screenshot()
            figure = plt.figure()
            # 绑定 on_click 操作
            figure.canvas.mpl_connect('button_press_event', self.on_click)
            # 打开并显示图片
            img = Image.open('D:\\screenshot.png')
            plt.imshow(img)
            plt.show()

