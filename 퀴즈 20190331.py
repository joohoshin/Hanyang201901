# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 14:39:58 2019

@author: jooho
"""

# 20190403 퀴즈

# 1. BMI

체중 = float(input('체중을 입력하세요(kg): '))
신장 = float(input('신장을 입력하세요(m): '))
BMI = 체중/신장**2
print('BMI: ', BMI) 
if 체중/신장**2>25:
    print('비만입니다. 운동으로 감량이 필요합니다.')
else:
    print('정상입니다. 꾸준한 운동으로 유지시켜주세요')


    
# 2. 1부터 100까지의 합계

sum = 0
for i in range(1,101):
    sum += i
print(sum)


# 3. 구구단 출력

for i in range(2,10):
    print()
    print(i, '단')
    for j in range(2,10):
        print(i,'*', j,'=', i*j)
        
# 4. 로또 생성

import random 

for i in range(1,7):
    num = random.randint(1,45)
    print(i,'번째 번호는',num, '입니다')
    
# 5.두 정수 입력 후 합계 출력

num1 = int(input('첫번째 정수를 입력하세요: '))
num2 = int(input('두번째 정수를 입력하세요: '))
print(num1,'과',num2,'의 합은', num1+num2,'입니다')