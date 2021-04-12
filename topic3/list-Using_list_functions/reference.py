# 과제 해설close solution tab
# 리스트에 값들 추가
# append를 이용해서 원하는 값들을 순서대로 '추가'하면 됩니다.

# numbers.append(1)
# numbers.append(7)
# numbers.append(3)
# numbers.append(6)
# numbers.append(5)
# numbers.append(2)
# numbers.append(13)
# numbers.append(14)
# print(numbers)


# 홀수 모두 제거
# while 반복문을 이용해서 numbers 리스트의 원소를 순서대로 확인할 수 있습니다. 하나씩 보다가 홀수인 원소가 있으면 제거하면 되겠죠? 이 논리를 코드로 표현하면 아래와 같습니다.

# i = 0
# while i < len(numbers):
#     # 홀수면 제거
#     if numbers[i] % 2 == 1:
#         del numbers[i]
#     i += 1
# print(numbers)


# 그런데 사실 위 코드에는 문제가 있습니다.

# 어떤 요소가 홀수여서 제거될 경우, 그 뒤에 있는 요소들이 모두 하나씩 앞당겨집니다. 예를 들어서 numbers[3]이 홀수여서 제거되면, 4번 인덱스에 있던 요소는 3번 인덱스로 가고 5번 인덱스에 있던 요소는 4번 인덱스로 간다는 거죠.

# 우리는 현재 i를 1씩 늘려 주며 while 반복문을 돌고 있는데요. 홀수인 요소를 제거하고 나서는 i를 늘리면 안 됩니다. i를 늘리면 요소 하나를 검토하지 않고 건너뛰게 되는 겁니다.

# 수행 부분에서 경우를 나눠서 동작을 다르게 하면 됩니다. 홀수 요소를 찾으면 그 요소를 제거하고, 짝수 요소를 찾으면 i를 늘리는 거죠. 아래 코드처럼요!

# i = 0
# while i < len(numbers):
#     if numbers[i] % 2 == 1:
#         del numbers[i]
#     else:
#         i += 1
# print(numbers)


# 인덱스 0 자리에 20을 삽입
# insert를 이용해서 값을 원하는 위치에 '삽입'할 수 있습니다.

# numbers.insert(0, 20)
# print(numbers)


# 정렬
# sort를 이용해서 리스트를 정렬할 수 있습니다. 작은 순서대로 정렬하기 위해서 파라미터를 안 넘겨 줬습니다.

# numbers.sort()
# print(numbers)


# 모범 답안
# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 값들 추가
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)

# numbers에서 홀수 제거
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 1:
        del numbers[i]
    else:
        i += 1
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
numbers.sort()
print(numbers)


# []
# [1, 7, 3, 6, 5, 2, 13, 14]
# [6, 2, 14]
# [20, 6, 2, 14]
# [2, 6, 14, 20]