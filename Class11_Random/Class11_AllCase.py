# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 07:53:40 2018

@author: jooho
"""

### 동전 4개를 던졌을 때 모두 앞면이 나올 확률은?

# 동전의 앞면은 1 뒷면은 0으로 정의

# Analytic Solution (binomial Tree 유사 방법)
# 반복문을 사용하여 모든 케이스를 그려보자

import pandas as pd

cnt=0
results = []
for _1st in range(2):
    for _2nd in range(2):
        for _3rd in range(2):
            for _4th in range(2):
                result = [_1st, _2nd, _3rd, _4th]                
                results.append(result)               
                cnt = cnt + 1
print(results)

results_df = pd.DataFrame(results, columns = ['1','2','3','4'])

# 횟수 출력
results_df['total'] = results_df.sum(axis=1) #axis = 0은 컬럼 합계
results_df['total'].plot.hist(bins = 5) #bin=5는 5개로 구분하라는 뜻

# 퍼센트로 구해보자
freq = results_df.groupby('total').total.count() #이건 결과값이 Series임
freq_df = pd.DataFrame(freq) 
freq_df['percent'] = freq_df['total']/cnt
freq_df.plot.bar(y='percent')

