import numpy as np


def interval_statistics(data, intervals):
    if len(data) == 0:
        return
    for num in data:
        for interval in intervals:
            lr = tuple(interval.split('~'))
            left, right = float(lr[0]), float(lr[1])
            if left <= num <= right:
                intervals[interval] += 1
    for key, value in intervals.items():
        print("%10s" % key, end='')  # 借助 end=''可以不换行
        print("%10s" % value, end='')  # "%10s" 右对齐
        print('%16s' % '{:.3%}'.format(value * 1.0 / len(data)))


if __name__ == '__main__' :
    start = -10  # 区间左端点
    number_of_interval = 10  # 区间个数
    length = 2  # 区间长度
    intervals = {'{}~{}'.format(length*x+start, 2*(x+1)+start): 0 for x in range(number_of_interval)}  # 生成区间
    # print(intervals)
    data = np.random.randint(start, start+length*number_of_interval+1, size=1000)  # 待统计数据(1000随机数)
    # print(data)
    interval_statistics(data, intervals)