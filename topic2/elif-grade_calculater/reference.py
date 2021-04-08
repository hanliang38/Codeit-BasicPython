# 과제 해설close solution tab
# 만약 경우의 수가 2개라면 그냥 if문과 else문을 사용하면 되는데요. 지금은 경우의 수가 다섯 개(A, B, C, D, F)입니다. 그러면 elif문까지 사용해야겠죠.

# 어렵지 않은 문제이니 바로 답을 공개하겠습니다.

# 모범 답안
def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    if total >= 90:
        print("A")
    elif total >= 80:
        print("B")
    elif total >= 70:
        print("C")
    elif total >= 60:
        print("D")
    else:
        print("F")


# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)
# B를 받기 위해서는 총 점수가 '80점 이상이면서 90점 미만'이어야 하는데요. 위에 작성된 조건을 보면 80 <= total < 90이 아니라 그냥 total >= 80입니다. 왜 그런 걸까요?

# elif문으로 넘어 왔다는 것은 앞선 if문의 조건 부분을 통과하지 않았다는 뜻입니다. 그러니까 점수가 90점 미만일 수밖에 없다는 거죠.