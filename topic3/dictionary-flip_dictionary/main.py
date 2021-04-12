# 실습과제
# 태호는 영어 단어 공부를 위해서 단어장 프로그램을 만들었습니다. 하지만 이번에는 영-한으로 공부하는 것이 아니라, 한-영으로 공부를 해 보고 싶습니다.

# 사전의 key와 value를 뒤집어 주는 함수 reverse_dict를 작성해 주세요. reverse_dict는 파라미터로 사전 dict를 받고, key와 value가 뒤집힌 새로운 사전을 리턴합니다.

# 실행 결과
# # 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
# def reverse_dict(dict):
#     new_dict = {}  # 새로운 사전
    
#     # dict의 key와 value를 뒤집어서 new_dict에 저장
#     # 코드를 입력하세요.
    
#     return new_dict  # 변환한 새로운 사전 리턴


# # 영-한 단어장
# vocab = {
#     'sanitizer': '살균제',
#     'ambition': '야망',
#     'conscience': '양심',
#     'civilization': '문명',
#     'privilege': '특권',
#     'principles': '원칙'
# }

# # 기존 단어장 출력
# print("영-한 단어장\n{}\n".format(vocab))

# # 변환된 단어장 출력
# reversed_vocab = reverse_dict(vocab)
# print("한-영 단어장\n{}".format(reversed_vocab))
# 위 코드를 완성하고 실행하면 아래와 같이 출력됩니다.

# 영-한 단어장
# {'sanitizer': '살균제', 'ambition': '야망', 'conscience': '양심', 'civilization': '문명', 'privilege': '특권', 'principles': '원칙'}

# 한-영 단어장
# {'살균제': 'sanitizer', '야망': 'ambition', '양심': 'conscience', '문명': 'civilization', '특권': 'privilege', '원칙': 'principles'}



# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
def reverse_dict(dict):
    new_dict = {}  # 새로운 사전
    
    # dict의 key와 value를 뒤집어서 new_dict에 저장
    # 코드를 입력하세요.
    for key, value in dict.items():
        new_dict[value] = key
    
    return new_dict  # 변환한 새로운 사전 리턴


# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

# 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))