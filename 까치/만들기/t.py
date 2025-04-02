number_with_commas = 1.2,052,369,400,842,501e+21
number_as_string = str(number_with_commas)  # 숫자를 문자열로 변환
number_without_commas = number_as_string.replace(',', '')  # 쉼표 제거
print(number_without_commas)

number_in_exponential = float(number_without_commas)  # 지수 표기법을 포함한 숫자로 변환
print(number_in_exponential)
