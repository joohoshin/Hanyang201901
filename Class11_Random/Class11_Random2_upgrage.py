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

xmin = -1
xmax = 1
step = 0.01

x= np.arange(xmin,xmax,step)
func_y = lambda x: x**2 - 0.5
y= func_y(x)

# 적분은 y=0을 기준으로 계산하므로 max가 0보다 작은 경우 max=0, 
# min이 0보다 큰 경우 min=0으로 변경한다.  

ymax = y.max() if y.max()>0 else 0
ymin = y.min() if y.min()<0 else 0

# 그리는 범위의 사각형의 넓이는
rect_area = (xmax-xmin) * (ymax-ymin)

# random으로 데이터를 뿌려서 넓이를 구해보자
iteration = 1000

plt.plot(x,y)
plt.axhline(y=0, color='k', linestyle='-') # y=0 선을 그려줌
results = []  # 함수 넓이 계산 범위에 포함되는 지 저장 +1, 0, 1로 저장
rnd_xs = []   # random x 위치 저장
rnd_ys = []   # random y 위치 저장

# 위치에 따른 결과값 판별 함수
def point_area(rnd_y, true_y):
    if rnd_y >=0:
        if true_y >= rnd_y:
            return 1
        else: return 0
    else:
        if true_y <= rnd_y:
            return -1
        else: return 0
    
for i in range(iteration):
    # random으로 점을 생성
    rnd = random.random()
    rnd_x = (xmax-xmin)*rnd + xmin
    rnd = random.random()
    rnd_y = (ymax-ymin)*rnd + ymin
    true_y = func_y(rnd_x)
    result = point_area(rnd_y, true_y)
    results.append(result)
    rnd_xs.append(rnd_x)
    rnd_ys.append(rnd_y)

results_df = pd.DataFrame({'x':rnd_xs, 'y':rnd_ys, 'final':results})
sns.scatterplot(x='x', y='y', hue='final', data=results_df )

# 최종 넓이 계산 (근사치)
count_yes = results_df.final.sum()
count_all = results_df.final.count()
estimate = count_yes/count_all * rect_area
print(estimate)
