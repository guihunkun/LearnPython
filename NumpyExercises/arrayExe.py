import numpy as np

'''
int8	字节（-128 to 127）
int16	整数（-32768 to 32767）
int32	整数（-2147483648 to 2147483647）
int64	整数（-9223372036854775808 to 9223372036854775807）
float32	单精度浮点数，包括：1 个符号位，8 个指数位，23 个尾数位
float64	双精度浮点数，包括：1 个符号位，11 个指数位，52 个尾数位
'''

x = np.array([[1,2,3], [4,5,6]], np.int32)
x = np.arange(24)
x = x.reshape(6,4)
print("x.ndim = ", x.ndim)

x = np.zeros(9)
x = x.reshape(3, 3)
print(x)

x = np.ones(16)
x = x.reshape(4,4)
print(x)




