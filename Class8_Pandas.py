# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 09:44:00 2018

@author: jooho
"""

# pandas library
import pandas as pd

# from list
s1 = pd.Series([1,2,3,4,5])

# from dict
s2 = pd.Series({'국어':100,'영어':80,'수학':90})

# DataFrame
s3 = pd.DataFrame([[1,2,3], 
                   [4,5,6],
                   [7,8,9]])

s4 = pd.DataFrame([[1,2,3],
                   [4,5,6],
                   [7,8,9]], columns = ['A','B','C'], index = ['가','나','다'])

# 비교를 위한 numpy
import numpy as np
n1 = np.array([[1,2,3],
               [3,4,5],
               [5,6,7]])

# 항목명 바꾸기
s3.columns = ['A','B','C']
s3.index = ['가','나','다']

# dict 형식으로 만들어 보기
s5 = pd.DataFrame({'연도':[2018,2018,2019,2019],
                   '상품':['Premium', 'Basic','Premium', 'Basic'],
                   '매출':[100,200,150,300]})

# iris Data Load
import seaborn as sns
iris = sns.load_dataset('iris')
iris.dtypes
iris

# 일부 줄만 보기
iris.head()
iris.tail()
iris.head(10)
iris.tail(15)

# plot
iris.plot() 
iris.plot.scatter(x='sepal_length', y='sepal_width')

# 종류별로 색상을 다르게
sns.scatterplot(x='sepal_length', y='sepal_width', 
            hue= 'species', data=iris )

iris[10:20]
iris.describe()

# CSV 에서 읽기
iris_csv = pd.read_csv('iris.csv', index_col=0)
sns.scatterplot(x='SepalLengthCm', y='SepalWidthCm', hue='Species', data=iris_csv)

