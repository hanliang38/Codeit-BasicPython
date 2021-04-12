# 과제 해설
# 온도 변환 함수
# 화씨 온도를 섭씨 온도로 변환해 주는 fahrenheit_to_celsius 함수는 이렇게 작성할 수 있습니다.

# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5 / 9


# 한 번 이 함수를 활용해 봅시다. temperature_list에는 화씨 온도가 저장되어 있는데요. 만약 2번 인덱스의 원소를 섭씨 온도로 바꾸고 싶다면 뭘 해야 할까요?
# 이렇게 하면 됩니다.

# temperature_list[2] = fahrenheit_to_celsius(temperature_list[2])

# 그리고 만약 변환된 섭씨 온도를 소수점 첫째 자리까지 반올림하고 싶다면 이렇게 하면 되겠죠.

# temperature_list[2] = round(fahrenheit_to_celsius(temperature_list[2]), 1)


# 리스트의 모든 요소 변환
# 이제 temperature_list의 모든 원소를 섭씨로 변환하겠습니다. 반복문을 사용해야겠죠? 인덱스 0부터 인덱스 len(temperature_list) - 1까지 반복을 해야 하는데요.

# i = 0
# while i < len(temperature_list):
#     # 인덱스 i에 있는 요소 변환
#     i += 1

# 이렇게 하면 되겠네요.

# 이제 temperature_list의 인덱스 i에 있는 요소를 화씨에서 섭씨로 변환하면 코드가 완성됩니다.

# 모범 답안
# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드
i = 0
while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1)
    i += 1
print("섭씨 온도 리스트: {}".format(temperature_list))  # 섭씨 온도 출력