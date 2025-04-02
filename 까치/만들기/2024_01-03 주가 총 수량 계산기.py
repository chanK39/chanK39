import re

while True:

    총자산text = input('총 자산 = ')#변수 가져오기
    
    if 총자산text in '종료하기':#총자산에 종료를 칠 경우 프로그램 종료하기
        print('''





----------------프로그램이 종료됩니다----------------
''')
            
        break
    
    
    #지수계산법인 총 자산을 숫자만 남기기
    
    number_in_exponential = 총자산text
    number_without_commas = number_in_exponential.replace(',', '')  # 쉼표 제거
    총자산 = round(int(float(number_without_commas)))  # 소수점을 처리하기 위해 float로 변환 후 int로 변환
    print(총자산)
    
    #if not (총자산 >= '0' and 총자산 <= '9'):#가져온 변수가 문자 혹은 숫자인지 판단하기
    #    print('---자산 오류---')
    #    continue
    
    
    
    주식명 = input('주식명 = ')
    if (주식명 >= '0' and 주식명 <= '9'):
        print('---주식명 오류---')
        continue
        
        
    주가 = input(주식명+' 주가 = ')
    if not (주가 >= '0' and 주가 <= '9'):
        print('---주가 오류---')
        continue




    #총 구매 가능한 주식 수 계산
    풀매수 = round(int(총자산)/int(주가))#반올림해서 값을 저장하기
    print(주식명,'올인시 = ',풀매수)

    


    #구매율 구하기
    비율 = input(주식명+' 구매 % = ')
    곱수 = int(비율)/100 
    #print(비율)
    #print(곱수)


    #구매량 구하기
    구매량 = round(int(총자산)*(곱수))
    if 구매량<0:
        print('불가능')
    else:
        마구 = ('마구'+주식명+구매량)
        print('.')
        print('.')
        print('.')
        print(마구)
        