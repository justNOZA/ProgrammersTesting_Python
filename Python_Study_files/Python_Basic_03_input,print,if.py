#출력문
print(1)
#기본적으로 ;을 찍어줄 필요가 없다.
# 한줄에 한개의 명령이 가능한데 각 명령을 ;으로 구분하면 한 줄에 여러가지를 쓸 수 있다.
print('문자열')
print("abc, 문자타입이 따로 없다. 모든 것이 다 객체")
print()#줄 바꾸는 역할
a = 1 #명시적으로 자료형을 제시하지 않는다.
b = 1 #변수 설정은 이름만 안 겹치면되고 JAVA랑 비슷하다.
print(a+b)
print(a, b)
print('aaaa','bbbbb','ccccc') #늘어 놓으면 차례대로 출력을 한다.
print('aaa bbbb cccc')
print('aaa', 'bbb', 'ccc', sep='/', end=' => ') #사이사이에 값을 넣는 것 sep / 마지막 값에 값을 주는 것 end
print(a,b,sep='/')
print(a,b,sep='/' ,end='\n')
print(a,b,sep='/') #end는 기본 default값으로 \n이 되어 있다.
print('aaaaa\nbbbbbb')
a1 = '서울'; b1 = '부산'; c1 = '광주'
print(a1,b1,c1,sep=' 찍고 ')

#키보드로 입력받기
c = input('정수를 입력해 주세요 : ') #input은 무조건 문자열로 받는다. 무엇을 입력하든 문자열로.....계산식을 넣어도 계산 안됨
print('c = ', c+'1') #정수로 변환하기....?
c2 = int(c) #정수가 아닌것을 변환하려고 하면 오류가 발생한다.
print('c+5 =',c2+5) #아래에서 에러가 나도 위에서부터 진행되기 때문에 문제가 없지만 위에서 에러가 나면 아래는 진행되지 않는다.
print('ok')

#키보드로 입력받기
d = input('실수를 입력해 주세요 : ') #input은 무조건 문자열로 받는다. 무엇을 입력하든 문자열로.....계산식을 넣어도 계산 안됨
print('d = ', d) #실수로 변환하기....?
d2 = float(d) #실수가 아닌것을 변환하려고 하면 오류가 발생한다.
print('d+5 =',d2+5) #아래에서 에러가 나도 위에서부터 진행되기 때문에 문제가 없지만 위에서 에러가 나면 아래는 진행되지 않는다.
print('ok')


e = int(input('숫자를 입력해주세요'))
print(e+5)

print(type(a), type(b), type(c), type(d), type(e), sep= '|') #type확인

#-------------------------------------------------------------------------------------------------------------------------------------------------

if type(a) == float : #<class 'int'>의 값을 확인할 때는 int, float, str 등을 바로 물어보면 된다.
    print('float')
elif type(a) == int :
    print('int')
else :
    print('str')