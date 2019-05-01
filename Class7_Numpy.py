# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 10:18:02 2018

@author: jooho
"""

# numpy 패키지 불러오기
import numpy as np

# 리스트를 만든 후 numpy 배열로 전환
list1 = [1,2,3,4,5]
a1 = np.array(list1)

# 한번에 만들기
a2 = np.array([2,4,6,8,10])

# 2차원 배열 만들기
array_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

# 난수로 변수 만들기
rand1 = np.random.rand(2,3) # 2차원 배열 
rand2 = np.random.rand(3) # 1차원 배열

# 정수 난수 배열 만들기
randint1 = np.random.randint(1,11,size=(2,3)) # 2차원 배열
randint2 = np.random.randint(2,10, size = 3) #1차원 배열

# 배열의 연산
arr1 = np.random.randint(1,11,size = 5)
arr2 = np.random.randint(1,11,size = 5)

arr1 + arr2
arr1 - arr2
arr1 * arr2
arr1 / arr2

# 행렬 연산
matrix1 = np.random.randint(1,11,size = (2,4))
matrix2 = np.random.randint(1,11,size = (2,4))

matrix2_T = matrix2.transpose() # transpose matrix
np.dot(matrix1, matrix2_T) # matrix product

# 통계치 계산
stat1 = np.random.rand(5)

stat1.sum() # 합계
stat1.mean() # 평균
stat1.std() #표준편차
stat1.var() # 분산
stat1.max() # 최대값
stat1.min() # 최소값

# arange
x = np.arange(-2,1, 0.5)

# y=2*x**2 + 10 함수를 그려보자
x= np.arange(-10,10, 0.1)
y = 2*x**2 + 10

import matplotlib.pyplot as plt
plt.plot(x,y)

# y=sin(x) 그래프를 그려보자
x2 = np.arange(20,40, 0.2)
y2 = np.sin(x2)
plt.plot(x2,y2)


### 탄젠트 그리기
# import library
import matplotlib.pyplot as plt
import numpy as np

# x,y 값을 지정
x = np.arange(-10.0, 10.0, 0.001)
y = np.tan(x)

# tangent는 무한대 값이 있으므로 그리기 위해서
# 출력할 y값의 한도를 정한다. 
ylim = 10

# 출력할 y값보다 큰 값을 nan을 넣어준다. (데이터 삭제)
y[y > ylim] = np.nan
y[y < -ylim] = np.nan

# 출력을 한다. 
plt.plot(x, y)
