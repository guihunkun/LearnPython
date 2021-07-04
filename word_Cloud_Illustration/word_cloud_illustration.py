import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image  # 导入PIL模块中的Image对象
import jieba           # 导入中文分词组件
import wordcloud       # 导入词云模块
from wordcloud import ImageColorGenerator
from collections import Counter
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签


def read_file(file_name):
    if os.path.exists(file_name):  # 判断文件是否存在
        with open(file_name, "r", encoding='utf-8') as file:  # 读取文件
            content = file.read()
            if content:  # 判断文本内容是否为空
                return content
            else:
                print("文件无内容")
    else:
        print(file_name, "文件不存在")


def generate_word_cloud_illustration(content, figure_name, result_name):
        cut_text = jieba.cut(content)
        words = " ".join(cut_text)  # 拼接
        img = np.array(Image.open(figure_name))  # 读取图片
        img_colors = ImageColorGenerator(img)
        wd = wordcloud.WordCloud(mask=img, font_path="simhei.ttf", background_color="white")
        # wd.generate(words)
        wd.generate_from_text(words)
        plt.imshow(wd.recolor(color_func=img_colors), interpolation="bilinear")
        plt.axis("off")
        plt.savefig(result_name)
        plt.show()


def statistics_words(content, number, word_statis_name):
    not_statis = ['也', '我', '着', '那', '这', '了', '你', ':', '：', '?', '！', '...', '…', '他', '她', '？', '，', '、', '。', '的', '和', '\u3000', '“', '”', ' ', 'ri', '与', '是', '在', '中', '了', '\n']
    words = list(jieba.lcut(content))
    statistics = Counter(words).most_common(number)
    dic = {key: value for (key, value) in statistics}
    for i in list(dic.keys()):
        if i in not_statis:
            dic.pop(i)

    label = list(dic.keys())
    N = len(dic)
    theta = np.arange(0.0, 2*np.pi, 2*np.pi/N)
    radii = list(dic.values())
    width = np.pi/6
    ax = plt.subplot(111, projection='polar')
    bars = ax.bar(theta, radii, width=width, bottom=0.0)
    plt.xticks(theta+np.pi/12, label)
    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.viridis(r / 10.))
        bar.set_alpha(0.5)
    plt.savefig(word_statis_name)
    plt.show()


if __name__ == '__main__':
    #file_name = "story.txt"     # 预读取文本文件名
    file_name = 'zhuxian.txt'
    figure_name = "map.png"     # 词频图形状图片文件名
    result_name = 'result.png'  # 保存的词云图文件名
    word_statis_name = "word_statistics"  # 词频统计绘制的雷达图文件名
    content = read_file(file_name)        # 读取文件
    statistics_words(content, 35, word_statis_name)  # 词频统计并绘制雷达图
    generate_word_cloud_illustration(content, figure_name, result_name)  # 生成词云图

