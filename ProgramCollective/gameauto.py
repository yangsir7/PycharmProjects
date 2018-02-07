import os
import math
# ������������ͼƬ�Ĳ���
import matplotlib.pyplot as plt
from PIL import Image


class WechatJump:
    def __init__(self):
        # ��ѹϵ������ͬ�ֱ��ʵ��ֻ���Ҫ������
        self._coefficient = 2.05
        # ��¼��ѹ����
        self._click_count = 0
        # ��¼��������������
        self._coords = []

    def generate_screenshot(self):
        # ��ͼ������ͼƬ����Ϊ /sdcard/screenshot.png
        os.system('adb shell screencap -p /sdcard/screenshot.png')
        # pull �����ǽ�ͼƬ���ֻ����͵����Ա���
        os.system('adb pull /sdcard/screenshot.png D:\\')

    # event �ǵ���¼�

    def on_click(self, event):
        # event.xdata, event.ydata �ֱ��ǵ���ĺ������꣬���������α��浽 _coords ������
        self._coords.append((event.xdata, event.ydata))
        # ������ÿ���ε������ʼ���Ŀ��㣩�ͻ�ִ�а�ѹ��ѹ��Ļ���������Ե�
        # self._click_count == 2 ʱ��ִ��
        self._click_count += 1
        if self._click_count == 2:
            self._click_count = 0
            # �����ڶ��ε��ʱ������
            _next = self._coords.pop()
            # ������һ�ε��ʱ������
            _prev = self._coords.pop()
            # ���ݹ��ɶ�����������֮��ľ���
            self.jump_to_next(math.sqrt((_next[0] - _prev[0]) ** 2 + (_next[1] - _prev[1]) ** 2))

    def jump_to_next(self, distance):
        press_time = int(distance * self._coefficient)
        # cmd ���һ������ press_time Ϊ��ѹʱ�䣬��ѹʱ��Ϊ ����x��ѹϵ�������ڰ�ѹϵ����
        # ������Ҫ����ÿ���˵��ֻ��ֱ��ʶ����������в��Ե���
        # 100 100 200 200 ���ĸ�������ʵ����ν��ֻ��ģ�� swipe ����ʱ����������
        cmd = 'adb shell input swipe 100 100 200 200 {}'.format(press_time)
        print(cmd)
        # ִ������
        os.system(cmd)

    def run(self):
        # ѭ��ִ�в���
        while True:
            # ����ִ�����ν�ͼ��������Ȼ����ʾԶ��ͼƬδ�ҵ������⣨����ע������һ�����Կ���
            self.generate_screenshot()
            self.generate_screenshot()
            figure = plt.figure()
            # �� on_click ����
            figure.canvas.mpl_connect('button_press_event', self.on_click)
            # �򿪲���ʾͼƬ
            img = Image.open('D:\\screenshot.png')
            plt.imshow(img)
            plt.show()

