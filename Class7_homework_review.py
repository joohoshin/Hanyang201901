

# 리스트와 함수 사용 시
data = []
while True:
    input_str = input('숫자를 입력하세요. 종료;입력끝 :')
    if input_str == '입력끝':
        if len(data)==0:
            print("데이터가 없습니다")
            break
        print(data)
        print('합', sum(data))   # 리스트의 합계 연산
        print('평균', sum(data)/len(data))
        print('최대', max(data))    
        print('최소', min(data))
        break
    else:
        num = float(input_str)
        data.append(num)

        
# 함수를 직접 만들어서
def sum_func(data): #data는 리스트 형태라 가정
    sum_ = 0
    for i in data:
        sum_ += i
    return sum_
    
def avg_func(data):
    cnt = 0
    for i in data:
        cnt +=1
    return sum_func(data)/cnt
    
def avg_func2(data):
    sum_= 0
    cnt = 0
    for i in data:
        cnt +=1
        sum_+=i
    return sum_/cnt
    
def min_func(data):
    min_ = float('inf')
    for i in data:
        if min_ >= i: min_=i
    return min_
    
def max_func(data):
    max_ = float('-inf')
    for i in data:
        if max_ <= i: max_=i
    return max_


data = []
while True:
    input_str = input('숫자를 입력하세요. 종료;입력끝 :')
    if input_str == '입력끝':
        if len(data)==0:
            print("데이터가 없습니다")
            break
        print(data)
        print('합', sum_func(data))   # 리스트의 합계 연산
        print('평균', avg_func2(data))
        print('최대', max_func(data))    
        print('최소', min_func(data))
        break
    else:
        num = float(input_str)
        data.append(num)    
    
    

