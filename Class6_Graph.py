# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 16:44:13 2018

@author: jooho
"""

# 그래프 라이브러리 matplotlib 불러오기
import matplotlib 

# 그래프 그리기 위한 리스트를 만들기
y = [1,3,4,7,8,2,4]
matplotlib.pyplot.plot(y)

# 두번째 데이터를 추가
x= [2,3,4,7,9,13,14]
matplotlib.pyplot.plot(x,y)

# 라이브러리 명령을 간단히 붙이기
import matplotlib.pyplot as plt
plt.plot(x,y)

# Scatter Plot 그리기
plt.scatter(x,y)

# 새로운 창에서 다시 출력
plt.figure()
plt.scatter(x,y)

# 제목 붙이기
plt.title('Sample Data')
plt.xlabel('sample xdata')
plt.ylabel('sample ydata')
plt.grid()

# 저장하기
plt.savefig('sample graph.png')

# 막대그래프
학생 = ['Kim', 'Park', 'Shin', 'Lee']
성적 = [80, 90, 100, 95]
plt.figure()
plt.bar(학생, 성적)

# 색상변경하기
색상 = ['r','g','b','m']
plt.bar(학생, 성적, color = 색상 )

# Histogram
퀴즈점수 = [20,30,40,35,44,50,60,60,60,40,50,55,15,58]
plt.figure()
plt.hist(퀴즈점수)


