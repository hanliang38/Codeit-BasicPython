# 과제 해설close solution tab
# dict의 key와 value를 모두 받아오려면 어떻게 해야 할까요?

# 이렇게 하면 됩니다.

# for key, value in dict.items():
# 각 key-value 쌍을 new_dict에 저장하고 싶은 건데요. new_dict[key] = value를 하면 기존 dict와 똑같은 사전이 만들어집니다. new_dict[value] = key를 해야 뒤집힌 사전을 만들 수 있겠죠?



# 모범 답안

# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
def reverse_dict(dict):
    new_dict = {}  # 새로운 사전
    
    # dict의 key와 value를 뒤집어서 new_dict에 저장
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