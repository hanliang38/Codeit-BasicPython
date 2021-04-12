# 실습과제
# 100XP
# 리스트 원소들의 순서를 거꾸로 뒤집으려고 합니다.

# numbers라는 리스트가 주어졌을 때, for문을 사용하여 리스트를 거꾸로 뒤집어 보세요!

# numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# # 리스트 뒤집기
# # 코드를 입력하세요.

# print("뒤집어진 리스트: " + str(numbers))
# 뒤집어진 리스트: [19, 17, 13, 11, 7, 5, 3, 2]

numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
# 코드를 입력하세요.

# numbers.reverse()

for left in range(len(numbers) // 2):
    
    right = len(numbers) - left -1
    
    numbers[right], numbers[left] = numbers[left], numbers[right]
    
print("뒤집어진 리스트: " + str(numbers))