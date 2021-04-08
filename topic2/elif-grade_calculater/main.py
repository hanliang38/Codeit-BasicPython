# 실습과제
# 100XP
# 학생들에게 최종 성적을 알려 주는 '학점 계산기'를 만들려고 합니다.

# 이 수업에는 50점 만점의 중간고사와 50점 만점의 기말고사가 있는데요. 두 시험의 점수를 합해서 최종 성적을 내는 방식입니다. 규칙은 다음과 같습니다.

# A: 90점 이상
# B: 80점 이상 90점 미만
# C: 70점 이상 80점 미만
# D: 60점 이상 70점 미만
# F: 60점 미만
# print_grade 함수는 파라미터로 중간고사 점수 midterm_score와 기말고사 점수 final_score를 받고, 최종 성적을 출력합니다.

# def print_grade(midterm_score, final_score):
#     total = midterm_score + final_score
#     # 코드를 쓰세요.


# # 테스트
# print_grade(40, 45)
# print_grade(20, 35)
# print_grade(30, 32)
# print_grade(50, 45)
# B
# F
# D
# A

def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    # 코드를 쓰세요.
    if 90 <= total:
        print("A")
    elif 80 <= total < 90:
        print("B")
    elif 70 <= total < 80:
        print("C")
    elif 60 <= total < 70:
        print("D")
    else:
        print("F")


# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)