# -*- coding: utf-8 -*-

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

# pie chart
labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
sizes = [15, 30, 45, 10]
plt.pie(x=sizes, labels = labels, autopct='%1.1f%%')

# dictionary로 저장한 것 출력하기
grade = {'이름':['가','나','다','라','마'],
         '퀴즈':[10,30,20,25,30], 
         '중간고사': [20,40,30,20,38],
         '기말고사': [30,50,60,45,50]}

plt.scatter(x=grade['퀴즈'],y=grade['중간고사'] )
plt.bar(grade['이름'],grade['기말고사'])

# 한글 깨짐 방지: 클라우드에서는 안됨 , 그냥 복사해서 사용할 것
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False
f_path='c:/windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=f_path).get_name()
rc('font', family=font_name)

plt.bar(grade['이름'],grade['기말고사'])

# 파일에서 읽기
import pandas as pd
grade_df = pd.read_csv('grade.csv', encoding = 'cp949')
plt.scatter(x=grade_df['출석'], y=grade_df['과제'])

# 파일로 저장
grade_df.to_csv('grade2.csv')


