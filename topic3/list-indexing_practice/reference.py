# 과제 해설close solution tab
# 리스트의 인덱스는 1이 아니라, 0부터 시작한다는 걸 유의해 주세요.

# greetings 리스트의 원소를 모두 출력하려면 인덱스 0부터 인덱스 6까지의 요소들을 받아오면 되겠죠? 그러니가 greetings[0], greetings[1], greetings[2]... 이런 식으로 greetings[6]까지 출력하면 된다는 거죠.

# 이것을 반복문으로 하면 이렇습니다.

# i = 0
# while i < 7:
#     print(greetings[i])
#     i += 1
# 위 코드를 조금 더 일반화하고 싶으면, len 함수를 쓰면 됩니다.

# 모범 답안
i = 0
while i < len(greetings):
    print(greetings[i])
    i += 1
# 7이라는 고정값 대신 len(greetings) 같은 일반화된 방식으로 쓰면, 더 안정적이고 확장성 있는 코드가 됩니다.