import statistics
과목 = ['국어', '과학', '영어', '수학' ,'역사']
점수 = [100,100,85,86,97]
만점 = ''
print('2022년 2학년 2학기 중간고사 성적표')
print('시험 과목',과목,'총',len(과목),'과목')

print('_____')
print(' ')
for j in range(0,5):
    print(과목[j],점수[j])
print('_____')
print(' ')
print('평균 점수=', statistics.mean(점수))

for i in range(0,5):
 if 점수[i]== 100:
    만점= 만점 + ' ' +과목[i]
 
print("만점인 과목= ", 만점)
최하 = 과목[점수.index(min(점수))]


print('최저점=', min(점수),최하)
print('최고점=', max(점수))
