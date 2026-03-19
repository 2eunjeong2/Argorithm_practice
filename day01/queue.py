'''
활용예시
- 프린터 출력 대기열
- ROS 토픽 메시지 버퍼
- BFS
''' 

# enquene : 뒤에 데이터 추가
# dequene : 앞의 데이터를 꺼냄

from collections import deque

queue = deque() # deque()함수 : 앞의 데이터를 꺼냄
queue.append('A') # enqueue A -> deque(['A'])
queue.append('B') # enqueue B -> deque(['A','B'])
queue.append('C') # enqueue C -> deque (['A','B','C'])
print(queue.popleft()) # -> 'A' (가장 먼저 넣은 A가 먼저나옴)
print(queue.popleft()) # -> 'B'