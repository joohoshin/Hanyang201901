# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 02:37:39 2018

@author: jooho
"""

# 출처: http://nbviewer.jupyter.org/github/justmarkham/DAT4/blob/master/notebooks/08_linear_regression.ipynb

# Linear Regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# TV, 라디오, 신문에 광고비 집행한 것과 매출에 대한 데이터
file = 'http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv'

data = pd.read_csv(file, index_col=0) #index_col=0은 처음 열을 row index로 지정하라는 뜻

# subplot은 여러개의 플롯을 한번에 그리는 것
fig, axs = plt.subplots(1, 3, sharey=True) #sharey = True는 y축을 공유한다는 뜻
data.plot.scatter(x='TV', y='sales', ax=axs[0], figsize=(15, 8))
data.plot.scatter(x='radio', y='sales', ax=axs[1])
data.plot.scatter(x='newspaper', y='sales', ax=axs[2])

# 통계분석툴을 가져온다. 
import statsmodels.formula.api as smf

# TV와 매출과의 관계를 분석해본다. 
lm = smf.ols(formula='sales ~ TV', data=data).fit()  #y=x1을 y~x1 식으로 적으면 됨
lm.summary() # 기본적인 통계치 출력

# 모델을 그려보자
# Statsmodel
x = pd.DataFrame(
        {'TV':np.arange(data.TV.min(), data.TV.max(), 0.01)}) #x값은 데이터의 최대,최소값
y = lm.predict(x)

# 그래프에 추가
plt.figure()
data.plot.scatter('TV', 'sales')
plt.plot(x, y, c='red')

# seaborn은 자체적으로 1차 regression 모델까지 그려준다. 
import seaborn as sns
plt.figure()
sns.lmplot(x='TV', y='sales', data=data, height=4, aspect=2) #aspect는 가로/세로 비율



