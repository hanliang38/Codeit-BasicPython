# 과제 해설
# 문자열의 첫 번째 원소와 마지막 원소를 비교해서 일치하는지 확인해야 합니다. 그 다음 문자열의 두 번째 원소와 끝에서 두 번째 원소를 비교해서 일치하는지 확인해야겠죠.

# 문자열 word의 첫 번째 원소의 인덱스는 0이고, 마지막 원소의 인덱스는 len(word) - 1입니다. 문자열 word의 두 번째 원소의 인덱스는 1이고, 끝에서 두 번째 원소의 인덱스는 len(word) - 2입니다.

# 이걸 어떻게 일반화할 수 있을까요?

# i를 0부터 1씩 늘린다고 가정했을 때, 인덱스 i에 있는 값과 인덱스 len(word) - i - 1에 있는 값을 비교하면 됩니다!

# 참고로 i를 0부터 len(word) - 1까지 반복할 필요는 없습니다. 어차피 반대쪽과 비교하는 것이기 때문에 i를 len(word) // 2까지만 반복해도 이미 모든 확인은 끝나는 거죠!

# 모범 답안
def is_palindrome(word):
    for left in range(len(word) // 2):
        # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    # for문에서 나왔다면 모든 쌍이 일치
    return True


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))