속성창 = ['불','물','땅','바람','전기','얼음','금속','식물','빛','어둠']
print('캐릭터를 생성합니다')
이름 = input('이름= ')
성별 = input('성별= ')
직업 = input('직업= ')

print('속성을 선택하시겠습니까?')
속성선택 = input('예/아니오 = ')
if 속성선택 == ('예'):
    print(속성창)
    속성 = input('속성을 선택하세요= ')
    print('수식언을 선택하세세요')
    목록보기 = input('목록 보기(예/아니요)= ')
    if 목록보기 == '예':
        print('''
        은밀한 모략가
        절름발이 사기꾼
        로드릭을 싫어하는 자
        잡배의 군주
        디펜스 마스터
        강철의 주인
        넉살 좋은 잡담꾼
        늙은 시계추의 관리자
        저주받은 검투사
        장막 뒤의 그림자
        미염공 장목후
        달걀을 세우는 모험가
        북두성군
        육망성의 사냥꾼
        한발 늦은 시련의 극복자
        멸망한 세계의 그림자
        양산형 제작자
        검은 빛의 인도자
        복수와 묵시의 통치자
        역경루 히키코모리
        센다이의 독안룡
        4신물의 주인
        꼬마 탐정님
        플라톤
        아리스토텔레스
        작은 행성의 작은 성좌
        무의식의 발견자
        장판파의 호신
        만다라의 수호자
        드러누운 드래곤
        성급한 늪의 포식자
        고요한 섬의 미식가
        잊혀진 선망의 군주
        하얀 성의 주인
        세기말의 마술사
        13일의 주인공
        리바운드왕
        천개의 가면
        가장 오래된 꿈
        심장을 노리는 고리대금업자
        연기 나는 거울
        천둥과 전쟁의 주인
        무저갱의 지배자
        여덟 조각의 불꽃
        이데아의 철인
        자신의 무지를 아는 자
        지옥의 필경사
        지옥 기생자
        밀물과 썰물의 조정자
        깊은 밤의 늑대
        들개 사냥꾼
        멜베르크의 개장수
        신궁왕
        입은 셋 머리는 하나
        하루살이의 왕
        검은 황야의 암살자
        자작나무의 전갈
        초승달의 군주
        흑월의 사냥꾼
        해변의 전술가
        노력 전문가
        우중충한 밤바다의 까마귀
        원한의 사냥꾼
        재앙의 뒤틀린 머리''')
    수식언 = input('수식언을 선택하세요= ')
else:
    속성 = 'unknown'

print('----------\n' '이름= ' +이름,'\n''성별= ' +성별,'\n' '수식언= '+수식언,'\n''속성= ' +속성,'\n' '직업= ' +직업,'\n''----------')