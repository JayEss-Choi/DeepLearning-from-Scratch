import numpy as np
import matplotlib.pyplot as plt

# 데이터 준비
x = np.arange(0, 2 * np.pi, 0.01)  # 0~2PI 범위에서 0.01 간격으로 생성
y1 = np.sin(x)
y2 = np.cos(x)

# 그래프 그리기
plt.plot(x, y1, label="sin")
plt.plot(x, y2, label="cos", linestyle="--")
plt.xlabel("x") # x축 이름
plt.ylabel("y") # y축 이름
plt.title("sin & cos") # 제목
plt.legend()
plt.show()