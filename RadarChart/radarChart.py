import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname='/Library/Fonts/Arial Unicode.ttf', size=10)


# Label
labels = np.array(['专业', '学习', '协作', '表达', '执行力', '创造力'])
# Value
data = np.array([8, 9, 9, 7, 9, 7])
angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
data = np.hstack((data, [data[0]]))
angles = np.hstack((angles, [angles[0]]))


fig = plt.figure(figsize=(2, 2))
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, data, 'ro-', linewidth=2)
ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties=font)
plt.ylim(1, 10)
plt.title("", fontsize=12, fontproperties='SimHei')
plt.savefig('capacity.png', bbox_inches='tight', pad_inches=0.1)
plt.show()
