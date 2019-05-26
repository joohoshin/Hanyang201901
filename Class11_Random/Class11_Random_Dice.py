# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 09:30:20 2018

@author: jooho
"""

# 이번에는 random을 활용해보자.(Monte Carlo)
# 주사위의 눈이 1~6이 아니라고 해보자 

import pandas as pd
import random 

# 주사위 눈이 아래와 같이 되어 있다고 하자
dices = [[1,2,3,4,4,6],  #1번째 주사위
         [2,3,3,5,6,6],  #2번째 주사위
         [1,2,3,5,5,5]]  #3번째 주사위

# 매번 주사위 던졌을 때 값을 얻어오자
def flip_dice(num_list):
    position = random.randint(0,5) #0~5까지 정수 생성 
    return num_list[position] # 주사위 눈에서 랜덤으로 선택된 위치의 값을 가져옴 

iteration = 10000  # 몇번 반복할 지 설정

results = []
for i in range(iteration):
    result = [flip_dice(dice) for dice in dices]
    results.append(result)

# pandas로 변환
results_df = pd.DataFrame(results, columns = ['1st','2nd','3rd'])

# 횟수 출력
results_df['total'] = results_df.sum(axis=1) #axis = 0은 컬럼 합계
results_df['total'].plot.hist(bins=14)

# 퍼센트로 구해보자
freq = results_df.groupby('total').total.count() #이건 결과값이 Series임
freq_df = pd.DataFrame(freq)
freq_df['percent'] = freq_df['total']/iteration
freq_df.plot.bar(y='percent')
        


    
