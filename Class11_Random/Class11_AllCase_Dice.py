# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 07:53:40 2018

@author: jooho
"""

### 주사위 3개를 던졌을 때 눈의 합계 분포 확인

# 주사위 눈은 1~6

# 반복문을 사용하여 모든 케이스를 그려보자

import pandas as pd

cnt=0
results = []
for _1st in range(1,7):
    for _2nd in range(1,7):
        for _3rd in range(1,7):            
                result = [_1st, _2nd, _3rd]                
                results.append(result)               
                cnt = cnt + 1

results_df = pd.DataFrame(results, columns = ['1st','2nd','3rd'])

# 횟수 출력
results_df['total'] = results_df.sum(axis=1) #axis = 0은 컬럼 합계
results_df['total'].plot.hist(bins = 16) 

# 퍼센트로 구해보자
freq = results_df.groupby('total').total.count() #이건 결과값이 Series임
freq_df = pd.DataFrame(freq) 
freq_df['percent'] = freq_df['total']/cnt
freq_df.plot.bar(y='percent')

