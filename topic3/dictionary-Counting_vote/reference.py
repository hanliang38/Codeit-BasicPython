# 과제 해설close solution tab
# for문을 이용해서 votes에 있는 후보 이름을 순서대로 name이라는 변수에 지정합니다. name을 vote_counter 사전에 반영하면 되는데요. 두 가지 경우가 있습니다.

# 해당 후보(name)가 아직 vote_counter에 없는 케이스
# 해당 후보(name)가 이미 vote_counter에 있는 케이스
# 1번 케이스는 해당 후보가 첫 득표를 한 상황인데요. 그러면 그냥 vote_counter[name] = 1을 하면 되겠죠?

# 2번 케이스는 해당 후보가 이미 최소 하나의 득표를 한 상황입니다. 이 경우 기존 득표 수에 1을 늘려 주면 되는데요. 그러면 vote_counter[name] += 1을 하면 됩니다.



# 모범 답안

# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

# 후보별 득표수 사전
vote_counter = {}

# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes:
    if name not in vote_counter:
        vote_counter[name] = 1
    else:
        vote_counter[name] += 1

# 후보별 득표수 출력
print(vote_counter)