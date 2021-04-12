# 과제 해설
# 가장 단순한 방식
# 가장 단순하게 코드를 짜면 이렇습니다.

# for a in range(1, 1000):
#     for b in range(1, 1000):
#         for c in range(1, 1000):
#             if a * a +  b * b == c * c and a < b < c and a + b + c == 1000:
#                 print(a * b * c)

# 이 코드를 막상 실행해 보면, 굉장히 오랜 시간이 걸릴 것입니다. 논리적으로 봤을 때 언젠가는 올바른 정답을 찾아 주는 코드입니다. 하지만 너무 오래 걸려서 사실상 사용할 수 없다고 보시면 되는데요. 이런 걸 "비효율적인 알고리즘"이라고 합니다.

# 알고리즘이 비효율적인 이유를 간단히만 설명드리겠습니다.

# a가 가능한 경우는 1부터 999까지, b가 가능한 경우는 1부터 999까지, c가 가능한 경우는 1부터 999까지인데요. 그러면,

# if a * a + b * b == c * c and a < b < c and a + b + c == 1000:
#     print(a * b * c)

# 위 코드가 총 997,002,999번 실행됩니다. 약 10억 번 정도 실행되는 거죠.

# 효율적인 방식
# 우리는 ﻿a + b + c = 1000a+b+c=1000﻿이라는 조건을 지켜야 합니다. 그말인즉슨 ﻿c = 1000 - a - bc=1000−a−b﻿라는 거죠. 이 점을 잘 활용하면 더 효율적인 코드를 작성할 수 있습니다.

# 모범 답안
for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - a - b
        if a * a + b * b == c * c and a < b < c:
            print(a * b * c)

# 이렇게 하면 정답인 31875000를 구할 수 있습니다.