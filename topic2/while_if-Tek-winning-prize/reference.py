# 과제 해설close solution tab
# 상수, 변수 정의
# 먼저 이 프로그램에서 사용될 상수와 변수를 모두 정의해 봅시다. 사용될 값들을 미리 적어 두면 틀이 잡힌 상태에서 고민을 시작할 수 있습니다.

# 상수(바뀌지 않을 값)와 변수(바뀔 값)를 나눠서 생각해 봅시다.

# 상수
# 먼저 상수는 어떤 것들이 있을까요?

# 이자율 (INTEREST_RATE) → 12%로 고정
# 2016년 은마아파트 가격 (APARTMENT_PRICE_2016) → 11억원으로 고정
#     # 상수 정의
# INTEREST_RATE = 0.12
# APARTMENT_PRICE_2016 = 1100000000
# 상수 이름은 모두 대문자로 쓴다는 점 기억해 두세요!

# 변수
# 이제 변수도 생각해 볼게요.

# 우선 반복문을 돌기 위해 사용되는 변수를 생각해 봅시다. 우리는 1988년부터 시작해서 2016년까지 반복을 하고 싶은 거죠? 그러면 연도를 나타내는 변수가 필요하겠네요. year라고 이름을 짓겠습니다.

# 또 어떤 변수가 필요할까요? 처음에는 은행에 5,000만원을 넣었지만, 매년 그 금액이 바뀔 텐데요. 이건 bank_balance라는 변수에 저장하겠습니다.

# 정리하자면 이렇습니다.

# 연도 (year) → 1988부터 2016까지 바뀜
# 은행 잔액 (bank_balance) → 50000000으로 시작해서 매년 쌓임
# # 변수 정의
# year = 1988
# bank_balance = 50000000
# while 반복문
# 반복문을 이용해서 1988년부터 2016년까지 돈이 얼마나 쌓이는지 계산해야 합니다. 어떻게 할 수 있을까요?

# while 반복문의 수행 부분에 들어갈 때마다 bank_balance가 12%씩 늘어나도록 하면 되겠죠? 코드로 표현하면 이렇습니다.

# bank_balance = bank_balance * (1 + INTEREST_RATE)
# 그런데 수행 부분에 몇 번이나 들어가야 할까요?

# 1988년에서 1989년으로 넘어갈 때 이자가 쌓여야겠죠? 마찬가지로 1989년에서 1990년으로 넘어갈 때도 이자가 쌓여야 합니다. 이런 식으로 2015년에서 2016년으로 넘어갈 때까지 수행 부분으로 들어가서 이자가 쌓여야 하는 거죠. 그러면 반복문을 이렇게 쓸 수 있습니다.

# while year < 2016:
#     bank_balance = bank_balance * (1 + INTEREST_RATE)
#     year += 1
# if, else문
# 마지막으로 결과를 출력하기만 하면 되는데요. 은행 잔액이 더 큰지 아파트 가격이 더 큰지에 따라서 출력 결과를 정해 주면 됩니다.

# if bank_balance > APARTMENT_PRICE_2016:
#     print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(bank_balance - APARTMENT_PRICE_2016)))
# else:
#     print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(APARTMENT_PRICE_2016 - bank_balance)))


# 모범 답안
# 상수 정의
INTEREST_RATE = 0.12
APARTMENT_PRICE_2016 = 1100000000

# 변수 정의
year = 1988
bank_balance = 50000000

while year < 2016:
    bank_balance = bank_balance * (1 + INTEREST_RATE)
    year += 1

if bank_balance > APARTMENT_PRICE_2016:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(bank_balance - APARTMENT_PRICE_2016)))
else:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(APARTMENT_PRICE_2016 - bank_balance)))
# 94193324원 차이로 동일 아저씨 말씀이 맞습니다.