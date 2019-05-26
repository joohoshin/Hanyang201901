# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 09:30:20 2018

@author: jooho
"""

# 이번에는 random을 활용해보자.(Monte Carlo)
# 동전의 앞뒤 나올 확률이 다르다고 해보자 

import pandas as pd
import random 

# 매번 동전을 던져서 결과를 모음
def flip_coin(face_prob):
    rnd = random.random()   #[0,1) 사이의 난수 발생
    result = 1 if rnd < face_prob else 0 
    return result

# 한번에 동전을 4개를 던지는데 앞면 확률이 다르다고 해보자

coins = [0.5, 0.2, 0.6, 0.55] # 앞면 나올 확률이 다음과 같다고 해보자
iteration = 10000  # 몇번 반복할 지 설정

# 동전을 10000번 던져서 결과를 저장
results = []
for i in range(iteration):
    result = [flip_coin(coin) for coin in coins] #List comprehension
    results.append(result)

# pandas로 변환
results_df = pd.DataFrame(results, columns = ['1','2','3','4'])

# 횟수 출력
results_df['total'] = results_df.sum(axis=1) #axis = 0은 컬럼 합계
results_df['total'].plot.hist(bins = 5)

# 퍼센트로 구해보자
freq = results_df.groupby('total').total.count() #이건 결과값이 Series임
freq_df = pd.DataFrame(freq)
freq_df['percent'] = freq_df['total']/iteration
freq_df.plot.bar(y='percent')
        


    
