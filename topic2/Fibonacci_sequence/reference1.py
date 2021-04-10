# 과제 해설close solution tab
# 일단 50개의 항이 조금 부담될 수 있으니, 10개의 항만 출력하는 걸 목표로 합시다. 어차피 10개를 제대로 출력할 수 있으면, 50개도 아무런 문제 없이 출력할 수 있을 테니까요.

# 반복문 틀 작성
# 10개의 항을 출력하기 위해서는 반복문을 열 번 돌아야겠죠? 열 번 도는 반복문부터 작성해 봅시다.

# i = 1

# while i <= 10:
#     i += 1
# 필요한 변수 정의
# 피보나치 수열의 항은 앞선 두 항의 합으로 계산되는데요. 따라서 피보나치 수열의 항들을 순서대로 출력하기 위해서는 늘 마지막 두 항을 변수에 보관해야 합니다.

# '현재 항'은 변수 current에, 그리고 '직전 항'은 변수 previous에 저장을 하겠습니다. 처음에는 current를 1로 설정하고 previous를 0으로 설정하면 되겠죠?

# previous = 0
# current = 1
# i = 1

# while i <= 10:
#     # 우리가 반복적으로 무엇을 해야 할까요?
#     i += 1
# 이제 while 반복문의 수행 부분만 채워 넣으면 됩니다.

# 수행 부분 채워 넣기
# 수행 부분에서 해야 할 일은 크게 두 가지입니다.

# current를 출력
# previous와 current를 적절히 수정
# 1번은 그냥 print(current)를 하면 되니까 먼저 채워 넣겠습니다.

# previous = 0
# current = 1
# i = 1

# while i <= 10:
#     print(current)
#     # previous와 current를 적절히 수정
#     i += 1
# previous와 current 수정하기
# 2번이 약간 헷갈리는 부분인데요. 수행 부분에서 previous와 current를 어떻게 수정할 수 있을까요? 일단 단순하게 생각하면 이렇습니다.

# previous ← current
# current ← current + previous
# 그리고 위 로직을 코드로 나타내면 아래와 같습니다.

# previous = current
# current = current + previous
# 그런데 사실 위 코드처럼 하면 문제가 생깁니다. 잘 생각해 보세요. previous = current를 하면, previous와 current가 같은 값을 저장하게 됩니다. 그리고 기존의 previous 값은 잃어버리게 되죠.

# 예를 들어서 previous가 정수 2고 current가 정수 3이라고 생각해 보세요. previous = current를 하면 어떻게 되나요? previous는 정수 3으로 바뀌고, current도 정수 3이죠? 기존 previous에 있던 정수 2는 완전히 잃어버리게 됩니다.

# 이 문제를 해결하기 위해서, 임시 보관소 역할을 할 변수를 만들어야 합니다.

# temp = previous  # previous를 임시 보관소 temp에 저장
# previous = current
# current = current + temp  # temp에는 기존 previous 값이 저장돼 있음
# 그러면 이제 문제 없이 previous와 current를 수정할 수 있습니다. 여기까지 완성된 코드를 봅시다.

# 모범 답안
previous = 0
current = 1
i = 1

while i <= 10:
    print(current)
    temp = previous  # previous를 임시 보관소 temp에 저장
    previous = current
    current = current + temp  # temp에는 기존 previous 값이 저장돼 있음
    i += 1
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 피보나치 수열의 10개 항이 잘 나오는 것 같죠? 이제 while i <= 10:을 while i <= 50:으로 수정하기만 하면 됩니다!