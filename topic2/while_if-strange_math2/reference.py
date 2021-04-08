# 과제 해설
# 문제 단순화하기
# 먼저 '2 또는 3의 배수'라는 조건은 무시하고, 그냥 10보다 작은 자연수의 합을 출력하는 프로그램을 작성해 봅시다.

# 10보다 작은 자연수의 합을 출력하는 프로그램을 쓰기 위해서는 누적된 합을 보관하는 변수가 필요한데요. 우리는 그 변수를 total이라고 하겠습니다. 그러면 이렇게 작성할 수 있습니다.

# i = 1
# total = 0

# while i < 10:
#     total += i  # total = total + i와 동일
#     i += 1  # i = i + 1과 동일

# print(total)
# 45
# 반복문을 돌면서 매번 total에 i를 더해 주면 되는 거죠. 그리고 반복문이 끝나면 총 누적된 합인 total을 출력하면 됩니다.

# 만약 1,000보다 작은 자연수의 합을 출력하려면, 위 코드에서 10을 1000으로 바꿔 주기만 하면 되겠죠?

# 조건 추가하기
# 이제 위 코드에서 한 줄만 추가하면 되는데요. total += 1을 매번 하는 게 아니라, i가 '2 또는 3의 배수'라는 조건을 부합할 때만 부르는 것입니다.

# 2 또는 3의 배수인지 판단하기 위해서는, 2 또는 3으로 나누어 떨어지는지 확인해야 합니다. 어떤 수가 2 또는 3으로 나누어 떨어진다는 것은, 2 또는 3으로 나누었을 때 나머지가 0이라는 의미입니다.

# i라는 변수가 2로 나누어 떨어지는지 확인하는 코드는 i % 2 == 0입니다. i라는 변수가 3으로 나누어 떨어지는지 확인하는 코드는 i % 3 == 0입니다. 그렇다면 i가 2 또는 3으로 나누어 떨어지는지 확인하는 코드는?

# 그냥 불린 연산 or을 사용해서 i % 2 == 0 or i % 3 == 0입니다.

# 모범 답안
i = 1
total = 0

while i < 1000:
    if i % 2 == 0 or i % 3 == 0:
        total += i
    i += 1

print(total)
# 참고로 i += 1은 if문 밖에 있어야 합니다. 그렇지 않으면 끝이 안 나는 "무한 루프"에 빠지게 됩니다. 주의해 주세요!