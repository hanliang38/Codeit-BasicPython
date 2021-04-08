# 실습과제
# 어떤 수가 짝수인지 홀수인지 판단해 주는 함수 is_evenly_divisible를 쓰세요.

# is_evenly_divisible는 number(수)를 파라미터로 받습니다. 짝수인 경우, 즉 number가 2로 나누어 떨어질 경우에는 True를 리턴해 줍니다. 홀수인 경우, 즉 number가 2로 나누어 떨어지지 않을 경우에는 False를 리턴해 줍니다.

# 함수 안에는 print문이 아닌, return문을 사용해야 합니다. 그리고 참고로 불린 개념을 잘 사용하면, 함수 단 한 줄로 작성할 수 있습니다!
# 

# False
# False
# True
# True
# False



def is_evenly_divisible(number):
    # 코드를 작성하세요
    return(( number % 2 ) == 0)


# 테스트
print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))
print(is_evenly_divisible(317))