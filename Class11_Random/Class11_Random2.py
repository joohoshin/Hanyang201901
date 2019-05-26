# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 10:10:51 2018

@author: jooho
"""
# 함수의 넓이를 수치적으로 구해보자

import numpy as np
import matplotlib.pyplot as plt
import random 
import seaborn as sns
import pandas as pd

# x의 범위를 설정
xmin = -1
xmax = 1
step = 0.01

# x값으로부터 y값을 구한다. 
x= np.arange(xmin,xmax,step)
func_y = lambda x: x**2
y= func_y(x)

# y의 최대최소값을 구한다. 
ymax = y.max()
ymin = y.min()

# 그리는 범위의 사각형의 넓이는
rect_area = (xmax-xmin) * (ymax-ymin)

# random으로 데이터를 뿌려서 넓이를 구해보자
iteration = 1000

plt.plot(x,y)
results = [] # 범위 안에 속하는지 저장, 1이면 함수값보다 작다. 0은 함수값보다 크다
rnd_xs = []  # 랜덤을 통해 나온 x값을 저장
rnd_ys = []  # 랜덤을 통해 나온 y값을 저장
for i in range(iteration):
    rnd = random.random()
    rnd_x = (xmax-xmin)*rnd + xmin  # rnd는 0~1 사이값이어서 범위를 조정
    rnd = random.random()
    rnd_y = (ymax-ymin)*rnd + ymin
    true_y = func_y(rnd_x)
    result = 1 if rnd_y<=true_y else 0  # 실제 함수값보다 작으면 1, 크면 0
    results.append(result)
    rnd_xs.append(rnd_x)
    rnd_ys.append(rnd_y)

results_df = pd.DataFrame({'x':rnd_xs, 'y':rnd_ys, 'final':results})
sns.scatterplot(x='x', y='y', hue='final', data=results_df )

# 최종 넓이 계산 (근사치)
count_yes = results_df.query("final==1").final.count()
count_all = results_df.final.count()
estimate = count_yes/count_all * rect_area
print(estimate)
