#17.6 표준 입력으로 금액(정수)이 입력됩니다. 1회당 요금은 1,350원이고, 교통카드를 사용했을 때마다의 잔액을 각 줄에 출력하는 프로그램을 만드세요
#(input에서 안내 문자열은 출력하지 않아야 합니다). 단, 최초 금액은 출력하지 않아야 합니다. 그리고 잔액은 음수가 될 수 없으며 잔액이 부족하면
# 출력을 끝냅니다.
# a=int(input())
# while a>1350:
#     a-=1350
#     print(a)

#18.표준 입력으로 정수 두 개가 입력됩니다(첫 번째 입력 값의 범위는 1~200, 두 번째 입력 값의 범위는 10~200이며 첫 번째 입력 값은 두 번째 입력 값보다
# 항상 작습니다). 다음 소스 코드를 완성하여 첫 번째 정수와 두 번째 정수 사이의 숫자 중 3으로 끝나지 않는 숫자가 출력되게 만드세요.
# 정답에 코드를 작성할 때는 while True:에 맞춰서 들여쓰기를 해주세요
# start, stop = map(int, input().split())
#
# i = start
#
# while True:
#     if i%10==3:  #3으로 끝나지 않는 숫자는 패스
#         i += 1
#         continue
#
#     if i >stop: #작은수가 큰수를 앞지르면 종료
#         break
#     print(i, end=' ')
#     i+= 1


#19.표준 입력으로 삼각형의 높이가 입력됩니다. 입력된 높이만큼 산 모양으로 별을 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다). 이때 출력 결과는 예제와 정확히 일치해야 합니다. 모양이 같더라도
# 공백이나 빈 줄이 더 들어가면 틀린 것으로 처리됩니다.
# height = int(input())
# for i in range(height): #앞쪽 삼각형 출력 (ex.0,1,2)
#     for j in reversed(range(height)): #공백을 찍기위해 rever 사용(ex.2,1,0)
#         if j > i:
#             print(' ', end='')
#         else:                       #공백이 아니면 별찍음
#             print('*', end='')
#     for j in range(height):
#         if j < i:
#             print('*', end='')
#     print()


#20.8 정수 두 개가 입력됩니다(첫 번째 입력 값의 범위는 1~1000, 두 번째 입력 값의 범위는 10~1000이며 첫 번째 입력 값은
# 두 번째 입력 값보다 항상 작습니다). 첫 번째 정수부터 두 번째 정수까지 숫자를 출력하면서 5의 배수일 때는 'Fizz', 7의
# 배수일 때는 'Buzz', 5와 7의 공배수일 때는 'FizzBuzz'를 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지
# 않아야 합니다).
#x,y=list(map(int,input().split(' ')))
# for i in range(x,y+1,1):
#     if i%35==0: #35조건을 먼저 확인
#         print("fizzbuzz")
#     elif i%7==0: #7의배수
#         print('buzz')
#     elif i%5==0:#5의배수
#         print('fizz')
#     else:
#         print(i)


#21.6 입력으로 꼭지점 개수(정수)와 선의 길이(정수)가 입력됩니다(꼭지점 개수의 입력 범위는 5~10, 선의 길이 입력 범위는
# 50~150입니다). 다음 소스 코드를 완성하여 꼭지점 개수와 선의 길이에 맞는 별이 그려지게 만드세요. 별을 그릴 때는
# 현재 위치부터 오른쪽으로 이동해서 시작해야 하며 시계 방향으로 그려야 합니다.

# import turtle as t
# n,line=map(int,input().split(" ")) #n=꼭지점의 갯수, line 각변의 길이
# t.shape('turtle')
# t.speed('slow')
# for i in range(n):
#     t.forward(line)
#     t.right((360/n)*2)
#     t.forward(line)
#     t.left(360/n) #다각형에서 외각의 합은 360

#22.10 정수 두 개가 입력됩니다(첫 번째 입력 값의 범위는 1~20, 두 번째 입력 값의 범위는 10~30이며 첫 번째 입력 값은
# 두 번째 입력 값보다 항상 작습니다). 첫 번째 정수부터 두 번째 정수까지를 지수로 하는 2의 거듭제곱 리스트를 출력하는
# 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 단, 리스트의 두 번째 요소와 뒤에서 두 번째 요소는
# 삭제한 뒤 출력하세요. 출력 결과는 리스트 형태라야 합니다.

# x,y = list(map(int,input().split(" ")))
# dot=[]
# for i in range(x,y+1,1):#전체 목록을 리스트로 저장
#     dot.append(2**i)
# del dot[1] #2번째항 제거
# del dot[-2]# 뒤에서 2번쨰항 제거
# print(dot)

#23.6 입력으로 2차원 리스트의 가로(col)와 세로(row)가 입력되고 그 다음 줄부터 리스트의 요소로 들어갈 문자가 입력됩니다.
# 이때 2차원 리스트 안에서 *는 지뢰이고 .은 지뢰가 아닙니다. 지뢰가 아닌 요소에는 인접한 지뢰의 개수를 출력하는
# 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).
# 여러 줄을 입력 받으려면 다음과 같이 for 반복문에서 input을 호출한 뒤 append로 각 줄을 추가하면 됩니다
# (list 안에 문자열을 넣으면 문자열이 문자 리스트로 변환됩니다).
# matrix = []
# for i in range(row):
#     matrix.append(list(input()))

# M,N = map(int, input().split())
# matrix = []
# print()
# for m in range(M):
#     matrix.append(list(input()))
#
# for m in range(M):
#     for n in range(N):
#         if matrix[m][n] == '*':
#             for a in range(-1,2):
#                 for b in range(-1,2):
#                     if (M > m+a >= 0) and (N > n+b >= 0) and matrix[m+a][n+b] != '*':
#                         if matrix[m+a][n+b] == '.':
#                             matrix[m+a][n+b] = 1
#                         else:
#                             matrix[m+a][n+b] += 1
#         elif matrix[m][n] == '.':
#             matrix[m][n] = 0
#
# for m in range(M):
#     for n in range(N):
#         print(''.join(str(matrix[m][n])),end='')
#     print(end='\n')

#24.5 문자열이 입력됩니다. 입력된 문자열에서 'the'의 개수를 출력하는 프로그램을 만드세요(input에서 안내 문자열은
# 출력하지 않아야 합니다). 단, 모든 문자가 소문자인 'the'만 찾으면 되며 'them', 'there', 'their' 등은 포함하지 않아야
# 합니다.
#예) the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether f
# rom the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why,
# at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the
# failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it
# is tiresome for children to be always and forever explaining things to the.

# x=input().split(' ')
# count=0
# for i in x:
#     if (i.strip(',.')=='the'):
#         count+=1
# print(count)

#24.6  물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다. 입력된 가격을 높은
# 가격순으로 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 이때 가격은 길이를 9로 만든
# 뒤 오른쪽으로 정렬하고 천단위로 ,(콤마)를 넣으세요.
#51900;83000;158000;367500;250000;59200;128500;1304000
# x=list(map(int,input().split(';')))
# x.sort(reverse=True) # 오름차순정령
# for i in x:
#     print('{0:>9}'.format(i,',')) #9개의자리를 만듬

#25.8  문자열 여러 개와 숫자 여러 개가 두 줄로 입력되고, 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성
# 합니다. 다음 코드를 완성하여 딕셔너리에서 키가 'delta'인 키-값 쌍과 값이 30인 키-값 쌍을 삭제하도록 만드세요.
#alpha bravo charlie delta
#10 20 30 40

# keys = input().split()
# values = map(int, input().split())
#
# x = dict(zip(keys, values))
# del x['delta']
# for keys,values in x.items():
#     if values == 30:
#         print(x)

#26.9  양의 정수 두 개가 입력됩니다. 다음 소스 코드를 완성하여 두 숫자의 공약수를 세트 형태로 구하도록 만드세요.
# 단, 최종 결과는 공약수의 합으로 판단합니다.

# x,y= map(int,input().split(' '))
# a = {i for i in range(1, x + 1) if x % i == 0}
# b = {i for i in range(1, y + 1) if y % i == 0}
#
# divisor = a & b
#
# result = 0
# if type(divisor) == set:
#     result = sum(divisor)
#
# print(result)

#27.6 문자열이 저장된 words.txt 파일이 주어집니다(문자열은 한 줄로 저장되어 있습니다). words.txt 파일에서 문자 c가
# 포함된 단어를 각 줄에 출력하는 프로그램을 만드세요. 단어를 출력할 때는 등장한 순서대로 출력해야 하며 ,(콤마)와
# .(점)은 출력하지 않아야 합니다


# import string
# import os
# words = list()
# with open('D:\junwoo\coding_dojang\codes\words.txt', 'r') as file:
#     for word in file:
#         words = word.split()
# for word in words:
#     temp = word.strip(string.punctuation).strip()
#     if 'c' in temp:
#         print(temp)


#28.4  단어가 줄 단위로 저장된 words.txt 파일이 주어집니다. words.txt 파일에서 회문인 단어를 각 줄에 출력하는 프로그램을
# 만드세요. 단어를 출력할 때는 등장한 순서대로 출력해야 합니다. 그리고 파일에서 읽은 단어는 \n이 붙어있으므로 \n을
# 제외한 뒤 회문인지 판단해야 하며 단어를 출력할 때도 \n이 출력되면 안 됩니다(단어 사이에 줄바꿈이 두 번 일어나면 안 됨
# import os
# words = list()
# with open('D:\junwoo\coding_dojang\codes\word2.txt', 'r') as file:
#     for word in file:
#         temp = word.strip('\\n')
#         words.append(temp)
# for word in words:
#     if word == word[::-1]:
#         print(word)

#29.8 숫자 두 개가 입력됩니다. 다음 소스 코드를 완성하여 두 숫자의 덧셈, 뺄셈, 곱셈, 나눗셈의 결과가 출력되게 만드세요.
# 이때 나눗셈의 결과는 실수라야 합니다.

# x, y = map(int, input().split())
#
# def calc(a, b):
#     return a + b, a - b, a * b, a / b
#
# a, s, m, d = calc(x, y)
# print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))

#30.0 국어, 영어, 수학, 과학 점수가 입력됩니다. 다음 소스 코드를 완성하여 가장 높은 점수, 가장 낮은 점수, 평균 점수가
# 출력되게 만드세요. 평균 점수는 실수로 출력되어야 합니다.
# 76 82 89 84
# korean, english, mathematics, science = map(int, input().split())
#
# def get_min_max_score(*args):  #최대 최소 인자값을 가져오는 함수작성
#     return min(args), max(args)
#
# def get_average(**kwargs):
#     return sum(kwargs.values()) / len(kwargs)
#
# min_score, max_score = get_min_max_score(korean, english, mathematics, science)
# average_score = get_average(korean=korean, english=english,
#                             mathematics=mathematics, science=science)
# print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
#       .format(min_score, max_score, average_score))
#
# min_score, max_score = get_min_max_score(english, science)
# average_score = get_average(english=english, science=science)
# print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
#       .format(min_score, max_score, average_score))

#31.5 피보나치수를 출력하시오

# def fib(n):
#     if (n==0 or n==1):
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
# a = int(input())
# print(fib(a))

#32   파일 이름 여러 개가 입력됩니다. 다음 소스 코드를 완성하여 파일 이름이 숫자 3개이면서 앞에 0이 들어가는 형식으로
# 출력되게 만드세요. 예를 들어 1.png는 001.png, 99.docx는 099.docx, 100.xlsx는 100.xlsx처럼 출력되어야 합니다.
# 그리고 람다 표현식을 사용해야 하며 출력 결과는 리스트 형태라야 합니다. 람다 표현식에서 파일명을 처리할 때는 문자열
# 포매팅과 문자열 메서드를 활용하세요.

# files = input().split()
# print(list(map(lambda x: '{0:03d}.{1}'.format(int(x.split('.')[0]), x.split('.')[1]), files)))

#33.6 정수가 입력됩니다. 다음 소스 코드를 완성하여 함수 c를 호출할 때마다 숫자가 1씩 줄어들게 만드세요.
# 여기서는 함수를 클로저로 만들어야 합니다. 정답에 코드를 작성할 때는 def countdown(n):에 맞춰서 들여쓰기를 해주세요

# def countdown(n):
#     i = n
#     def continueCount():
#         nonlocal i
#         r = i
#         i -= 1
#         return r
#     return continueCount
#
# n = int(input())
# c = countdown(n)
# for i in range(n):
#     print(c(), end=' ') #c에 저장된 함수가 클로저

#34. 게임 클래스 만들기
#캐릭터 능력치(체력, 마나, AP)가 입력됩니다. 다음 소스 코드에서 애니(Annie) 클래스를 작성하여 티버(tibbers) 스킬의
# 피해량이 출력되게 만드세요. 티버의 피해량은 AP * 0.65 + 400이며 AP(Ability Power, 주문력)는 마법 능력치를 뜻합니다.


# class Annie:
#     def __init__(self, health, mana, ability_power): #파이썬에서는 초기화시 무조선 자기자신 반환
#         self.health = health
#         self.mana = mana
#         self.ability_power = ability_power
#     def tibbers(self):
#         print('티버: 피해량', self.ability_power * 0.65 + 400)
#
# health, mana, ability_power = map(float, input().split())
#
# x = Annie(health = health, mana = mana, ability_power = ability_power)
# x.tibbers()

#35. 시간 클래스 만들기 시:분:초 형식의 시간이 입력됩니다. 다음 소스 코드에서 Time 클래스를 완성하여 시, 분, 초가
# 출력되게 만드세요. from_string은 문자열로 인스턴스를 만드는 메서드이며 is_time_valid는 문자열이 올바른 시간인지
# 검사하는 메서드입니다. 시간은 24시까지, 분은 59분까지, 초는 60초까지 있어야 합니다.
#예) 23:35:59

# class Time:
#     def __init__(self, hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#     @staticmethod  #static 함수로 변환
#     def is_time_valid(strValue : str):
#         strValueSplit = strValue.split(':')
#         return 0 <= int(strValueSplit[0]) <= 23 and 0 <= int(strValueSplit[1]) <= 59 and 0 <= int(strValueSplit[2]) <= 59
#     @classmethod #class 로변환
#     def from_string(cls, strValue : str):
#         strValueSplit = strValue.split(':')
#         return cls(int(strValueSplit[0]),int(strValueSplit[1]),int(strValueSplit[2]))
# time_string = input()
#
# if Time.is_time_valid(time_string):
#     t = Time.from_string(time_string)
#     print(t.hour, t.minute, t.second)
# else:
#     print('잘못된 시간 형식입니다.')

#36 상속 동물 클래스 Animal과 날개 클래스 Wing을 상속받아 새 클래스 Bird를 작성하여 '먹다', '파닥거리다', '날다',
# True, True가 각 줄에 출력되게 만드세요.

# class Animal:
#     def eat(self):
#         print('먹다')
#
# class Wing:
#     def flap(self):
#         print('파닥거리다')
#
# class Bird(Animal,Wing):
#     def fly(self):
#         print('날다')
#
# b = Bird()
# b.eat()
# b.flap()
# b.fly()
# print(issubclass(Bird, Animal))
# print(issubclass(Bird, Wing))

#37. 두점사이의 거리  좌표 4개가 입력되어 Point2D 클래스의 인스턴스 리스트에 저장됩니다. 여기서 점 4개는 첫 번째 점부터
# 마지막 점까지 순서대로 이어져 있습니다. 다음 소스 코드를 완성하여 첫 번째 점부터 마지막 점까지 연결된 선의 길이가
# 출력되게 만드세요.

# import math
# class Point2D:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
# length = 0.0
# p = [Point2D(), Point2D(), Point2D(), Point2D()]
# p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())
#
# for i in range(len(p) - 1):
#     x = p[i + 1].x - p[i].x
#     y = p[i + 1].y - p[i].y
#     length += math.sqrt(x ** 2 + y ** 2)
#
# print(length)

#38. 문자열이 입력됩니다. 다음 소스 코드를 완성하여 입력된 문자열이 회문이면 문자열을 그대로 출력하고,
# 회문이 아니면 '회문이 아닙니다.'를 출력하도록 만드세요. palindrome 함수와 NotPalindromeError 예외를 작성해야 합니다.

# class NotPalindromeError(Exception):
#     def __init__(self):
#         super().__init__('회문이 아닙니다.')
# def palindrome(word):
#     try:
#         if word == word[::-1]:
#             print(word)
#         else:
#             raise NotPalindromeError
#
#     except NotPalindromeError as e:
#         print(e)
# try:
#     word = input()
#     palindrome(word)
# except NotPalindromeError as e:
#     print(e)

#39 시간 이터레이터 만들기 정수 세 개가 입력됩니다(첫 번째 정수는 시작하는 초, 두 번째 정수는 반복을 끝낼 초,
# 세 번째 정수는 인덱스이며 입력되는 초의 범위는 0~100000, 입력되는 인덱스의 범위는 0~10입니다). 다음 소스 코드에서
# 시간 값을 생성하는 이터레이터를 만드세요.

# 시간 값은 문자열이고 시:분:초 형식입니다. 만약 숫자가 한 자리일 경우 앞에 0을 붙입니다(예: 12:01:08).
# 1초는 00:00:01입니다. 23:59:59를 넘길 경우 00:00:00부터 다시 시작해야 합니다.
# 시간은 반복을 끝낼 초 직전까지만 출력해야 합니다(반복을 끝낼 초는 포함되지 않음)

# class TimeIterator:
#     def __init__(self, start, stop, index=0):
#         self.start = start
#         self.stop = stop
#         self.index = index
#
#     def __getitem__(self, index):
#         if index < self.stop - self.start:
#             time = self.start + index
#             if time // 3600 > 23:
#                 time -= 86400
#
#             hour = time // 3600
#             minute = (time % 3600) // 60
#             second = time % 60
#             return '{0:02d}:{1:02d}:{2:02d}'.format(hour, minute, second)
#         else:
#             raise IndexError
#
# start, stop, index = map(int, input().split())
# for i in TimeIterator(start, stop):
#     print(i)
# print('\n', TimeIterator(start, stop)[index], sep='')

#40 제네레이터 만들기 표준 입력으로 정수 두 개가 입력됩니다(첫 번째 입력 값의 범위는 10~1000, 두 번째 입력 값의 범위는
# 100~1000이며 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다). 다음 소스 코드에서 첫 번째 정수부터 두 번째 정수
# 사이의 소수(prime number)를 생성하는 제너레이터를 만드세요. 소수는 1과 자기자신만으로 나누어 떨어지는 1보다 큰 양의
# 정수입니다.

# def prime_number_generator(start, stop):
#     for i in range(start, stop):
#         for j in range(2, i + 1):
#             if i == j:
#                 yield i #제네레이터는 yield를 통해서 함수값을 사용 바깥코드랑 왔다갔다함
#             if i % j == 0:
#                 break
#
# start, stop = map(int, input().split())
#
# g = prime_number_generator(start, stop)
# print(type(g))
# for i in g:
#     print(i, end=' ')

#41 사칙연산 코루틴 만들기
#표준 입력으로 사칙연산 계산식이 여러 개 입력됩니다. 다음 소스 코드에서 각 계산식의 결과를 구하는 코루틴을 만드세요.
# 계산식은 문자열 형태이며 값과 연산자는 공백으로 구분됩니다. 그리고 값은 정수로 변환하여 사용하고, 나눗셈은 / 연산자를
# 사용하세요.
#예) 1 + 2, 4 - 9
# def calc():
#     result = 0
#     while True:
#         expressions = (yield result)
#         a, expression, b = expressions.split()
#         if expression == '+':
#             result = int(a) + int(b)
#         elif expression == '-':
#             result = int(a) - int(b)
#         elif expression == '*':
#             result = int(a) * int(b)
#         else:
#             result = int(a) / int(b)
#
# expressions = input().split(', ')
# c = calc()
# next(c)
# for e in expressions:
#     print(c.send(e))
# c.close()

#42 데코레이터 만들기 HTML 태그 이름 두 개가 입력됩니다. 다음 소스 코드에서 함수의 반환값을 HTML 태그로 감싸는
# 데코레이터를 만드세요. HTML 태그는 웹 페이지에 사용하는 문법이며 <span>문자열</span>, <p>문자열</p>처럼 <태그이름>
# 으로 시작하며 </태그이름>으로 끝납니다.
#예 p spen

def html_tag(x):
    def real_decorator(func):
        def wrapper():
            return '<{0}>{1}</{0}>'.format(x, func())
        return wrapper
    return real_decorator

a, b = input().split()
@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'
print(hello())

#43 url 검사하기 URL 문자열이 입력 입력됩니다. 입력된 URL이 올바르면 True, 잘못되었으면 False를 출력하는 프로그램을
# 만드세요. 이 심사문제에서 판단해야 할 URL의 규칙은 다음과 같습니다

# import re
# url= input()
# print(re.match('http[s]*:\\/\\/[a-zA-Z0-9-]+\\.[a-zA-Z0-9-]+\\/*[a-zA-Z0-9-._,?=/]*',url)!=None)

#44 원의 반지름(실수)이 입력됩니다. 입력된 반지름을 이용하여 원의 넓이를 출력하는 프로그램을 만드세요
# import math
# # r = float(input())
# # print(r ** 2 * math.pi) #반지름제곱 곱하기 원주율

#45  패키지 사용하기 정수가 입력됩니다. 주어진 calcpkg 패키지를 활용하여 입력된 정수의 제곱근과 입력된 정수를 반지름으로
# 하는 원의 넓이가 출력되게 만드세요. 제곱근은 calcpkg 패키지에서 operation 모듈의 squareroot 함수를 사용하고, 원의
# 넓이는 calcpkg 패키지에서 geometry 모듈의 circle_area 함수를 사용하세요(calcpkg 패키지를 사용하지 않고 계산하면 결과가
# 맞더라도 틀린 것으로 처리됩니다. 반드시 calcpkg 패키지를 사용하세요).
# import math
# import calcpkg
# from calcpkg.operation import squareroot as root
# from calcpkg.geometry import circle_area as area
#
# num = int(input())
# print(root(num))
# print(area(num))

