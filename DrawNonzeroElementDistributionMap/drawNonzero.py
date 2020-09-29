import numpy as np
import matplotlib.pyplot as plt


def read_file(file_name):
	f = open(file_name)
	lines = f.readlines()
	K = np.zeros((len(lines), len(lines)))
	i = 0
	for line in lines:
		line = line.strip().split('\t')
		#K[i, :] = np.array(list(map(int, line)))
                K[i] = list(map(int, line))
		i+=1
	return K


if __name__ == '__main__':
	file_name = "A.txt"
	K = read_file(file_name)
	plt.matshow(K)
	plt.show()
