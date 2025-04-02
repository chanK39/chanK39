import re

while True:
    총자산text = input('총 자산 = ')

    if 총자산text.lower() == '종료하기':  # 대소문자 구분 없이 종료하기
        print('''





----------------프로그램이 종료됩니다----------------
''')
        break

    # 총 자산에서 숫자만 추출하기
    총자산 = int(''.join(re.findall(r'\d+', 총자산text)))

    if 총자산 <= 0:
        print('---자산 오류---')
        continue

    주식명 = input('주식명 = ')

    if any(map(str.isdigit, 주식명)):  # 숫자가 포함된 주식명 체크
        print('---주식명 오류---')
        continue

    주가 = input(주식명 + ' 주가 = ')

    if not 주가.isdigit() or int(주가) <= 0:  # 주가를 숫자로 받고 음수/0인 경우 체크
        print('---주가 오류---')
        continue

    # 총 구매 가능한 주식 수 계산
    풀매수 = 총자산 // int(주가)
    print(주식명, '올인시 = ', 풀매수)

    # 구매율 구하기
    비율 = input(주식명 + ' 구매 % = ')

    if not 비율.isdigit() or int(비율) < 0 or int(비율) > 100:  # 비율이 0보다 작거나 100보다 크면 오류
        print('---구매 % 오류---')
        continue

    # 구매량 구하기
    구매량 = 총자산 * int(비율) // 100
    if 구매량 < 0:
        print('불가능')
    else:
        마구 = f'마구 {주식명} {구매량}'
        print('.\n.\n.')
        print(마구)
