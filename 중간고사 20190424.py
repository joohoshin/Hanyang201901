# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:40:12 2019

@author: jooho
"""

# 중간고사

# 1. List

colors = ['black', 'red', 'white', 'blue', 'pink'] # 리스트 생성
colors[3] # 'blue' 불러오기
colors.append('orange') #orange 추가
del colors[0] #'black' 삭제
colors[3] = 'grey' #'pink'를 'grey'로 변경
print(colors) #결과값 출력, 그냥 colors 만 써도 맞음

#2. 원의 넓이 함수 
import math
def 원의넓이(반지름):
    return math.pi * 반지름 **2

#3. 원의 넓이 구해보기

반지름 = [3,5,7,13] 
for i in 반지름:
    print(원의넓이(i))
    
#4. 맞는 것 고르기 정답 1번

def 합계(start, end):
    total = 0
    for i in range(start, end+1):
        total += i
    return total        
합계(1,100)

#5. 전역변수와 지역변수, 결과값 출력, 정답 125
number = 10
def function_A():
    number = 5
    result = number*5**2
    print(result)
function_A()

#6. 오류 발생 찾기, 정답 2번
#1)
num1= input('첫번째 숫자를 입력하세요. ')
num2= input('두번째 숫자를 입력하세요. ')
print(num1 + num2)

#2)
num1= input('몸무게(kg) ')
num2= input('키(m) ')
BMI = num1/num2**2
print(BMI)

#3)
name = input('이름이 뭐에요? ')
major = input('전공이 뭐에요? ')
print(name, major)


#7. 메모장 작성
memo = [] #빈 메모장을 만듭니다. 빈 리스트로 만듭니다. 

#반복 실행을 위한 while
while True:
    
    # 메뉴를 띄운다. 
    menu = input('무엇을 할까요? (1: 메모작성, 2: 메모보기, 3: 메모삭제, 4:종료)')

    if menu=='1':
        new_memo = input('메모를 입력하세요: ')
        memo.append(new_memo)        
    elif menu=='2':
        # 여러개의 메모를 차례대로 출력
        for i in memo: print(i)
    elif menu=='3':
        del_memo = int(input('몇번째 메모를 지울까요?'))
        del memo[del_memo-1] #리스트의 인덱스는 0부터 시작하므로 입력값에서 1을 빼기
        print(del_memo, '번째 메모가 삭제되었습니다. ')
    elif menu=='4':
        break # 루프를 벗어나서 다음 문장 실행
    else:
        print('메뉴 선택을 잘못했습니다. 다시 선택해주세요')        
print('메모장이 종료되었습니다.')


