# python_study
## 이 레퍼지토리에서는 파이썬 기반의 코딩 테스트 관련 개념을 공부하고 직접 푼 코드를 작성하여 올립니다. 
## 1. 알고리즘
 ### 1-1.메모이제이션   
   #### - 개념 : 동일한 계산을 반복하여 계산하는 상황일때, 이전에 계산된 값을 메모리에 저장함으로 실행속도를 증가 시킴
   #### - 예시 : 피보나치 수 
  "'''"    
  
def fib_recursion(n):
  if n == 1 or n == 2 :
    return 1
  else :
    return fib_recursion(n-1) + fib_recursion(n-2)

memo = {1:1, 2:1} 
def fib_memoization(n,memo):
  if  n in dic :
    return memo[n]
  memo[n]=fib_memoization(n-1)+ fib_memoization(n-2)
  return memo[n]

  
  "'''"
     
## 2. 복합  

