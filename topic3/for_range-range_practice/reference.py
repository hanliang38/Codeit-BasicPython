# 과제 해설close solution tab
# 리스트의 길이가 20이라고 가정하면, 해당 리스트의 인덱스 목록은 range(20)으로 받아올 수 있습니다. 리스트 numbers의 인덱스 목록을 받아오려면 range(len(numbers))를 하면 되겠죠?

# 우선 인덱스만 순서대로 출력해 봅시다.

# for i in range(len(numbers)):
#     print(i)
# 인덱스 i에 있는 원소를 받아오려면 numbers[i]를 하면 되는데요. 그러면 i와 numbers[i]를 함께 출력하면 되겠죠?

# 모범 답안

numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# 인덱스와 원소 출력
for i in range(len(numbers)):
    print(i, numbers[i])