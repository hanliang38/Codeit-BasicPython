# 과제 해설close solution tab
# while 반복문을 이용해서 1부터 10까지 출력하려면 이렇게 하면 됩니다.

# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# 그러면 1부터 50까지 출력하려면? 이렇게 하면 되겠죠.

# i = 1
# while i <= 50:
#     print(i)
#     i += 1
# 저희는 1부터 100까지의 수 중 짝수(2, 4, 6, 8, ... , 96, 98, 100)만 출력하고 싶은 건데요. 생각해 보면 이건 1 * 2, 2 * 2, 3 * 2, 4 * 2, ... , 48 * 2, 49 * 2, 50 * 2와 같습니다. 그러면 위 코드에서 출력하는 값을 i * 2로 수정하기만 하면 되는 거죠!

# 모범 답안
i = 1
while i <= 50:
    print(i * 2)
    i += 1