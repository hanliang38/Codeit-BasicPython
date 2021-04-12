# 과제 해설close solution tab
# 1. 단어장 만들기
# 사전을 만들기 위해서는 괄호를 열고 닫고, 그 사이에 원하는 쌍(pair)들을 추가하면 됩니다.

# vocab = {
#     'sanitizer': '살균제',
#     'ambition': '야망',
#     'conscience': '양심',
#     'civilization': '문명'
# }
# 2. 새로운 단어들 추가
# vocab 사전에 새로운 key-value 쌍을 추가하기 위해서는 vocab[key] = value의 형태로 코드를 쓰면 됩니다.

# vocab['privilege'] = '특권'
# vocab['principle'] = '원칙'

# 모범 답안

# 1. 단어장 만들기
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명'
}
print(vocab)


# 2. 새로운 단어들 추가
vocab['privilege'] = '특권'
vocab['principle'] = '원칙'
print(vocab)