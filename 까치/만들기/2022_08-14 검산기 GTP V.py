# 유효한 사칙연산을 담은 세트
OPERATORS = {'+', '-', '*', '/'}

# 계산을 수행하는 함수
def calculate(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2

# 검산기 시작
while True:
    # 입력 받기
    operator = input('사칙연산= ')
    
    # 종료 조건
    if operator == '종료':
        print('프로그램이 종료됩니다')
        break
    
    # 유효한 사칙연산이 아닌 경우
    if operator not in OPERATORS:
        print('사칙연산에는 +, -, *, /만 입력하세요')
        continue
    
    # 수 입력 받기
    num1 = input('수= ')
    if not num1.isdigit():
        print('숫자를 입력하세요')
        continue
    
    num2 = input(operator + '할 수= ')
    if not num2.isdigit():
        print('숫자를 입력하세요')
        continue
    
    expected = input('예상값= ')
    if not expected.isdigit():
        print('숫자를 입력하세요')
        continue
    
    # 계산하고 결과 출력
    result = calculate(operator, int(num1), int(num2))
    if result == int(expected):
        print('맞습니다')
    else:
        print('아닙니다')
        print(f'{num1} {operator} {num2} = {result}')
        
print('프로그램 종료')
