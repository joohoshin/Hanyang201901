# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 20:07:33 2018

@author: jooho
"""

import pandas as pd

# matplotlib 한글 깨짐 방지 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


### 파일 데이터 읽기

# 파일 경로 지정
# 경로 지정시 폴더 구분 기호를 \를 한번 더 적어준다. 
path = 'C:\\Users\\jooho\\Downloads\\2015_ accident_statistics by age'
file = '2015 accident by age and sex.csv'

# 파일명과 합쳐준다. 
path_file = path + '\\' + file

# 한글 윈도우는 cp949 인코딩 사용
accident_data = pd.read_csv(path_file, encoding = 'cp949')

### 연령별 사고 발생건수를 알아보자

# 성별 중에서 기타불명을 제거해보자
accident_clean = accident_data.query("성별!='기타불명'")

# 연령이 불명인 데이터도 제거해보자
accident_clean = accident_clean.query("연령층!='불명'")

# 위의 두 조건을 & (and)를 활용하여 한번에 할 수도 있다. 
accident_clean = accident_data.query("성별!='기타불명' & 연령층!='불명'")

### 연령층과 발생건수만 선택하여 그려보자
연령별_발생건수 = accident_clean[['연령층', '발생건수']]
연령별_발생건수 = 연령별_발생건수.groupby(['연령층']).sum()
연령별_발생건수 = 연령별_발생건수.reset_index()

import seaborn as sns
# seanborn barplot은 기본값이 confidence interval 출력, 없애려면 ci= None 입력
sns.barplot(x='연령층', y='발생건수', data=연령별_발생건수, ci=None) 

### 발생건수 대비 사망자수 비율을 알아보자
# 필요없는 컬럼을 삭제해보자
accident2 = accident_clean.drop('부상신고', axis=1) #axis 0은 index, 1은 컬럼
delete_row = accident_clean.drop(3,axis = 0)

# 사망율 컬럼 추가
accident2['사망율_발생건수'] = accident2['사망자수']/accident2['발생건수']
plt.figure()
sns.barplot(x='연령층', y='사망율_발생건수', data=accident2, ci=None)

# 성별을 그룹화하여 그려보자
plt.figure()
sns.barplot(x='연령층', y='사망율_발생건수', hue='성별', data=accident2, ci=None)

# csv 출력, 한글 윈도우는 cp949 인코딩 사용
accident2.to_csv('accident2.csv', encoding = 'cp949')

# 엑셀 파일 읽기
xldata = pd.read_excel('C:\\Users\\jooho\\Downloads\\2015_ accident_statistics by age\\2015 accident by age and sex.xlsx')

### 엑셀 파일 쓰기
# 엑셀 파일 생성
xlfile = pd.ExcelWriter('accident2.xlsx', engine = 'xlsxwriter')

# 시트에 데이터 쓰기
accident2.to_excel(xlfile, sheet_name = 'accident2')

# 엑셀 파일 저장
xlfile.save()

# 워킹 디렉토리 확인
import os
os.getcwd()



