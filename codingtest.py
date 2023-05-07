import random
from random import randrange
from collections import Counter
#
# def dp(n):
#     if n==1:
#         return 1
#     if n==2:
#         return 2
#     if mem[n] == 0:
#         mem[n].append(dp(n))
#     if mem[n] != 0 :
#         return mem[n]
#     return (dp(x-1)+dp(x-2))%10007
#
# n=input()
# dp(n)

# n=17
# k=4
# last_num=0
# def divid():
#     global n
#     global k
#     global last_num
#     cnt=0
#     if divmod(n,k):
#         last_num=divmod(n, k)
#
#     else



# import time
#
# x = int(input())
# start=time.time()
# cnt = 0
# while True:
#     if x==1:
#         break
#     elif x%3 ==0:
#         x/=3
#         cnt+=1
#         continue
#     elif x % 2 == 0:
#         x /= 2
#         cnt += 1
#         continue
#     else:
#         x+=-1
#         cnt+=1
#
# print(cnt)
# end=time.time()
# print(f"{end - start: .5f} sec")




#곱하기 또는 더하기

#
# x = [random.randint(0, 9) for p in range(0, 20)]
# print("lenOfX:",len(x))
# print("first",x)
# a=0
#
# x = [i for i in x if i not in {0}]
# ones= [i for i, value in enumerate(x) if value == 1]
# print("contOneList:",ones)
#
# for i in range(len(x)):
#     if i ==0 :
#         a+= x[i]
#         print("-- start cal --",a)
#         if x[i] == 1 or a !=0 :
#             continue
#     if a==1 and i>0 :
#         a+=x[i]
#         continue
#     if i in ones:
#         a+=1
#         print("-- add one --", a)
#     else:
#         a*=x[i]
#         print("-- multiply x --", a, "   ///  ", x[i])
#
# print("lenOfX:",len(x))
# print("last",x)
# print("answer:",a)




#모험가의 수 x

# x = randrange(1,100000)
#
# # 각 모험가의 공포도 y
# y = [random.randint(1, x) for p in range(0, x)]
# y = sorted(y)
# z =  Counter(y)
#
# print(x)
# print(y)
# print(z)
# travel_group = 0
# group_mem = 0
#
#
# for i in range(len(y)):
#     group_mem += 1
#     if group_mem >= y[i]:
#         travel_group +=1
#         group_mem = 0
# print(travel_group)





# 상화좌우 문제

# plan_list = ["L","R","U","D"]
# n = random.randrange(1, 101)
# m = random.randrange(1, 101)
# plan = random.choices(plan_list,k=m)
#
# location = [1, 1]
# print(n)
# print("len of plan :",len(plan))
# print(location)
#
# for i in range(len(plan)) :
#     if plan[i] == "L" :
#         location[0] -=1
#         if location[0] < 1:
#             location[0] += 1
#
#     elif plan[i] == "U":
#         location[1] -=1
#         if location[1] < 1:
#             location[1] += 1
#
#     elif plan[i] == "R":
#         location[0] += 1
#
#     elif plan[i] == "D":
#         location[1] +=1
#
#
# print(location)

##상화좌우 풀이
# n= int(input())
# x , y =  1,1
# plans = input().split()
#
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# move = ['L','R','U','D']
# for plan in plans:
#     for i in range(len(move)):
#         if plan == move[i]:
#             nx = x +dx[i]
#             ny = y +dy[i]
#     if nx <1 or ny <1 or nx >n or ny >n :
#         continue
#     x,y = nx, ny
# print(x,y)




# 시간 문제

# N = random.randint(0, 23)
# condition1,condition2,condition3=False,False,False
# counter=0
#
# for i in range(-1,N):
#     if "3" in str(i) :
#         condition1 = True
#     else:
#         condition1 = False
#     for j in range(-1,59):
#         if "3" in str(j) :
#             condition2 = True
#         else:
#             condition2 = False
#
#         for k in range(-1, 59):
#             if "3" in str(k):
#                 condition3 = True
#             else:
#                 condition3 = False
#             if condition1 or condition2 or condition3 == True:
#                 counter +=1
# print(counter)

## 시간 문제 풀이
# h=int(input())
# count=0
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i)+str(j)+str(k):
#                 count +=1
# print(count)



## dfs code
# def dfs(graph, v, visited):
#     visited[v]=True
#     print(v, end='')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i , visited)
#
# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]
#
# visited = [False] * 9
# dfs(graph,7,visited)




# 왕실 나이트
# N = random.randint(0, 7)
# M = random.randint(0, 7)
# column = [ 'a','b','c','d','e','f','g','h']
# rows = [1,2,3,4,5,6,7,8]
#
# input=column[N]+str(rows[M])
# cnt=0
# col = input[0]
# num = input[1]
# col_loc = column.index(col)
#
# print("input_data:",input)
#
# if int(num) + 2 in rows :
#     if column[col_loc + 1]  in column and col_loc <= 7:
#         cnt += 1
#     if column[col_loc - 1]  in column and col_loc >= 1:
#         cnt += 1
# if int(num)-2 in rows :
#     if column[col_loc + 1]  in column and col_loc <= 7:
#         cnt += 1
#     if column[col_loc - 1]  in column and col_loc >= 1:
#         cnt += 1
# if column[col_loc + 2] in column and col_loc <= 6:
#     if int(num) + 1 in rows:
#         cnt += 1
#     if int(num) - 1 in rows:
#         cnt += 1
# if column[col_loc - 2] in column and col_loc >= 2:
#     if int(num) + 1 in rows:
#         cnt += 1
#     if int(num) - 1 in rows:
#         cnt += 1
#
# print("night_move:",cnt)


# 왕실 나이트 풀이
# N = random.randint(0, 7)
# M = random.randint(0, 7)
# columns = [ 'a','b','c','d','e','f','g','h']
# rowss = [1,2,3,4,5,6,7,8]
#
# input_data=columns[N]+str(rowss[M])
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) +1
# # 유니코드로 변환하여 알파벳의 위치를 확인
# steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
# result =0
# for step in steps:
#     next_row = row + step[0]
#     next_column = column + step[1]
#     if next_row >=1 and next_row <=8 and next_column>=1 and next_column <=8:
#         result+=1
# print(input_data)
# print(result)

# 문자열 재정렬

# 음류수 얼려먹기
import numpy as np
import random
from io import StringIO

n=20
m=20

# print(dir(StringIO))



for num in range(1,n):
    for base in range(1,m):
        k=random.randint(0,1)
        print('{:3d}'.format(k), end='')
    print()


lines=StringIO.readlines()

# node= map(int, input().split())



print("matrix")

print(lines)
# def search(node, start, visited):
#
