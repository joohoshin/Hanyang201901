# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 03:18:03 2018

@author: jooho
"""

# Multivariate Linear Regression

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import seaborn as sns

# TV, 라디오, 신문에 광고비 집행한 것과 매출에 대한 데이터
file = 'http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv'
data = pd.read_csv(file, index_col=0) 

# TV, 라디오 신문과 매출과의 관계를 분석해본다. 
# ordinary least square method 사용
#y=x1을 y~x1+x2+.. 식으로 적으면 됨
lm = smf.ols(formula='sales ~ TV + radio + newspaper', data=data).fit()  
lm.summary() # 기본적인 통계치 출력

# 특정 수치값을 넣어서 예측해볼수 있다. 
new_data = pd.DataFrame({'TV':[200,150], 'radio':[40,30], 'newspaper':[50,60]})
new_y = lm.predict(new_data)
print(new_y)

# seaborn으로 여러 변수들의 관계를 한번에 볼 수 있다. 
g = sns.PairGrid(data)
g.map(plt.scatter)