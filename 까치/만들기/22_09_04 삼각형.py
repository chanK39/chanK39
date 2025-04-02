def Y(X):
    Y = (int(X)/2 + 90)

심 = input('삼각형의 (내심/외심)= ')


if 심 == '내심':
    A = input('윗각= ')
    X = int(A)/2 + 90
    print('각 BIC= ',X)

if 심 == '외심':
    A = input('윗각= ')
    X = int(A)*2
    print('각 BIC= ',X)