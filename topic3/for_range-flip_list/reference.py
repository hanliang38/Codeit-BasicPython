# 과제 해설



# 접근법 #1
# 리스트를 뒤집기 위해서는, 서로 대칭인 원소들의 위치를 바꿔야(swap) 합니다.

# 대칭 관계 이해하기
# 대칭인 원소들을 어떻게 찾을 수 있을까요? 서로 대칭이 되는 인덱스를 찾아야겠죠.

# 인덱스 0과 대칭되는 위치는 인덱스 len(numbers) - 1입니다.
# 인덱스 1과 대칭되는 위치는 인덱스 len(numbers) - 2입니다.
# 인덱스 2와 대칭되는 위치는 인덱스 len(numbers) - 3입니다.
# 대칭되는 두 인덱스를 left와 right라고 합시다.

# right = len(numbers) - left - 1로 관계를 표현할 수 있습니다.

# 반복문 돌기
# 반복문을 돌면서 left 요소와 right 요소의 위치를 바꿔 줘야 합니다.

# 그러기 위해서는 이렇게 할 수 있는데요.

# numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# # 리스트 뒤집기
# for left in range(len(numbers)):
#     # 인덱스 left와 대칭인 인덱스 right 계산
#     right = len(numbers) - left - 1

#     # 위치 바꾸기
#     temp = numbers[left]
#     numbers[left] = numbers[right]
#     numbers[right] = temp

# print("뒤집어진 리스트: " + str(numbers))


# 뒤집어진 리스트: [2, 3, 5, 7, 11, 13, 17, 19]
# 이렇게 하면 리스트가 뒤집히지 않은 상태로 출력됩니다. 왜 그런 걸까요?

# 우리는 for문을 left가 0일 때부터 left가 len(numbers) - 1일 때까지 반복하는데요. 사실 left가 그렇게 끝까지 돌 필요가 없습니다. 그냥 리스트 길이의 반만 돌아도 리스트를 뒤집을 수 있기 때문이죠!

# 오히려 리스트 길이의 반을 넘게 돌면, 잘 바꿔 놨던 위치를 다시 원상 복구하는 셈입니다.




# 접근법 #2
# 위치 바꾸기를 쉽게 할 수 있는 방법도 있습니다. 피보나치 수열 과제에서 언급한 방법 기억나시나요? 강의에서 배우지는 않지만, 튜플(tuple)이라는 자료형을 이용해서 할당하는 겁니다. 튜플은 아래와 같이 표현합니다.

# korean_names = ('효선', '유신')
# english_names = 'hyoseon', 'yusin'

# print(type(korean_names))
# print(type(english_names))
# <class 'tuple'>
# <class 'tuple'>
# 위처럼 괄호를 통해 표현할 수도 있지만 , 로만 각 요소를 구분해도 튜플로 인식이 됩니다.

# 그럼 어떻게 위치를 쉽게 바꿀 수 있는지 코드를 보겠습니다.

# numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# # 리스트 뒤집기
# for left in range(len(numbers) // 2):
#     # 인덱스 left와 대칭인 인덱스 right 계산    
#     right = len(numbers) - left - 1

#     # 위치 바꾸기
#     numbers[right], numbers[left] = numbers[left], numbers[right]

# print("뒤집어진 리스트: " + str(numbers))


# 위와 같이 쓰게 되면 지정 연산자(=) 의 오른쪽에 있는 튜플이 위치가 바뀌기 전의 numbers[left], numbers[right] 의 값을 보관하게 됩니다. 그리고 numbers[right], numbers[left] 에 해당하는 요소에 값을 각각 할당하게 되면서 이전 코드처럼 임시 변수를 만들지 않고도 값을 교환할 수 있는 것입니다.



# 모범 답안
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for left in range(len(numbers) // 2):
    # 인덱스 left와 대칭인 인덱스 right 계산
    right = len(numbers) - left - 1  
    
    # 위치 바꾸기
    numbers[right], numbers[left] = numbers[left], numbers[right]

print("뒤집어진 리스트: " + str(numbers))