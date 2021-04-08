# 과제 해설
# 불린 자료형에서 배운 내용을 복습해 봅시다. 7 % 2 == 0은 False이고, 8 % 2 == 0은 True이죠? 이 원리를 파라미터 number에 적용하면?

# number가 짝수인 경우에 number % 2 == 0는 True가 나오고, number가 홀수인 경우에 number % 2 == 0은 False가 나오는 거죠.

# 그러면 함수 is_evenly_divisible은 그냥 number % 2 == 0을 리턴하면 되는 것입니다.

# 모범 답안
def is_evenly_divisible(number):
    return number % 2 == 0


# 테스트 코드    
print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))
print(is_evenly_divisible(317))