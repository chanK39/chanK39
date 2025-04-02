# 기본 설명
print('사칙연산에 Enter 혹은 종료를 누르거나 치면 검산기가 종료됩니다')
print('더하기, 빼기, 곱하기, 나누기와 숫자로만 답해주세요')
opList =  ['종료', '더하기', '덧셈', '+' ,'곱하기','곱셈','X','x','나누기','나눗셈','/','÷','빼기','뺄셈','마','-','−']
opList2 = ['E','A','A','A','M','M','M','M','D','D','D','D','R','R','R','R','R']

#반복문(계속 반복시킴) 검산기 시작
while True:
    사칙연산 = input('사칙연산= ' )
    if 사칙연산 in opList:#사칙연산에 이 말들만 들어가기
        if 사칙연산 in '종료':#사칙연산에 종료를 칠 경우 프로그램 종료하기
            print('프로그램이 종료됩니다')
            break
        #사칙연산 하나로 정의하기
        oper =  opList2[opList.index(사칙연산)]
            
      
        #계산 정보 물어보기
        #변수에 숫자만 입력하게 만들기
        수 = (input('수= ' ))
        if (수 >= '0' and 수 <= '9'):#수 라는 변수가 숫자인지 판단하기
            print('...')
        else:continue#숫자가 아니면 처음으로 돌아가기
        계산수 = (input(사칙연산+' 할 수= ' ))
        if  (계산수 >= '0' and 계산수 <= '9'):
            print('...')
        else:continue
        예상값 = (input('예상값= ' ))
        if (예상값 >= '0' and 예상값 <= '9'):
            print('...')
        else:continue
        #계산하고 결과 말하기, int()는 ()안에 있는게 숫자라고 알려준다
        if oper =='A':
            result = int(수) + int(계산수) 
        elif oper == 'M':
            result = int(수) * int(계산수)   
        elif oper == 'D':
            result = int(수) / int(계산수) 
        elif oper == 'R':
            result = int(수) - int(계산수)  
        else:
            print ('error')
            
        if result == int(예상값):
            print('맞습니다')
        else:
            print('아닙니다')
            print((수),(사칙연산),(계산수),'=',int(result))
                         
    else:#사칙연산에 이상한거 입력했을때
        print('사칙연산에는 더하기, 빼기, 나누기, 곱하기만 입력하세요')
        continue#처음으로 돌아가기
print('프로그램 종료')                 
