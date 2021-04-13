# 과제 해설
# sum_digit 함수 정의
# sum_digit 함수를 정의하기 위한 단계들을 먼저 봅시다.

# 자릿수 합을 보관하는 변수 total을 0으로 정의한다.
# 정수형 num을 문자열로 바꾼다.
# 문자열은 리스트와 유사하다는 점을 이용하여, 반복적으로 각 자릿수를 받는다.
# 각 자릿수를 정수형으로 변환한다.
# 각 자릿수를 total에 더한다.
# 반복문을 이용해서 total을 모두 계산한 후, total을 리턴한다.
# 이 단계들을 코드로 표현하면 이렇습니다.

# def sum_digit(num):
#     total = 0
#     str_num = str(num)
    
#     for i in range(len(str_num)):
#         digit = str_num[i]
#         total += int(digit)
    
#     return total
# 그런데 우리는 인덱스 i는 굳이 필요 없습니다. 그래서 코드를 더 깔끔하게 쓰고 싶으면 이렇게 바꿀 수 있습니다.

# # 자리수 합 리턴
# def sum_digit(num):
#     total = 0
#     str_num = str(num)
    
#     for digit in str_num:
#         total += int(digit)

#     return total
# 훨씬 낫죠?

# 테스트
# 잘 작동하는지 테스트를 해 봅시다.

# print(sum_digit(12))
# print(sum_digit(486)
# 3
# 18
# 잘 되는 것 같습니다!

# sum_digit(1)부터 sum_digit(1000)까지 더하기
# 이제 sum_digit(1)부터 sum_digit(1000)까지 더하면 되는데요. 이건 for문을 이용해서 어렵지 않게 할 수 있습니다.

# digit_total = 0
# for i in range(1, 1001):
#     digit_total += sum_digit(i)



# 모범 답안

# 자리수 합 리턴
def sum_digit(num):
    total = 0
    str_num = str(num)
    
    for digit in str_num:
        total += int(digit)

    return total


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
digit_total = 0
for i in range(1, 1001):
    digit_total += sum_digit(i)

print(digit_total)